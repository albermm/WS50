from django.shortcuts import render, redirect
from django import forms

from . import util


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
