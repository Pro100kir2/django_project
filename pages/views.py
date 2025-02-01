from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'pages/templates/home.html')

def about_view(request):
    return render(request, 'pages/templates/about.html')

@login_required
def admin_only_view(request):
    return render(request, 'pages/templates/admin_only.html')
