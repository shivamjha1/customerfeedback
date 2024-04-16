from typing import Any
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
from .models import Review
#from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
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


class Thank_youView(TemplateView):
    template_name="review/thank-you.html"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
class Review_list(TemplateView):
    template_name="review/review_list.html"
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.all()
        return context
    
class Single_Review(TemplateView):
    template_name="review/single_review.html"
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        review_name=kwargs["id"]
        selected=Review.objects.get(id=review_name)
        context["review"]=selected
        return context
    