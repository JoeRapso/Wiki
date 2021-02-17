import markdown2, re
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
            "name": name.capitalize # test this further, test "ht", "cs" variations
        })
    except: 
        return HttpResponse('404 File not found', status=404)
def search(request):
    if request.method == "POST":
        q = request.POST.get('q')
        matches = [i for i in util.list_entries() if q[0].upper() in i] # test querry case sensitivity further, before final version
        return render(request, "encyclopedia/search.html", {"matching_list": matches})

