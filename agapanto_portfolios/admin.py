from django.contrib import admin
from rest_framework_apicontrol.admin import (
    TrackableModelAdmin,
)
from .models import (
    Portfolio,
    PortfolioItem,
)


admin.site.register(Portfolio, TrackableModelAdmin)
admin.site.register(PortfolioItem, TrackableModelAdmin)
