# Generated by Django 3.2.3 on 2021-06-03 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_profile_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status_char',
            new_name='status',
        ),
    ]
