from storage.views import MyView
from django.urls import path, include

from . import views



urlpatterns = [
    path('products/', MyView.as_view())
]
