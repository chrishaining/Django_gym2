# Generated by Django 3.0 on 2020-01-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_member_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='goal',
            field=models.CharField(default='General fitness', max_length=255),
        ),
    ]