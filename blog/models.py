from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):   #models.Model은 DB에 저장되어야 하는 객체임을 알려준다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


'''

class PostWithReply(models.Model):
    index = models.index()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    reply = models.Reply()

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  # ! 포매팅해서 반환
        _str = StringIO()   
        _str.write("Index = ")
        _str.write(str(self.index))
        _str.write(" / title = ")
        _str.write(self.title)
        
        return _str.getvalue()

class Reply(models.Model):
    post_index = models.ForeignKey(models.PostWithReply.index, on_delete=models.CASCADE)  # 답변을 단 Post의 인덱스 CASCADE부분 모르겠네
    index = models.index()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        _str = StringIO()   
        _str.write("Post's Index = ")
        _str.write(str(self.post_index))
        _str.write("/ Reply's Index = ")
        _str.write(str(self.index))
        _str.write(" / title = ")
        _str.write(self.title)
        
        return _str.getvalue()

'''