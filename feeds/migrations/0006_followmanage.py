# Generated by Django 5.1.6 on 2025-02-18 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feeds", "0005_alter_post_no_of_likes"),
    ]

    operations = [
        migrations.CreateModel(
            name="FollowManage",
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
                ("follower", models.CharField(max_length=100)),
                ("user", models.CharField(max_length=100)),
            ],
        ),
    ]
