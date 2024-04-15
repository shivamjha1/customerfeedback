from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
#from .models import Review
from django.views import View
# def review(request):
#     if request.method=='POST':
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             # x=form.cleaned_data
#             # rev=Review(user_name=x['user_name'],review_text=x['review_text'],rating=x['rating'])
#             # rev.save()
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#     else:
#         form=ReviewForm()
#     return render(request,"review/review.html",{
#         "form":form
#     })


#Class Based View
class ReviewView(View):
    def get(self,request):
        form=ReviewForm()
        return render(request,"review/review.html",{
        "form":form
    })
    def post(self,request):
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request,"review/review.html",{
        "form":form
    })

def thank_you(request):
    return render(request,"review/thank-you.html")