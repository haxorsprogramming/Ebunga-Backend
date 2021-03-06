from django.contrib import admin
from django.urls import path

from . import views
from ebungabn import views as ebn
from siswa import views as r_siswa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('product/', ebn.product),
    path('json-test/', views.jsontest),
    path('product-detail/<slug:idProduct>/', views.readget),
    path('test-mysql/', views.test_koneksi),
    path('add-siswa/', r_siswa.add_siswa)
]
