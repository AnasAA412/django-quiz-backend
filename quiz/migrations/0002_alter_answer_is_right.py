# Generated by Django 4.1.7 on 2023-03-07 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='is_right',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
