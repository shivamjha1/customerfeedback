from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import FileForm
# Create your views here.
def store_file(file):
    with open("temp/image.jpg","wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        form=FileForm()
        return render(request, "profiles/create_profile.html",{
            "form":form
        })

    def post(self, request):
        form=FileForm(request.POST,request.FILES)
        if form.is_valid():
            store_file(form['file'])
            return HttpResponseRedirect("/profiles")
        return render(request, "profiles/create_profile.html",{
            "form":form
        })