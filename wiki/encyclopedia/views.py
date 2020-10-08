from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

from . import util

class NewTaskForm(forms.Form):
    task = forms.CharField(initial="Search Encyclopedia")


# Create your views here.

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/error.html")
    else:    
        return render(request, "encyclopedia/title.html", {"title":title, "content":content})





tasks = []

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("wiki:index"))
        else:
            return render(request, "encyclopedia/add.html", {
                "form" : form
            })

    return render(request, "encyclopedia/add.html", {
        "form" : NewTaskForm(auto_id=False)
    })




'''
class NewSearchForm(forms.Form):
    search = forms.CharField(label="New Search")
searches = []
def search(request):
    if request.method == "POST":
        form = NewSearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            searches.append(search)
            return HttpResponseRedirect(reverse("wiki:search"))
        else:
            return render(request, "wiki/index.html",{
                "form" : form
            })
    return render(request, "wiki/index.html", {
        "form" : NewSearchForm()
    })
    

'''