from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django_filters import rest_framework as filters

from .models import Entry, Follow, Profile
from .serializers import EntrySerializer, FollowSerializer, SelfProfileSerializer, ProfileSerializer


class SelfProfileRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SelfProfileSerializer
    lookup_field = 'user'
    queryset = Profile.objects.all()


class ProfileLitsAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
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
