from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello_viewset')
router.register('profile',views.UserProfileViewSet,base_name='profile')
router.register('login', views.LoginViewSet,base_name='login')
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view()),
    path('',include(router.urls)) 
]

