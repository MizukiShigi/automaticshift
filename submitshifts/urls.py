from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SubmitShifsView.as_view(), name='submit_shifts'),
]
