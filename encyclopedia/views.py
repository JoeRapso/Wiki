import markdown2
from django.shortcuts import render, HttpResponse
from django import forms

from . import util

class SearchForm(forms.Form):
    q = forms.CharField(label="New Task")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm()
    })
def entry(request, name):
    try:
        return render(request, "encyclopedia/entrypage.html", {
            "content": markdown2.markdown(util.get_entry(name)),
            "name": name.capitalize
        })
    except: 
        return HttpResponse('404 File not found', status=404)
def search(request):
    return render(request, "encyclopedia/search.html")

    if request.method == "POST":
        q = q(request.POST)
        q.append(q)
