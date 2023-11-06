import graphene
from components.api.graphql.schema import schema as components_schema


class Query(components_schema.Query):
    # Inherits all classes and methods from app-specific queries, so no need
    # to include additional code here.
    pass


schema = graphene.Schema(query=Query)
