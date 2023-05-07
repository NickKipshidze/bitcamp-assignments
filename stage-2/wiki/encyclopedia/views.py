from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from random import choice
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, page):
    page_markdown = util.get_entry(page)

    if page_markdown == None:
        page_markdown, page = "# Page not found", "Not found"

    page_html = markdown2.markdown(page_markdown)

    return render(request, "encyclopedia/page.html", {
        "title": page,
        "entry": page_html
    })

def random(request):
    return page(
        request, 
        choice(util.list_entries())
    )

def search(request):
    query = request.GET["q"]

    results = [entry for entry in util.list_entries() if query.lower() in entry.lower()]

    return render(request, "encyclopedia/results.html", {
        "entries": results
    })

def editor(request, title):
    if "title" and "content" in request.GET:
        return save(request)
    
    if title in util.list_entries():
        return render(request, "encyclopedia/editor.html", {
            "title": title,
            "content": util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/editor.html", {
            "title": "New",
            "content": "# My page"
        })

def save(request: WSGIRequest):
    title = request.GET["title"]
    content = request.GET["content"]

    if request.path.split("/")[-1] in util.list_entries():
        util.save_entry(title, content)
        return page(request, title)
    elif title in util.list_entries():
        return HttpResponse(f"Error: Entry \"{title}\" already exsists")
    else:
        util.save_entry(title, content)
        return page(request, title)