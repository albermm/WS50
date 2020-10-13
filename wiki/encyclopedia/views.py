from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import random
import markdown2
from markdown2 import Markdown

from . import util

class NewSearchForm(forms.Form):
    query = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))    

class NewPageForm(forms.Form):
    title = forms.CharField(label= 'Title')
    textarea = forms.CharField(label= 'Add Description', help_text= ' write encyclopedia content', widget=forms.Textarea(attrs={"cols": 5,"rows":10}))
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit'))


class NewEntryForm(forms.Form):
    textarea = forms.CharField(label= 'Add Changes', initial='', widget=forms.Textarea(attrs={"cols": 5,"rows":10}))
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit'))


# Create your views here.


def index(request):
    query = request.GET.get('q')
    if query:
        title, content, result = search(request, query)['query'], search(request, query)['content'], search(request, query)['result']        
        return render(request, "encyclopedia/title.html", {"title":title, "content":content, "result":result}) 
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })    



def title(request, title):
    query = request.GET.get('q')
    if query:
        title, content, result = search(request, query)['query'], search(request, query)['content'], search(request, query)['result']        
        return render(request, "encyclopedia/title.html", {"title":title, "content":content, "result":result}) 
    else:  
        content = util.get_entry(title)
        if util.get_entry(title) == None:
            return render(request, "encyclopedia/error.html")
        else:   
            markdowner = Markdown()  
            body = markdowner.convert(content)  
            request.session['page'] = title
            page = request.session['page']
            return render(request, "encyclopedia/title.html", {
                "title":title, "body":body
            }) 
    

def search(request, query):
    lista = util.list_entries()
    result = []
    result = [i for i in lista if query.lower() in i.lower()]
    print(f"resultados son {result}") 
    content = util.get_entry(query)
    if query in lista:
        resultado = {"query": query, "content":content, "result":""}
        return resultado
    elif result:
        resultado = {"query": "", "content":"", "result":result}
        print ("resultado: ", result)
        return resultado


def add(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['textarea']
            exist = util.get_entry(title)
            print(f"exist {exist} y titulo {title}")
            if exist == None:
                util.save_entry(title, content)
                print("anadido, lo guardo")
                return render(request, "encyclopedia/title.html", {"title":title, "content":content}) 
            else:
                print("Existe ya")
                return render(request, "encyclopedia/error.html")
          
        else:
            form = NewPageForm()
            return render(request, "encyclopedia/add.html", {
                "form": form
            })
    return render(request, "encyclopedia/add.html", {
        "form": NewPageForm()
    })
   

def edit(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['textarea']
            page = request.session['page']
            print(f"edition se llama {content} and page is {page}")
            util.save_entry(page, content)
            print("lo guardo")
            return render(request, "encyclopedia/title.html", {"title":page, "content":content}) 
        else:
            form = NewEntryForm()
            return render(request, "encyclopedia/edit.html", {
                "form": form
            })
    else:
        page = request.session['page']
        content = util.get_entry(page)
        print(f"aqui llego {page}, el contenido es {content}")
        form = NewEntryForm(initial={'textarea':content})
        return render(request, "encyclopedia/edit.html", {
            "form": form
        })
   
    
def randpage(request):
    query = request.GET.get('q')
    if query:
        title, content, result = search(request, query)['query'], search(request, query)['content'], search(request, query)['result']        
        return render(request, "encyclopedia/title.html", {"title":title, "content":content, "result":result}) 
    else:
        return render(request, "encyclopedia/randpage.html", {
            "entry": random.choice(util.list_entries())
        })