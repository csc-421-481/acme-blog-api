# Generated by Django 4.0.10 on 2023-12-27 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='label',
            new_name='name',
        ),
    ]
