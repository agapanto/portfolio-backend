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
    filterset_fields = (
        'current_status',
        'read_access',
        'write_access',
        'user',
    )
    ordering_fields = (
        'name',
        'current_status',
        'user',
        'created_at',
        'updated_at',
    )

    def get_queryset(self):
        return self.request.user.portfolios.filter(
            instance_status='active'
        )


class PortfolioItemViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing a portfolioitem.
    """
    serializer_class = PortfolioItemSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
    filterset_fields = (
        'current_status',
        'portfolio',
        'portfolio__unique_id',
        'user',
        'created_at',
        'updated_at',
    )
    ordering_fields = (
        'name',
        'current_status',
        'portfolio',
        'portfolio__unique_id',
        'user',
    )

    def get_queryset(self):
        return self.request.user.portfolioitems.filter(
            instance_status='active'
        )
