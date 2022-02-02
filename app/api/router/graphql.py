# Created by Kelvin_Clark on 2/2/2022, 3:07 AM
import strawberry
from strawberry.fastapi import GraphQLRouter

from app.data.schema.gaphql.query import Query
from app.api.dependencies.graphql import SQLAlchemySessionExtension

__schema = strawberry.Schema(query=Query, extensions=[SQLAlchemySessionExtension])
router = GraphQLRouter(path="/graphql", schema=__schema)
