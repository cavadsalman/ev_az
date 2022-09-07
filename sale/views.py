from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Property
from .filters import PropertyFilter

# Create your views here.

def home(request):
    return render(request, 'sale/home.html')

def property_detail(request):
    return render(request, 'sale/property-detail.html')

def property_list(request):
    properties_filter = PropertyFilter(request.GET, queryset=Property.objects.all())
    properties = properties_filter.qs
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(properties, 4)
    page = paginator.page(page_number)
    return render(request, 'sale/property-list.html', context={
        'properties': page.object_list,
        'paginator': paginator,
        'page_object': page,
        'filter': PropertyFilter
    })