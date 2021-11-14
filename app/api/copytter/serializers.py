from rest_framework import serializers
from .models import Entry, Follow, Profile


class SelfProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Entry
        fields = '__all__'