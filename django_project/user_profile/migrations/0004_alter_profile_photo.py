# Generated by Django 3.2.3 on 2021-05-27 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_order_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='олень.jpg', upload_to=''),
        ),
    ]
