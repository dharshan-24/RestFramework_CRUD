from django.urls import path 
from .models import *
from .views import *



urlpatterns = [
    path("add/",StudentData.as_view()),
    path("all/<int:pro_id>/",StudentData.as_view()),
    path("all/",StudentData.as_view()),
    path("update/<int:pro_id>/",StudentData.as_view()),
    path("delete/<int:pro_id>/",StudentData.as_view()),
    
]
