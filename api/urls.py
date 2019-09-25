from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views



router = DefaultRouter()
router.register('todoViewSet', views.todoviewset, base_name='todoViewSet')
router.register('UserProfileViewSet', views.UserProfileViewSet)

urlpatterns = [
    path('todoapiview', views.todoviews.as_view() ),
    path('login/', views.UserLoginViewSet.as_view()),
    path('', include(router.urls))
]