# Generated by Django 4.0.10 on 2023-12-24 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_bloguser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='matricNumber',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
