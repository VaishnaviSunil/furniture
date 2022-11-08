from django.urls import path
from . import views
app_name='furniture_home'
urlpatterns = [
    path('',views.index,name='ind'),
    path('home',views.home,name='hom'),
    path('bedroom',views.bed,name='bed'),
    path('livingroom',views.living,name='live'),
    path('about',views.about,name='abt'),
    path('contact',views.contact,name='con'),
    path('accessories',views.accessory,name='asry'),
]