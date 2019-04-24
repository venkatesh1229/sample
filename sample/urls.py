#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.welcome),
    path('count/', views.count, name='count'),

]
