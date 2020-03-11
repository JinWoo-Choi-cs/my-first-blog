from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

#**작업 이후 새로운 페이지로 다시 전송시켜주기 위해 추가
from django.shortcuts import redirect



# . (dot)은 현재 디렉토리 혹은 어플을 의미한다.

#* 템플릿 파일에서 아래 return 값을 활용한다.
# return: {}내부에 keys(문자열) : values(값) 으로 매개변수 넘겨줌

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts' : posts})
    

# ** pkArg로 바꿔도 된다! 대신 view.py, post_list.html, url.py 다 고쳐야함
# ** redirect 하는곳에서 (post_edit.html)도 매개변수 명 맞춰줘야함
def post_detail(request, pkArg):
    post = get_object_or_404(Post, pk=pkArg)
    return render(request, 'blog/post_detail.html', {'post' : post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid() :
            #form.save로 바로 저장 해도 되지만
            #다른 설정을 추가하기 위해서 commit=False를 추가해서 잠시 멈추고
            #다른 설정을 한 뒤 save(commit)를 진행한다
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":

        # PostForm에 instance로 객체를 넘기면 해당 객체를 수정 가능
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pkArg=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})