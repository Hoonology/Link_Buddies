from django.shortcuts import render,redirect
from django.utils import timezone
from  .models import QnA
from django.views.generic import ListView

# Create your views here.
app_name = "qna"

# def list(request):
#     qna_list=QnA.objects.order_by("create_date")
#     return render(request,"qna/qna_list.html",{"qna_list":qna_list})

class qnalist(ListView):
    model = QnA

def detail(request,qna_id):
    qna = QnA.objects.get(id=qna_id)
    if request.method == "GET":
        return render(request,"qna/qna_detail.html",{"qna":qna})
    else:
        qna.answer = request.POST.get('answer')
        qna.save()
        return redirect("/qna")
def modify(request,qna_id):
    qna = QnA.objects.get(id=qna_id)
    if request.method == "GET":
        return render(request, "qna/qnaform.html", {"qna": qna})
    else :
        qna.title = request.POST.get('title')
        qna.question = request.POST.get('question')
        qna.secret = request.POST.get("secret_checked")
        qna.modified_date = timezone.now()
        qna.save()
        return redirect("/qna/detail/"+str(qna_id))

def create(request):
    if request.method == "POST":
        qna=QnA(title=request.POST.get('title'),
                question=request.POST.get('question'),
                create_date=timezone.now(),
                author=request.user,
                secret=request.POST.get("secret_checked"))
        qna.save()
        return redirect("/qna/")
    else:
        return render(request,'qna/qnaform.html')

def delete(request,qna_id):
    qna = QnA.objects.get(id=qna_id)
    qna.delete()
    return redirect("/qna")