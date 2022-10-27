from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

# from core.schema import schema
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", GraphQLView.as_view(graphiql=True)),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),

]
