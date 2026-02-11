from djongo import models


class Team(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.CharField(max_length=100)
    member_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class User(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200)
    team_id = models.CharField(max_length=100)
    avatar = models.CharField(max_length=10)
    created_at = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Workout(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    points_per_unit = models.IntegerField()
    unit = models.CharField(max_length=20)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    user_id = models.CharField(max_length=100)
    workout_id = models.CharField(max_length=100)
    workout_name = models.CharField(max_length=100)
    amount = models.FloatField()
    unit = models.CharField(max_length=20)
    points = models.IntegerField()
    date = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.workout_name} - {self.amount} {self.unit}"


class Leaderboard(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    user_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    team_id = models.CharField(max_length=100)
    total_points = models.IntegerField()
    rank = models.IntegerField()
    updated_at = models.CharField(max_length=100)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']

    def __str__(self):
        return f"{self.rank}. {self.username} - {self.total_points} points"
