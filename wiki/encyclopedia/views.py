from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

from . import util

class NewSearchForm(forms.Form):
    query = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))    


# Create your views here.
'''
def index(request):
    if request.method == "POST":
        form = NewSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            return title(request, query)
        else:
            return render(request, "encyclopedia/index.html", {
                "form" : form
            })
           
    
    return render(request, "encyclopedia/index.html", {
             "entries": util.list_entries(),
             "form" : NewSearchForm(auto_id=False)
    })
'''



def index(request):
    query = request.GET.get('q')
    if query:
        content = util.get_entry(query)
        return render(request, "encyclopedia/title.html", {"title":query, "content":content})   
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })    



def title(request, title):
    query = request.GET.get('q')
    if query:
        content = util.get_entry(query)
        return render(request, "encyclopedia/title.html", {"title":query, "content":content})   
    else:  
        content = util.get_entry(title)
        if util.get_entry(title) == None:
            return render(request, "encyclopedia/error.html")
        else:   
            return render(request, "encyclopedia/title.html", {"title":title, "content":content}) 


