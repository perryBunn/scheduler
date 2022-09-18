from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("<str:short_name>/", views.floor, name="floor"),
    path("<str:short_name>/<int:period>/", views.period, name="period"),
]
