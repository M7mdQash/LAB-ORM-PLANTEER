from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# TODO: make home view

def home_view(request):
    return render(request, 'main/index.html')