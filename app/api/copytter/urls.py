from django.urls import path
from .views import EntryListAPIView, FollowListAPIView, ProfileLitsAPIView, SelfProfileRetrieveAPIView, UserRetrieveAPIView, EntryCreateAPIView, UpdateSelfProfileAPIView

urlpatterns = [
    path(
        'selfprofile/<int:user>/',
        SelfProfileRetrieveAPIView.as_view(),
        name="detail"),
    path(
        'update/selfprofile/<int:pk>/',
        UpdateSelfProfileAPIView.as_view(),
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
        'create/entry/',
        EntryCreateAPIView.as_view()),
    path(
        'follows/',
        FollowListAPIView.as_view()),
]
