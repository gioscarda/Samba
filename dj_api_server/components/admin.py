from django.contrib import admin
from .models import Property, Component, ComponentsType

admin.site.register(Property)
admin.site.register(Component)
admin.site.register(ComponentsType)
