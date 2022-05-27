from django.shortcuts import render

from django.shortcuts import render
from .models import Book

def index(request):
    booklist = Book.objects.all()
    return render(request,'base.html',{'booklist':booklist})

def search(request):
    name = request.GET.get('name')
    return render(request,'search.html',{'name':name})