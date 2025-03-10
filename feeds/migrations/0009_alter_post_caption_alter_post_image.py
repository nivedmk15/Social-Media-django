# Generated by Django 5.1.6 on 2025-02-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feeds", "0008_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="caption",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(default=None, upload_to="post_images/"),
            preserve_default=False,
        ),
    ]
