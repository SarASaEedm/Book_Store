from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse

from bookindex.forms import BookForm, BookModelForm
##
from bookindex.models import Book

import json

books = [
    {"id": 1, "title": "book1", "author": "Ahmed", "no": 594, "pic": "pic1.png", "price": 342},
    {"id": 2, "title": "book2", "author": "Bob", "no": 432, "pic": "pic2.png", "price": 432},
    {"id": 3, "title": "book3", "author": "Alice", "no": 343, "pic": "pic3.png", "price": 943},
    {"id": 4, "title": "book4", "author": "Bob", "no": 479, "pic": "pic4.png", "price": 855},
    {"id": 5, "title": "book5", "author": "Alice", "no": 234, "pic": "pic5.png", "price": 856},
]

def books_list(request):
    return HttpResponse(books)


def books_info(request, id):
    print(f"id={id}", type(id))
    all_books = [book for book in books if book["id"] == id]
    if all_books:
        book = all_books[0]
        return render(request, "bookindex/book_details.html", {"title": book["title"], "book": book})
    return HttpResponse("Book not found")

def books_landing(request):
    return render(request, "bookindex/index.html",
                  context = {"title":"book1", "books":books})


###############lab2

def index(request):
    books = Book.objects.all()
    return render(request, "bookindex/index2.html", context = {'books':books})

def show(request, id):
    #book = Book.objects.get(id=id)
    book = get_object_or_404(Book, pk=id)
    return render(request, "bookindex/show.html", context = {'book':book})

def delete(request, id):
    #book = Book.objects.get(id=id)
    book = get_object_or_404(Book, pk=id)
    book.delete()
    url = reverse("books_index")
    return redirect(url)

def create(request):
    print(request)
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(cleaned_data)
            book = Book(**cleaned_data)
            book.save()
            url = reverse("books_index")
            return redirect(url)
    return render(request,
                  'bookindex/create.html'
                ,context={'form':form})



def create_std_modelform(request):
    form = BookModelForm()
    if request.POST:
        print(request.POST)
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            url = reverse("books_index")
            return redirect(url)


    return render(request, 'bookindex/create_m_f.html',
                  context={'form':form})




def edit(request, id):
    book = get_object_or_404(Book, pk=id)
    form = BookModelForm(instance=book)
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES,instance=book)
        if form.is_valid():
            book=form.save()
            url = reverse("books_index")  # accept urlname
            return redirect(url)


    return render(request, 'bookindex/edit.html',
                  {'form': form})