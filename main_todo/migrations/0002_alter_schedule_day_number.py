# Generated by Django 4.1.1 on 2022-10-06 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day_number',
            field=models.CharField(choices=[('1', 'ПОНЕДІЛОК1'), ('2', 'ВІВТОРОК1'), ('3', 'СЕРЕДА1'), ('4', 'ЧЕТВЕР1'), ('5', "П'ЯТНИЦЯ1"), ('6', 'ПОНЕДІЛОК2'), ('7', 'ВІВТОРОК2'), ('8', 'СЕРЕДА2'), ('9', 'ЧЕТВЕР2'), ('10', "П'ЯТНИЦЯ2")], default='1', max_length=10, verbose_name='День'),
        ),
    ]
