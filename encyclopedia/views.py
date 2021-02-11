import markdown2
from django.shortcuts import render, HttpResponse
from django import forms

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
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
    if request.method == "POST":
        q = request.POST.get('q')
        q = q.upper()
    if q in util.list_entries():
        return render(request, "encyclopedia/search.html", {"q": q})

