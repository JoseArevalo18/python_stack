from django.shortcuts import render, HttpResponse
from .models import Book, Author


def index(request):
    if request.method == "POST":
        Book.objects.create(title=request.POST['titulo'],desc=request.POST['descripcion'])
        all_books = Book.objects.all()
        return render(request,'index.html', {'all':all_books})
    all_books = Book.objects.all()
    return render(request,'index.html', {'all':all_books})

def book(request,number):
    if request.method == "POST":
        new_author = Author.objects.get(id=request.POST['auth_select'])
        sel_book = Book.objects.get(id=number)
        sel_book.authors.add(new_author)
        sel_authors = Author.objects.filter(book=sel_book)
        not_authors = Author.objects.exclude(book=sel_book)
        all_authors = Author.objects.all()
        context = {
            'selbook':sel_book,
            'selauthor':sel_authors,
            'allauthors': all_authors,
            'notauthors': not_authors
            }
        return render(request,'books.html', context)
    sel_book = Book.objects.get(id=number)
    sel_authors = Author.objects.filter(book=sel_book)
    not_authors = Author.objects.exclude(book=sel_book)
    all_authors = Author.objects.all()
    context = {
            'selbook':sel_book,
            'selauthor':sel_authors,
            'allauthors': all_authors,
            'notauthors': not_authors
            }
    return render(request,'books.html', context)

def authorIndex(request):
    if request.method == "POST":
        Author.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],notes=request.POST['notes'])
        all_authors = Author.objects.all()
        return render(request,'authors_index.html', {'all':all_authors})
    all_authors = Author.objects.all()
    return render(request,'authors_index.html', {'all':all_authors})

def author(request,number):
    if request.method == "POST":
        new_book = Book.objects.get(id=request.POST['auth_select'])
        sel_author = Author.objects.get(id=number)
        sel_author.book.add(new_book)
        sel_books = Book.objects.filter(authors=sel_author)
        not_books = Book.objects.exclude(authors=sel_author)
        all_books = Book.objects.all()
        context = {
            'selauthor':sel_author,
            'selbook':sel_books,
            'allbooks': all_books,
            'notbooks': not_books
            }
        return render(request,'authors.html', context)
    sel_author = Author.objects.get(id=number)
    sel_books = Book.objects.filter(authors=sel_author)
    not_books = Book.objects.exclude(authors=sel_author)
    all_books = Book.objects.all()
    context = {
            'selauthor':sel_author,
            'selbook':sel_books,
            'allbooks': all_books,
            'notbooks': not_books
            }
    return render(request,'authors.html', context)