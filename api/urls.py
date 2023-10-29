from django.urls import path
from api import views

urlpatterns = [
    path('', views.patent_by_attr, name='home'),
]

