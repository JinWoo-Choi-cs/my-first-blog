from django.urls import path
from . import views

# path의 name 부분은 템플릿에서 a href 링크에 {% url 'post_edit' %} 여기에서 설정한 값과 매칭되어야한다

# {% url 'post_edit' pk=post.pk %} 이 부분에서 pk=post.pk 는 
# path에서 <int:pk> 부분에 들어가게된다.

# e.g.) <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pkArg>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

