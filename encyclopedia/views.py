import markdown2, random
from django.shortcuts import render, HttpResponse, redirect
from django.template.response import TemplateResponse
from django import forms

from . import util

# Returns a list of entry titles and displays it in index.html
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

# Renders the contents of an entry file into HTML
def entry(request, title):
    try:
        return render(request, "encyclopedia/entrypage.html", {
            "content": markdown2.markdown(util.get_entry(title)),
            "title": title
        })
    except:
        return render(request, "encyclopedia/error.html", {
            "status": "404 error - file not found. Please try a different wiki entry."
        }, status=404)

# Searches for an entry based on the users query
def search(request):
    if request.method == "POST":
        q = request.POST.get('q')
        q = q.lower()
        titles_list = util.list_entries()
        titles_list = [x.lower() for x in titles_list]
        if q in titles_list:
            return redirect('entry', q)
        matches = [i for i in util.list_entries() if q[0].upper() in i]
        return render(request, "encyclopedia/search.html", {"matching_list": matches})

# Renders the newpage.html
def createPage(request):

    return render(request, "encyclopedia/newpage.html")

# Grabs relevant variables from a form and creates a new wiki entry
def createdPage(request):
    if request.method == "POST":
        title = request.POST.get('title')
        title_lower = title.lower()
        titles_list = util.list_entries()
        titles_list = [x.lower() for x in titles_list]
        if title_lower in titles_list:
            return render(request, "encyclopedia/error.html", {
            "status": "403 forbidden error - file with same title already exists. Please type a different title."
        }, status=403)
        content = request.POST.get('content')
        title= title[:1].upper() + title[1:]
    util.save_entry(title, content)
    return redirect('entry', title)

# Grabs the content of an entry and displays it in the relevant HTML areas
def editPage(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        return render(request, "encyclopedia/editpage.html", {"title": title, "content": util.get_entry(title)})

# Allows for the contents of an entry to be changed/edited
def editedPage(request):

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        util.save_entry(title, content)
        return redirect('entry', title)

# Grabs an entry at random and displays it
def randomPage(request):
    randomTitle = random.choice(util.list_entries())
    return redirect('entry', randomTitle)




