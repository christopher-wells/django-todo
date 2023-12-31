# Generated by Django 4.2.7 on 2023-11-08 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                ("task_name", models.CharField(max_length=255)),
                ("task_complete", models.BooleanField(default=False)),
                ("date_task_added", models.DateTimeField(auto_now_add=True)),
                ("date_task_completed", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["date_task_added"],
            },
        ),
    ]
