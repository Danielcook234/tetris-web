from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tetris-home'),
    path('start/', views.start_btn, name='start-btn')
]