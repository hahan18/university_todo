import string

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView
from .models import Schedule, MainData
from .forms import ScheduleUpdateForm, LoginUserForm


class Todo(ListView):
    model = Schedule
    template_name = 'main_todo/todo.html'
    context_object_name = 'Schedule'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        sch = self.model.objects

        context_dict = {
            'first_lesson': sch.filter(up_or_down_week='1', number_of_lesson='1'),
            'second_lesson': sch.filter(up_or_down_week='1', number_of_lesson='2'),
            'third_lesson': sch.filter(up_or_down_week='1', number_of_lesson='3'),
            'fourth_lesson': sch.filter(up_or_down_week='1', number_of_lesson='4'),
            'first_lesson2': sch.filter(up_or_down_week='2', number_of_lesson='1'),
            'second_lesson2': sch.filter(up_or_down_week='2', number_of_lesson='2'),
            'third_lesson2': sch.filter(up_or_down_week='2', number_of_lesson='3'),
            'fourth_lesson2': sch.filter(up_or_down_week='2', number_of_lesson='4'),
            'date_now': timezone.now().strftime('%A %d.%m'),
            'current_week': MainData.objects.get(pk=1).up_or_down_week,
            'current_day': timezone.now().isoweekday(),
            'title': 'Розклад',
        }
        context.update(context_dict)

        return context


@login_required(login_url='login/')
def update(request, day_number, number_of_lesson):
    schedule = get_object_or_404(Schedule, day_number=day_number, number_of_lesson=number_of_lesson)
    form = ScheduleUpdateForm(instance=schedule)

    if request.method == 'POST':
        form = ScheduleUpdateForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('/')

    last_changes = schedule.last_changes

    day = ''.join([el for el in schedule.get_day_number_display() if el not in string.digits])
    week = schedule.get_up_or_down_week_display()
    lesson = schedule.get_number_of_lesson_display()

    context = {'form': form,
               'last_changes': last_changes,
               'date_now': timezone.now().strftime('%a %d.%m'),
               'current_week': MainData.objects.get(pk=1).up_or_down_week,
               'title': 'Змінити запис',
               'day': day,
               'week': week,
               'lesson': lesson,
               }
    return render(request, 'main_todo/update.html', context)


@login_required(login_url='login/')
def up_down(request):
    obj = MainData.objects.get(pk=1)
    if obj.up_or_down_week == '1':
        obj.up_or_down_week = '2'
    else:
        obj.up_or_down_week = '1'
    obj.save()
    return redirect(request.META['HTTP_REFERER'])


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main_todo/login.html'

    def get_success_url(self):
        return reverse_lazy('todo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = timezone.now().strftime('%a %d.%m')
        context['current_week'] = MainData.objects.get(pk=1).up_or_down_week
        context['title'] = 'Увійти'
        return context


def logout_user(request):
    logout(request)
    return redirect('login_user')
