from django.shortcuts import render
def index(request):
    content = {
        "data":"hola"
    }
    return render(request, "index_tem/index.html", content)