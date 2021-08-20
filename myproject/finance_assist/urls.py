from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('action/', views.action, name='action'),
    path('<int:action_id>/', views.detail, name='detail'),
    path('report/', views.report, name='report'),
]