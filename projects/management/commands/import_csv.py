import csv
import os
from random import randint

from django.conf import settings
from django.contrib.auth.hashers import make_password

from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime

from projects.models import Project, Task
from users.models import User


class Command(BaseCommand):
    help = "Import data from CSV file"

    def handle(self, *args, **options):
        user_csv: str = os.path.join(settings.BASE_DIR, "data_csv", "Task Manager - Users_Projects_Tasks - Users.csv")
        task_csv: str = os.path.join(settings.BASE_DIR, "data_csv", "Task Manager - Users_Projects_Tasks - Tasks.csv")
        project_csv: str = os.path.join(settings.BASE_DIR, "data_csv",
                                        "Task Manager - Users_Projects_Tasks - Projects.csv")
        num_projects: int = 0

        with open(project_csv, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                num_projects += 1
                row.pop('id')
                Project.objects.update_or_create(**row)

        with open(user_csv, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row.pop('id')
                row["password"] = make_password(row["password"])
                User.objects.update_or_create(**row)

        with open(task_csv, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["created_at"] = parse_datetime(row["created_at"])
                row.pop('id')
                Task.objects.update_or_create(**row, project=Project.objects.get(id=randint(1, num_projects)))
