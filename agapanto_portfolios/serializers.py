from rest_framework import (
    serializers,
)
from .models import (
    Portfolio,
    PortfolioItem,
)


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = (
            'name',
            'description',
            'image',
            'current_status',
            'read_access',
            'write_access',
            # 'user'
        )


class PortfolioItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioItem
        fields = (
            'name',
            'description',
            'image',
            'current_status',
            'portfolio',
            # 'user'
        )
