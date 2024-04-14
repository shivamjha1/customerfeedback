from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm

def review(request):
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/thank-you')
    else:
        form=ReviewForm()
    return render(request,"review/review.html",{
        "form":form
    })

def thank_you(request):
    return render(request,"review/thank-you.html")