from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request, 'product.html')