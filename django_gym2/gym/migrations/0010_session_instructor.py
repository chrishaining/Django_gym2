# Generated by Django 3.0 on 2020-01-26 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0009_instructor_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='instructor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gym.Instructor'),
        ),
    ]