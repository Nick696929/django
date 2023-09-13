from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('list/', views.list, name='list'),
    path('main/', views.main, name='main')
]