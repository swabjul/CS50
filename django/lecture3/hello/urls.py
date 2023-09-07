from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("<str:name>", views.greet, name="greet"),
  path("swab", views.swab, name="swab"),
  path("jul", views.jul, name="jul")
]