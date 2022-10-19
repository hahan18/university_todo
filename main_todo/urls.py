from django.urls import path
from .views import Todo, update, up_down, LoginUser, logout_user, chinese_phrase

urlpatterns = [
    path('', Todo.as_view(), name='todo'),
    path('update/<int:day_number>/<int:number_of_lesson>/', update, name='update'),
    path('updown/', up_down, name='updown'),
    path('chinese_phrase/', chinese_phrase, name='chinese_phrase'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]
