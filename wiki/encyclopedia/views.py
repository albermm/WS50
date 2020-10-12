from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from . import util

class NewSearchForm(forms.Form):
    query = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))    

class NewPageForm(forms.Form):
    title = forms.CharField(label= 'Title')
    textarea = forms.CharField(help_text= ' write encyclopedia content', widget=forms.Textarea(attrs={"cols": 5,"rows":10}))
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit'))


class NewEntryForm(forms.Form):
    textarea = forms.CharField()
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit'))

   
  
 
# Create your views here.


def index(request):
    
    if "page" not in request.session:
        request.session["page"] = []
        return render(request, "encyclopedia/index.html", {
            "page": request.session["page"]
        })
          
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
            return render(request, "encyclopedia/title.html", {"title":title, "content":content}) 
    

def search(request, query):
    lista = util.list_entries()
    result = next((s for s in lista if query in s)) 
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
                print("lo guardo")
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
    page = request.POST.get('edition')
    
    content = util.get_entry(page)
    print(f"titulo is {page} and content is {content}")
    #form = NewEntryForm()
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['textarea']
            page = request.session["page"]
            print(page)
            util.save_entry(page, content)
            print("lo guardo")
            return render(request, "encyclopedia/title.html", {"title":page, "content":content}) 
        else:
            form = NewEntryForm()
            return render(request, "encyclopedia/edit.html", {
                "form": form
            })
    else:
        return render(request, "encyclopedia/edit.html", {
            "form": NewEntryForm()
        })
   
            #page = form.save()#(commit=False)
            #page = form.cleaned_data["page"]
            #request.session["pages"] += [page]
            #page.save() 
            #return redirect('page_detail', id=page.id)
            #return HttpResponseRedirect(reverse("wiki:index"))
    
