from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

import mysql.connector
import json

mydb = mysql.connector.connect(host='localhost', user='root', password='', database='dbs_test_django')
mycursor = mydb.cursor()
# Create your views here.
@csrf_exempt
def add_siswa(request):
    if request.method == 'GET':
        return HttpResponse("ini get")
    elif request.method == 'POST':
        nama = request.POST.get("nama")
        kelas = request.POST.get("kelas")
        email = request.POST.get("email")
        sql = "INSERT INTO tbl_siswa (nama, kelas, email) VALUES (%s, %s, %s);"
        val = (nama, kelas, email)
        mycursor.execute(sql, val)

        mydb.commit()
        data = {'name': nama,'status':'sukses'}
        return JsonResponse(data)
