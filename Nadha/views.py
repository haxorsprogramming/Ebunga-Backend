from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


def about(request):
    return render(request, "about.html")

def readget(request, idProduct):
    data = {
        'name': idProduct,
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)

@csrf_exempt
def jsontest(request):
    name = request.POST.get("name")
    data = {
        'name': name,
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)