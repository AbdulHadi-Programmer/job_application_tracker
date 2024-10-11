from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from tracker.models import Add_Job

class Command(BaseCommand):
    help = 'Assigns all jobs to a default user if they have no user assigned'

    def handle(self, *args, **kwargs):
        # Get the user model
        User = get_user_model()

        # Set the default user to assign jobs to (e.g., 'admin')
        default_user = User.objects.get(username='admin')  # Replace 'admin' with the correct default username

        # Filter jobs with no user assigned (user is null)
        jobs_without_user = Add_Job.objects.filter(user__isnull=True)

        for job in jobs_without_user:
            job.user = default_user  # Assign the default user
            job.save()

        self.stdout.write(self.style.SUCCESS('Successfully assigned all jobs to the default user.'))
