from django.urls import path
from . import views

urlpatterns = [  # IP주소/major/
    path('', views.index),
    path('dashboard/', views.dashboard),
    path('user/', views.user),
    path('score/', views.score),
]