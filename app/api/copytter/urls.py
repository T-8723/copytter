from django.urls import path
from .views import EntryListAPIView, FollowListAPIView, ProfileLitsAPIView, SelfProfileRetrieveAPIView


urlpatterns = [
    path(
        'selfprofile/<int:user>/',
        SelfProfileRetrieveAPIView.as_view(),
        name="detail"),
    path(
        'profile/<int:pk>/',
        ProfileLitsAPIView.as_view(),
        name="detail"),
    path(
        'entries/',
        EntryListAPIView.as_view()),
    path(
        'follows/',
        FollowListAPIView.as_view()),
]
