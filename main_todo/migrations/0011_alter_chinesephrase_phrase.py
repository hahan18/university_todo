# Generated by Django 4.1.1 on 2022-10-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_todo', '0010_alter_chinesephrase_phrase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chinesephrase',
            name='phrase',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Фразочка'),
        ),
    ]