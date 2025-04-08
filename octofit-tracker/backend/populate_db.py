import os
import django
import random
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

def populate_users():
    users = [
        {"username": "john_doe", "email": "john@example.com", "password": "password123"},
        {"username": "jane_smith", "email": "jane@example.com", "password": "password123"},
        {"username": "alice_wonder", "email": "alice@example.com", "password": "password123"},
    ]
    for user_data in users:
        User.objects.get_or_create(**user_data)

def populate_teams():
    users = list(User.objects.all())
    teams = [
        {"name": "Team Alpha", "members": random.sample(users, min(len(users), 2))},
        {"name": "Team Beta", "members": random.sample(users, min(len(users), 2))},
    ]
    for team_data in teams:
        team, created = Team.objects.get_or_create(name=team_data["name"])
        if created:
            team.members.add(*team_data["members"])
            team.save()

def populate_workouts():
    workouts = [
        {"name": "Push-ups", "description": "Do 20 push-ups"},
        {"name": "Running", "description": "Run for 30 minutes"},
        {"name": "Cycling", "description": "Cycle for 10 kilometers"},
    ]
    for workout_data in workouts:
        Workout.objects.get_or_create(**workout_data)

def populate_activities():
    users = list(User.objects.all())
    activities = [
        {"user": random.choice(users), "activity_type": "Running", "duration": timedelta(minutes=30)},
        {"user": random.choice(users), "activity_type": "Cycling", "duration": timedelta(minutes=45)},
    ]
    for activity_data in activities:
        Activity.objects.get_or_create(**activity_data)

def populate_leaderboard():
    users = list(User.objects.all())
    leaderboard_entries = [
        {"user": user, "score": random.randint(50, 150)} for user in users
    ]
    for entry_data in leaderboard_entries:
        Leaderboard.objects.get_or_create(**entry_data)

def populate_database():
    populate_users()
    populate_teams()
    populate_workouts()
    populate_activities()
    populate_leaderboard()

if __name__ == "__main__":
    populate_database()
    print("Database populated with test data.")
