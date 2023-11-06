from django.db import models


class Property(models.Model):
    """ Component property class. """

    key = models.CharField(
        max_length=50
    )
    value = models.TextField(
        max_length=1000
    )
    component = models.ForeignKey(
        to='Component',
        related_name='properties',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.component}_{self.key}'


class ComponentsType(models.Model):
    """ Components type class. """

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name


class Component(models.Model):
    """
    Frontend generic component class.
    - order: it distinguishes the component from others at the same level (same parent and same type)
    - type: component type (es. Button, Page, Section, Layout, ect.)
    - parent: the parent component
    """

    order = models.PositiveSmallIntegerField(
        editable=False
    )
    type = models.ForeignKey(
        to='ComponentsType',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        obj_str = f'{self.type}_{self.order}'
        if self.parent:
            obj_str = f'{self.parent}_{obj_str}'
        return obj_str

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        same_level_objs = Component.objects.filter(type=self.type, parent=self.parent).count()
        self.order = same_level_objs + 1
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)
