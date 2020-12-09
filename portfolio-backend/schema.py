# cookbook/schema.py
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from agapanto_portfolios.models import (
    Portfolio,
    PortfolioItem,
)


class PortfolioNode(DjangoObjectType):
    image = graphene.String()

    class Meta:
        model = Portfolio
        fields = (
            "id",
            "name",
            "description",
            "image",
            "current_status",
            "user"
        )
        filter_fields = [
            'name',
            'current_status',
            'user'
        ]
        interfaces = (
            graphene.relay.Node,
        )

    def resolve_image(self, info):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return ""

class PortfolioItemNode(DjangoObjectType):
    # https://docs.graphene-python.org/projects/django/en/latest/queries/#default-queryset
    image = graphene.String()

    class Meta:
        model = PortfolioItem
        fields = (
            "id",
            "name",
            "description",
            "image",
            "url",
            "current_status",
            "portfolio",
            "user"
        )
        filter_fields = [
            'name',
            'current_status',
            'portfolio',
            'user'
        ]
        interfaces = (
            graphene.relay.Node,
        )

    def resolve_image(self, info):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return ""

class Query(graphene.ObjectType):
    portfolio = graphene.relay.Node.Field(PortfolioNode)
    all_portfolios = DjangoFilterConnectionField(PortfolioNode)

    portfolio_item = graphene.relay.Node.Field(PortfolioItemNode)
    all_portfolio_items = DjangoFilterConnectionField(PortfolioItemNode)

schema = graphene.Schema(
    query=Query
)
