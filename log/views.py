
# Create your views here.
# crear los metodos o funciones que permiten realizar las validaciones de parametros.
# from django.shortcuts import render, HttpResponse
from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("root")

def new(request):
    return HttpResponse("new")

def create(request):
    return redirect("/")

def show(request, _number):
    return HttpResponse(f"number:{_number}")

def edit(request, _number):
    return HttpResponse("edit")

def delete(request, _number):
    return redirect("/")

def json(request):
    data = {
        "title": "My first blog",
        "content": "Lorem, ipsum ........"
    }
    return JsonResponse(data, safe = False)