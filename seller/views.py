from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def login_page(request):
    return render(request, 'seller/login.html')

def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'seller/register.html', context={
        'form': form
    })