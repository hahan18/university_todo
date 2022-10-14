# Generated by Django 4.1.1 on 2022-10-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_todo', '0005_schedule_link2'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('last_changes', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]