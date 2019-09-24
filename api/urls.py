from django.urls import path, include

from .views import todoviews

urlpatterns = [
    path('', todoviews.as_view() ),
]