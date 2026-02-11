from rest_framework import viewsets
from .models import Team, User, Workout, Activity, Leaderboard
from .serializers import (
    TeamSerializer,
    UserSerializer,
    WorkoutSerializer,
    ActivitySerializer,
    LeaderboardSerializer
)


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workouts
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for activities
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for leaderboard
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
