# Generated by Django 5.1.6 on 2025-02-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feeds", "0003_alter_post_no_of_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="no_of_likes",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
