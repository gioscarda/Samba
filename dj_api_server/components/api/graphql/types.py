from graphene_django import DjangoObjectType
from ...models import Property, Component, ComponentsType


class PropertyType(DjangoObjectType):

    class Meta:
        model = Property
        fields = '__all__'


class ComponentType(DjangoObjectType):

    class Meta:
        model = Component
        fields = '__all__'


class ComponentsTypeType(DjangoObjectType):

    class Meta:
        model = ComponentsType
        fields = '__all__'
