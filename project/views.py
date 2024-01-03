# Create your views here.
from django.shortcuts import render

def index_page(request):
    return render(request, 'home_page.html')