# Generated by Django 5.1.1 on 2024-09-16 23:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0003_alter_member_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
