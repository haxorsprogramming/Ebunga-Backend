from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

import mysql.connector
import json

mydb = mysql.connector.connect(host='localhost', user='root', password='', database='dbs_ebunga_front_end')

def test_koneksi(request):

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tbl_provinsi")
    myresult = mycursor.fetchall()
    rowarray_list = []

    for row in myresult:
        h = (row[0], row[1])
        rowarray_list.append(h)

    # return HttpResponse(j)
    return JsonResponse(myresult, safe=False)

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