from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('offers/',views.offers,name='offers'),
    path('contacts/',views.contacts,name='contacts'),
    path('login/',views.login,name='login'),
    path('logout/',views.login,name='logout'),
]