# Generated by Django 4.1.1 on 2022-10-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_todo', '0004_alter_schedule_first_name_alter_schedule_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='link2',
            field=models.URLField(blank=True, null=True, verbose_name='Посилання в зум'),
        ),
    ]
