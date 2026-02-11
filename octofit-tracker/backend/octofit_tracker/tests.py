from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Team, User, Workout, Activity, Leaderboard


class TeamModelTest(TestCase):
    def setUp(self):
        Team.objects.create(
            _id='test_team',
            name='Test Team',
            description='A test team',
            created_at='2026-02-11',
            member_count=5
        )

    def test_team_creation(self):
        team = Team.objects.get(_id='test_team')
        self.assertEqual(team.name, 'Test Team')
        self.assertEqual(team.member_count, 5)

    def test_team_str(self):
        team = Team.objects.get(_id='test_team')
        self.assertEqual(str(team), 'Test Team')


class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(
            _id='test_user',
            username='testuser',
            email='test@example.com',
            full_name='Test User',
            team_id='test_team',
            avatar='🦸',
            created_at='2026-02-11',
            total_points=100
        )

    def test_user_creation(self):
        user = User.objects.get(_id='test_user')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.total_points, 100)

    def test_user_str(self):
        user = User.objects.get(_id='test_user')
        self.assertEqual(str(user), 'testuser')


class WorkoutModelTest(TestCase):
    def setUp(self):
        Workout.objects.create(
            _id='test_workout',
            name='Running',
            description='Cardio exercise',
            category='cardio',
            points_per_unit=10,
            unit='km'
        )

    def test_workout_creation(self):
        workout = Workout.objects.get(_id='test_workout')
        self.assertEqual(workout.name, 'Running')
        self.assertEqual(workout.points_per_unit, 10)

    def test_workout_str(self):
        workout = Workout.objects.get(_id='test_workout')
        self.assertEqual(str(workout), 'Running')


class ActivityModelTest(TestCase):
    def setUp(self):
        Activity.objects.create(
            _id='test_activity',
            user_id='test_user',
            workout_id='test_workout',
            workout_name='Running',
            amount=5.0,
            unit='km',
            points=50,
            date='2026-02-11',
            created_at='2026-02-11'
        )

    def test_activity_creation(self):
        activity = Activity.objects.get(_id='test_activity')
        self.assertEqual(activity.workout_name, 'Running')
        self.assertEqual(activity.points, 50)

    def test_activity_str(self):
        activity = Activity.objects.get(_id='test_activity')
        self.assertEqual(str(activity), 'Running - 5.0 km')


class LeaderboardModelTest(TestCase):
    def setUp(self):
        Leaderboard.objects.create(
            _id='test_leaderboard',
            user_id='test_user',
            username='testuser',
            full_name='Test User',
            team_id='test_team',
            total_points=100,
            rank=1,
            updated_at='2026-02-11'
        )

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.get(_id='test_leaderboard')
        self.assertEqual(leaderboard.username, 'testuser')
        self.assertEqual(leaderboard.rank, 1)

    def test_leaderboard_str(self):
        leaderboard = Leaderboard.objects.get(_id='test_leaderboard')
        self.assertEqual(str(leaderboard), '1. testuser - 100 points')


class TeamAPITest(APITestCase):
    def test_get_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserAPITest(APITestCase):
    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    def test_get_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(APITestCase):
    def test_get_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    def test_get_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class APIRootTest(APITestCase):
    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('teams', response.data)
        self.assertIn('users', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
