"""agapanto_portfolios models."""
# import uuid
from django.conf import settings
from django.db import models
# from django.contrib.postgres.fields import JSONField
from rest_framework_apicontrol.mixins import (
    STATUS_FIELD_MAX_LENGTH,
    # ActiveModelMixin,
    # EnabledModelMixin,
    PerAppModelMixin,
    InstanceStatusModelMixin,
    TrackableModelMixin,
    UniqueIDModelMixin,
)

PORTFOLIO_STATUS_CHOICES = (
    ('hidden', 'hidden'),
    ('published', 'published'),
)

PORTFOLIO_READ_ACCESS_CHOICES = (
    ('owner', 'owner'),
    ('group', 'group'),
    ('public', 'public'),
)

PORTFOLIO_WRITE_ACCESS_CHOICES = (
    ('owner', 'owner'),
    ('group', 'group'),
    ('public', 'public'),
)


class Portfolio(InstanceStatusModelMixin,
                TrackableModelMixin,
                UniqueIDModelMixin):
    """Portfolio: group of items to show to others."""

    name = models.CharField(
        max_length=64
    )
    description = models.TextField()
    image = models.ImageField()
    current_status = models.CharField(
        max_length=STATUS_FIELD_MAX_LENGTH,
        choices=PORTFOLIO_STATUS_CHOICES,
    )
    read_access = models.CharField(
        max_length=STATUS_FIELD_MAX_LENGTH,
        choices=PORTFOLIO_READ_ACCESS_CHOICES
    )
    write_access = models.CharField(
        max_length=STATUS_FIELD_MAX_LENGTH,
        choices=PORTFOLIO_WRITE_ACCESS_CHOICES
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        pass

    def __str__(self):
        return self.unique_id


class PortfolioItem(InstanceStatusModelMixin,
                    TrackableModelMixin,
                    UniqueIDModelMixin):
    """PortfolioItem: an item inside a portfolio."""

    name = models.TextField()
    description = models.TextField()
    image = models.ImageField()
    current_status = models.CharField(
        max_length=STATUS_FIELD_MAX_LENGTH,
        choices=PORTFOLIO_STATUS_CHOICES,
    )
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        pass

    def __str__(self):
        return self.unique_id
