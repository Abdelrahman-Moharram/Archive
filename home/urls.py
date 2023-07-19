from django.urls import path 
from .views import index, get_far3y_from_asasy

app_name = "home"

urlpatterns = [
    path('',index, name="index"),
    path('get_far3y/<int:id>/',get_far3y_from_asasy, name="get_far3y"),
    
]