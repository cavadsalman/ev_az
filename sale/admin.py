from django.contrib import admin
from .models import (
    City, PropertyType, PurchaseType,
    Property, PropertyFeature, PorpertyImage
)

# Register your models here.
admin.site.register(City)
admin.site.register(PropertyType)
admin.site.register(PurchaseType)
admin.site.register(Property)
admin.site.register(PropertyFeature)
admin.site.register(PorpertyImage)