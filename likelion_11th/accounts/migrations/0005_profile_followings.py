# Generated by Django 4.2.2 on 2023-06-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_is_activate'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to='accounts.profile'),
        ),
    ]