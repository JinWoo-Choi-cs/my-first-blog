encoding : utf-8
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render


# region-s Testing Done
#* 만들기
# Post.objects.create(author=User.objects.get(username='admin'), title='Created Testing', text="???")

#print ("------------- before -------------")
#print (Post.objects.all()) # user = admin

#print ("------------- after -------------")
# me = User.objects.get(username='admin')
# Post.objects.filter(author=me, title='Post').delete()
# print (Post.objects.filter(title__contains='Post'))
# Post.objects.filter(author=me, title__contains='Post').delete()
# Post.objects.create(author=me, title='Post made by run file', text='Testing')

#for a in Post.objects.all() :
#    print ("----------------" + a.title)

#* 5~10  번쨰까지만
# Post.objects.all()[5:10]     
#* ~ 5  번쨰까지만 
# Post.objects.all()[:5]      
#* ~10  번쨰까지 중에 2개당 1개씩  
# Post.objects.all()[:10:2]     

#* 하나 발행
#Post.objects.get(title="Created Testing").publish()

#* 전부 발행
#for a in Post.objects.all():
#    a.publish()

#* 현재보다 빨리 발행된것 찾기
#Post.objects.filter(published_date__lte=timezone.now())
#* 오름차순 정리
#Post.objects.order_by('created_date')
#* 내림차순 정리
#Post.objects.order_by('-created_date')
#* 더블 쿼리 (쿼리 연결 : chaining)
#Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
#Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')

# region-e Testing Done
print()

print (Post.objects.all()[0].pk)
print (Post.objects.all()[1].pk)

