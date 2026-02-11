from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB directly using pymongo
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        
        # Delete existing data
        self.stdout.write('Clearing existing data...')
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        
        # Create unique index on email field
        self.stdout.write('Creating unique index on email field...')
        db.users.create_index([("email", 1)], unique=True)
        
        # Insert Teams
        self.stdout.write('Populating teams...')
        teams_data = [
            {
                "_id": "team_marvel",
                "name": "Team Marvel",
                "description": "Earth's Mightiest Heroes",
                "created_at": datetime.now().isoformat(),
                "member_count": 0
            },
            {
                "_id": "team_dc",
                "name": "Team DC",
                "description": "Justice League United",
                "created_at": datetime.now().isoformat(),
                "member_count": 0
            }
        ]
        db.teams.insert_many(teams_data)
        
        # Insert Users
        self.stdout.write('Populating users...')
        users_data = [
            # Team Marvel
            {
                "_id": "user_ironman",
                "username": "ironman",
                "email": "tony.stark@avengers.com",
                "full_name": "Tony Stark",
                "team_id": "team_marvel",
                "avatar": "🦾",
                "created_at": datetime.now().isoformat(),
                "total_points": 0
            },
            {
                "_id": "user_spiderman",
                "username": "spiderman",
                "email": "peter.parker@avengers.com",
                "full_name": "Peter Parker",
                "team_id": "team_marvel",
                "avatar": "🕷️",
                "created_at": datetime.now().isoformat(),
                "total_points": 0
            },
            {
                "_id": "user_hulk",
                "username": "hulk",
                "email": "bruce.banner@avengers.com",
                "full_name": "Bruce Banner",
                "team_id": "team_marvel",
                "avatar": "💪",
                "created_at": datetime.now().isoformat(),
                "total_points": 0
            },
            {
                "_id": "user_blackwidow",
                "username": "blackwidow",
                "email": "natasha.romanoff@avengers.com",
                "full_name": "Natasha Romanoff",
                "team_id": "team_marvel",
                "avatar": "🕸️",
                "created_at": datetime.now().isoformat(),
                "total_points": 0
            },
            {
                "_id": "user_thor",
                "username": "thor",
                "email": "thor.odinson@avengers.com",
                "full_name": "Thor Odinson",
                "team_id": "team_marvel",
                "avatar": "⚡",
                "created_at": datetime.now().isoformat(),
                "total_points": 0
            },
            # Team DC
            {
                "_id": "user_superman",
                "username": "superman",
                "email": "clark.kent@justiceleague.com",
                "full_name": "Clark Kent",
                "team_id": "team_dc",
                "avatar": "🦸",
                "created_at": datetime.now().isoformat(),
                "total_points": 0
            },
            {
                "_id": "user_batman",
                "username": "batman",
                "email": "bruce.wayne@justiceleague.com",
                "full_name": "Bruce Wayne",
                "team_id": "team_dc",
                "avatar": "🦇",
                "created_at": datetime.now().isoformat(),
                "total_points": 0
            },
            {
                "_id": "user_wonderwoman",
                "username": "wonderwoman",
                "email": "diana.prince@justiceleague.com",
                "full_name": "Diana Prince",
                "team_id": "team_dc",
                "avatar": "👸",
                "created_at": datetime.now().isoformat(),
                "total_points": 0
            },
            {
                "_id": "user_flash",
                "username": "flash",
                "email": "barry.allen@justiceleague.com",
                "full_name": "Barry Allen",
                "team_id": "team_dc",
                "avatar": "⚡",
                "created_at": datetime.now().isoformat(),
                "total_points": 0
            },
            {
                "_id": "user_aquaman",
                "username": "aquaman",
                "email": "arthur.curry@justiceleague.com",
                "full_name": "Arthur Curry",
                "team_id": "team_dc",
                "avatar": "🔱",
                "created_at": datetime.now().isoformat(),
                "total_points": 0
            }
        ]
        db.users.insert_many(users_data)
        
        # Update team member counts
        db.teams.update_one({"_id": "team_marvel"}, {"$set": {"member_count": 5}})
        db.teams.update_one({"_id": "team_dc"}, {"$set": {"member_count": 5}})
        
        # Insert Workouts
        self.stdout.write('Populating workouts...')
        workouts_data = [
            {
                "_id": "workout_running",
                "name": "Running",
                "description": "Cardio running exercise",
                "category": "cardio",
                "points_per_unit": 10,
                "unit": "km"
            },
            {
                "_id": "workout_cycling",
                "name": "Cycling",
                "description": "Cycling exercise",
                "category": "cardio",
                "points_per_unit": 8,
                "unit": "km"
            },
            {
                "_id": "workout_swimming",
                "name": "Swimming",
                "description": "Swimming exercise",
                "category": "cardio",
                "points_per_unit": 15,
                "unit": "km"
            },
            {
                "_id": "workout_weightlifting",
                "name": "Weight Lifting",
                "description": "Strength training with weights",
                "category": "strength",
                "points_per_unit": 5,
                "unit": "reps"
            },
            {
                "_id": "workout_yoga",
                "name": "Yoga",
                "description": "Flexibility and mindfulness",
                "category": "flexibility",
                "points_per_unit": 12,
                "unit": "minutes"
            },
            {
                "_id": "workout_pushups",
                "name": "Push-ups",
                "description": "Upper body strength",
                "category": "strength",
                "points_per_unit": 2,
                "unit": "reps"
            }
        ]
        db.workouts.insert_many(workouts_data)
        
        # Insert Activities
        self.stdout.write('Populating activities...')
        activities_data = []
        user_ids = [u["_id"] for u in users_data]
        workout_ids = [w["_id"] for w in workouts_data]
        
        activity_id = 1
        for _ in range(50):  # Create 50 random activities
            user_id = random.choice(user_ids)
            workout = random.choice(workouts_data)
            
            if workout["unit"] == "km":
                amount = round(random.uniform(1, 15), 2)
            elif workout["unit"] == "minutes":
                amount = random.randint(15, 90)
            else:  # reps
                amount = random.randint(10, 100)
            
            points = int(amount * workout["points_per_unit"])
            
            # Random date within last 30 days
            days_ago = random.randint(0, 30)
            activity_date = datetime.now() - timedelta(days=days_ago)
            
            activities_data.append({
                "_id": f"activity_{activity_id}",
                "user_id": user_id,
                "workout_id": workout["_id"],
                "workout_name": workout["name"],
                "amount": amount,
                "unit": workout["unit"],
                "points": points,
                "date": activity_date.isoformat(),
                "created_at": activity_date.isoformat()
            })
            activity_id += 1
        
        db.activities.insert_many(activities_data)
        
        # Calculate and update user total points
        self.stdout.write('Calculating user points...')
        for user in users_data:
            user_activities = db.activities.find({"user_id": user["_id"]})
            total_points = sum(activity["points"] for activity in user_activities)
            db.users.update_one(
                {"_id": user["_id"]},
                {"$set": {"total_points": total_points}}
            )
        
        # Insert Leaderboard (top performers)
        self.stdout.write('Populating leaderboard...')
        leaderboard_data = []
        
        # Get all users with their updated points
        all_users = list(db.users.find())
        all_users.sort(key=lambda x: x["total_points"], reverse=True)
        
        for rank, user in enumerate(all_users, 1):
            leaderboard_data.append({
                "_id": f"leaderboard_{user['_id']}",
                "user_id": user["_id"],
                "username": user["username"],
                "full_name": user["full_name"],
                "team_id": user["team_id"],
                "total_points": user["total_points"],
                "rank": rank,
                "updated_at": datetime.now().isoformat()
            })
        
        db.leaderboard.insert_many(leaderboard_data)
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams: {db.teams.count_documents({})}')
        self.stdout.write(f'Users: {db.users.count_documents({})}')
        self.stdout.write(f'Workouts: {db.workouts.count_documents({})}')
        self.stdout.write(f'Activities: {db.activities.count_documents({})}')
        self.stdout.write(f'Leaderboard entries: {db.leaderboard.count_documents({})}')
        self.stdout.write(self.style.SUCCESS('Database successfully populated with superhero test data!'))
