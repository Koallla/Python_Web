from storage.views import MyView
from django.urls import path, include


urlpatterns = [
    path('products/', MyView.as_view())
]
