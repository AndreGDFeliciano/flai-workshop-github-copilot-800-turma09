from rest_framework import serializers
from .models import Team, User, Workout, Activity, Leaderboard


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at', 'member_count']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'full_name', 'team_id', 'avatar', 'created_at', 'total_points']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'category', 'points_per_unit', 'unit']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'workout_id', 'workout_name', 'amount', 'unit', 'points', 'date', 'created_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_id', 'username', 'full_name', 'team_id', 'total_points', 'rank', 'updated_at']
