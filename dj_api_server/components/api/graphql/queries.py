import graphene
from .types import PropertyType, ComponentType, ComponentsTypeType
from ...models import Component, ComponentsType, Property


class Query(graphene.ObjectType):

    components = graphene.List(ComponentType)
    components_types = graphene.List(ComponentsTypeType)
    properties = graphene.List(PropertyType)

    def resolve_components(root, info):
        return Component.objects.all()

    def resolve_components_types(root, info):
        return ComponentsType.objects.all()

    def resolve_properties(root, info):
        return Property.objects.all()
