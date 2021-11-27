from rest_framework import serializers
from .models import Entry, Follow, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class SelfProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'


class UpdateSelfProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'gender',
            'birth_date',
            'location',
            'age',
            'icon_pass',
            'profile_message',
            'profile_user_id',
            'profile_first_registed')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = (
            'user',
            'gender',
            'birth_date',
            'location',
            'age',
            'icon_pass',
            'profile_message',
            'profile_user_id',
            'follow_count',
            'follower_count'
        )


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):
    author = ProfileSerializer()

    class Meta:
        model = Entry
        fields = '__all__'
