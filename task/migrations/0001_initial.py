# Generated by Django 5.1.1 on 2024-09-20 17:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("description", models.CharField(max_length=1024)),
                ("due_date", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Not Started!", "ns"),
                            ("In Progress!", "wip"),
                            ("Completed!", "done"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[("Low", "0"), ("Medium", "1"), ("High", "2")],
                        max_length=32,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[("Personal", "personal"), ("Work", "work")],
                        max_length=32,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "task_item",
                "verbose_name_plural": "task_items",
                "db_table": "task_item",
            },
        ),
    ]
