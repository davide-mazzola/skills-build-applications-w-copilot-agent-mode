from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data safely
        for model in [User, Team, Activity, Leaderboard, Workout]:
            model.objects.all().delete()

        # Create teams
        Team.objects.create(name='Marvel')
        Team.objects.create(name='DC')

        # Create users
        User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel')
        User.objects.create(name='Captain America', email='cap@marvel.com', team='Marvel')
        User.objects.create(name='Batman', email='batman@dc.com', team='DC')
        User.objects.create(name='Superman', email='superman@dc.com', team='DC')

        # Create activities
        Activity.objects.create(user='Iron Man', type='Run', duration=30)
        Activity.objects.create(user='Captain America', type='Swim', duration=45)
        Activity.objects.create(user='Batman', type='Bike', duration=60)
        Activity.objects.create(user='Superman', type='Run', duration=50)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
        Workout.objects.create(name='Strength Training', description='Strength for all heroes')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)


    def handle(self, *args, **options):
        # Delete existing data safely
        for model in [User, Team, Activity, Leaderboard, Workout]:
            model.objects.all().delete()

        # Create teams
        Team.objects.create(name='Marvel')
        Team.objects.create(name='DC')

        # Create users
        User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel')
        User.objects.create(name='Captain America', email='cap@marvel.com', team='Marvel')
        User.objects.create(name='Batman', email='batman@dc.com', team='DC')
        User.objects.create(name='Superman', email='superman@dc.com', team='DC')

        # Create activities
        Activity.objects.create(user='Iron Man', type='Run', duration=30)
        Activity.objects.create(user='Captain America', type='Swim', duration=45)
        Activity.objects.create(user='Batman', type='Bike', duration=60)
        Activity.objects.create(user='Superman', type='Run', duration=50)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
        Workout.objects.create(name='Strength Training', description='Strength for all heroes')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Ensure unique index on email field for users
        from django.db import connection
        db = connection.cursor().db_conn.client['octofit_db']
        db['octofit_tracker_user'].create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
