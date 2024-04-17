from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
#using view to make everything predeifned
from django.views.generic.edit import CreateView
from .forms import FileForm

from .models import Files
# Create your views here.
# def store_file(file):
#     with open("temp/image.jpg","wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


class CreateProfileView(CreateView):
    template_name="profiles/create_profile.html"
    model=Files
    fields="__all__"
    success_url="/profiles"



# class CreateProfileView(View):
#     def get(self, request):
#         form=FileForm()
#         return render(request, "profiles/create_profile.html",{
#             "form":form
#         })

#     def post(self, request):
#         form=FileForm(request.POST,request.FILES)
#         if form.is_valid():
#             profile=Files(image=request.FILES['file'])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
#         return render(request, "profiles/create_profile.html",{
#             "form":form
#         })