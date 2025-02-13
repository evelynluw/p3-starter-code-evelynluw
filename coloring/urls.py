from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('color/<str:filename>/', views.color, name="color"),
    path('choose_template', views.choose_template, name='choose_template')
]
