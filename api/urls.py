from django import views
from django.urls import path
from .views import HeroViewSet


urlpatterns=[
    path('api-auth/',HeroViewSet.as_view(),name="api")
]