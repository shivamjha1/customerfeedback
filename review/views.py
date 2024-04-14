from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm

def review(request):
    if request.method=='POST':
        return HttpResponseRedirect('/thank-you')
    form=ReviewForm()
    return render(request,"review/review.html",{
        "form":form
    })

def thank_you(request):
    return render(request,"review/thank-you.html")