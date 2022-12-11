from django.urls import path
from . import views


urlpatterns = [  # IP주소/major/
    path('', views.index),
    path('dashboard/', views.dashboard),  # 대시보드
    path('CSresult/', views.CSresult), #CS솔루션결과
    path('FNresult/', views.FNresult), #FN솔루션결과
    path('user/', views.user),  # 유저 프로필
    path('score/', views.score),  # 학점 등록 & 비교과 이수 현황
    path('register/', views.register),  # 전선 수강 내역
    path('apply/', views.apply),  # 희망 지망 선택

]

