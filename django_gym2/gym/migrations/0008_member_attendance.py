# Generated by Django 3.0 on 2020-01-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_member_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='attendance',
            field=models.IntegerField(default=0),
        ),
    ]