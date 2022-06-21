from django.shortcuts import render,redirect
from django.utils import timezone
from  .models import Community,Comment
from django.views.generic import ListView
# Create your views here.
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse
#
def community(request):
    if request.method == "GET":
        content_list = Community.objects.order_by("create_date")
        comment_list = Comment.objects.order_by("create_date")
        return render(request,'community/community.html',{"content_list":content_list,"comment_list":comment_list})
    else:
        feed = Community(
            content=request.POST.get('content'),
            create_date=timezone.now(),
            author=request.user,
            # region=request.user,
            category=request.POST.get('category'))
        feed.save()
        return redirect("/community/")

def detail(request,content_id):
    content=Community.objects.get(id=content_id)
    if request.method == "GET":
        try:
            comment_list = Comment.objects.get(content=content_id)
            return render(request, "community/community_detail.html", {"content":content,"comment_list":comment_list})
        except:
            return render(request,"community/community_detail.html",{"content":content})
    else:
        comment = Comment(
            user = request.user,
            ceate_date = timezone.now(),
            content = content_id,
            comment = request.POST.get('comment'))
        comment.save()
        return render(request,"community/community_detail.html",{"content":content})