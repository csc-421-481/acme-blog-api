# Generated by Django 4.0.10 on 2023-12-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_bloguser_managers_alter_bloguser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
