# Generated by Django 5.1.6 on 2025-02-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feeds", "0006_followmanage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, upload_to="post_images/"),
        ),
    ]
