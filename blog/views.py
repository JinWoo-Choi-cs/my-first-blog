from django.shortcuts import render
from django.utils import timezone
from .models import Post
# . (dot)은 현재 디렉토리 혹은 어플을 의미한다.


#* Create your views here.

#** 템플릿 파일에서 아래 return 값을 활용한다.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # return : {}내부에 keys(문자열) : values(값) 으로 매개변수 넘겨줌
    return render(request, 'blog/post_list.html', {'Posts' : posts})


#
#*
#**
#!
#?
#region-s
#region-e
#todo
# //param

