from django.urls import path
from . import views

urlpatterns = [
    path("sessioninfo", views.SessionView.as_view()),
]
