from django.db import models


class Schedule(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Прізвище")
    subject = models.CharField(max_length=100, null=True, blank=True, verbose_name="Предмет")
    link = models.URLField(null=True, blank=True, verbose_name='Посилання1')
    link2 = models.URLField(null=True, blank=True, verbose_name='Посилання2')

    class UpOrDownWeek(models.TextChoices):
        UP = '1', 'ВЕРХНІЙ',
        DOWN = '2', 'НИЖНІЙ',

    up_or_down_week = models.CharField(
        max_length=10,
        choices=UpOrDownWeek.choices,
        verbose_name='Верхній чи нижній тиждень',
        default=UpOrDownWeek.UP
    )

    class DayNumber(models.TextChoices):
        MN_F = '1', 'ПОНЕДІЛОК1'
        TU_F = '2', 'ВІВТОРОК1'
        WD_F = '3', 'СЕРЕДА1'
        TH_F = '4', 'ЧЕТВЕР1'
        FR_F = '5', "П'ЯТНИЦЯ1"
        MN_S = '6', 'ПОНЕДІЛОК2'
        TU_S = '7', 'ВІВТОРОК2'
        WD_S = '8', 'СЕРЕДА2'
        TH_S = '9', 'ЧЕТВЕР2'
        FR_S = '10', "П'ЯТНИЦЯ2"

    day_number = models.CharField(
        max_length=10,
        choices=DayNumber.choices,
        verbose_name='День',
        default=DayNumber.MN_F
    )

    class NumberOfLesson(models.TextChoices):
        FIRST = '1', 'ПЕРША ПАРА'
        SECOND = '2', 'ДРУГА ПАРА'
        THIRD = '3', 'ТРЕТЯ ПАРА'
        FOURTH = '4', 'ЧЕТВЕРТА ПАРА'

    number_of_lesson = models.CharField(
        max_length=10,
        choices=NumberOfLesson.choices,
        verbose_name='Пара',
        default=NumberOfLesson.FIRST
    )

    last_changes = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject + ' ' + self.day_number + self.number_of_lesson

    class Meta:
        ordering = ['day_number', 'number_of_lesson']


class MainData(models.Model):
    class UpOrDownWeek(models.TextChoices):
        UP = '1', 'ВЕРХНІЙ',
        DOWN = '2', 'НИЖНІЙ',

    up_or_down_week = models.CharField(
        max_length=10,
        choices=UpOrDownWeek.choices,
        verbose_name='Верхній чи нижній тиждень',
        default=UpOrDownWeek.UP
    )


