from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django_filters import rest_framework as filters

from .models import Entry, Follow, Profile
from django.contrib.auth.models import User
from .serializers import EntrySerializer, FollowSerializer, SelfProfileSerializer, ProfileSerializer, UserSerializer, UpdateSelfProfileSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SelfProfileRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SelfProfileSerializer
    lookup_field = 'user'
    queryset = Profile.objects.all()


class UpdateSelfProfileAPIView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdateSelfProfileSerializer
    queryset = Profile.objects.all()


class ProfileLitsAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
    lookup_field = 'user'
    queryset = Profile.objects.all()


class FollowListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()


class FollowEntryListAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EntrySerializer

    def get(self, request):
        filterset = FilterEntry(
            request.query_params,
            queryset=Entry.objects.all())
        serializer = EntrySerializer(instance=filterset.qs, many=True)
        return Response(serializer.data)


class EntryCreateAPIView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()


class EntryListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EntrySerializer

    def get(self, request):
        filterset = FilterEntry(
            request.query_params,
            queryset=Entry.objects.all())
        serializer = EntrySerializer(instance=filterset.qs, many=True)
        return Response(serializer.data)


class FilterEntry(filters.FilterSet):

    """ EntryモデルのFilter """
    class Meta:
        model = Entry
        fields = '__all__'
