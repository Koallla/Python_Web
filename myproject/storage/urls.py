from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('products/', views.products_view, name='products'),
]