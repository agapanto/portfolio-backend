"""portfolio-backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .viewsets import (
    PortfolioViewSet,
    PortfolioItemViewSet,
)

router = DefaultRouter()
router.register(
    r'portfolios',
    PortfolioViewSet,
    basename='portfolio'
)
router.register(
    r'portfolioitems',
    PortfolioItemViewSet,
    basename='portfolio_item'
)


urlpatterns = [
    path('api/', include((router.urls, 'agapanto_portfolios'))),
]
