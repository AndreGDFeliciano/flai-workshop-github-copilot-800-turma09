from django.contrib import admin
from .models import Team, User, Workout, Activity, Leaderboard


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'description', 'member_count', 'created_at']
    search_fields = ['name', 'description']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['_id', 'username', 'email', 'full_name', 'team_id', 'total_points', 'created_at']
    search_fields = ['username', 'email', 'full_name']
    list_filter = ['team_id']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'category', 'points_per_unit', 'unit']
    search_fields = ['name', 'description']
    list_filter = ['category']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['_id', 'user_id', 'workout_name', 'amount', 'unit', 'points', 'date']
    search_fields = ['user_id', 'workout_name']
    list_filter = ['workout_name']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['rank', 'username', 'full_name', 'team_id', 'total_points', 'updated_at']
    search_fields = ['username', 'full_name']
    list_filter = ['team_id']
    ordering = ['rank']
