import django_filters as filters
from .models import Property
from django import forms
from django.db import models

class PropertyFilter(filters.FilterSet):
    price = filters.NumericRangeFilter('price', 'range')
    class Meta:
        model = Property
        fields = ['city', 'type', 'purchase', 'new', 'repaired']
        # filter_overrides = {
        #     models.BooleanField: {
        #         'filter_class': filters.BooleanFilter,
        #         'extra': lambda f: {
        #             'widget': forms.CheckboxInput,
        #         },
        #     }
        # }