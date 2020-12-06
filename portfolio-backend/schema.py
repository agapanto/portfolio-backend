# cookbook/schema.py
import graphene
from graphene_django import DjangoObjectType
from agapanto_portfolios.models import (
    Portfolio,
    PortfolioItem,
)


class PortfolioType(DjangoObjectType):
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

class PortfolioItemType(DjangoObjectType):
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


class Query(graphene.ObjectType):
    all_portfolios = graphene.List(PortfolioType)
    all_portfolio_items = graphene.List(PortfolioItemType)

    def resolve_all_portfolios(root, info):
        return Portfolio.objects.all()

    def resolve_all_portfolio_items(root, info):
        # We can easily optimize query count in the resolve method
        return PortfolioItem.objects.select_related("portfolio").all()

schema = graphene.Schema(
    query=Query
)
