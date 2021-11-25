from django.urls import path
from .views import EntryListAPIView, FollowListAPIView, ProfileLitsAPIView, SelfProfileRetrieveAPIView, UserRetrieveAPIView


urlpatterns = [
    path(
        'selfprofile/<int:user>/',
        SelfProfileRetrieveAPIView.as_view(),
        name="detail"),
    path(
        'user/<int:pk>/',
        UserRetrieveAPIView.as_view()),
    path(
        'profile/<int:user>/',
        ProfileLitsAPIView.as_view(),
        name="detail"),
    path(
        'entries/',
        EntryListAPIView.as_view()),
    path(
        'follows/',
        FollowListAPIView.as_view()),
]
