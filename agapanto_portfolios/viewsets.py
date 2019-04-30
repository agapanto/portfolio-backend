from rest_framework import (
    viewsets,
)
from .serializers import (
    PortfolioSerializer,
    PortfolioItemSerializer,
)


class PortfolioViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing a portfolio.
    """
    serializer_class = PortfolioSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]

    def get_queryset(self):
        return self.request.user.portfolios.all()


class PortfolioItemViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing a portfolioitem.
    """
    serializer_class = PortfolioItemSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]

    def get_queryset(self):
        return self.request.user.portfolioitems.all()
