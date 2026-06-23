from django.shortcuts import get_object_or_404, render
from manage_books.models import Book, Author, Publisher, Series, Note

def index(request):
    books = Book.objects.all()
    return render(request, 'manage_books/index.html.jinja', {'books': books})

def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'manage_books/book.html.jinja', {'book': book})

def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'manage_books/author.html.jinja', {'author': author})

def publisher(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    return render(request, 'manage_books/publisher.html.jinja', {'publisher': publisher})

def series(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    return render(request, 'manage_books/series.html.jinja', {'series': series})

def note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'manage_books/note.html.jinja', {'note': note})

def authors(request):
    authors = Author.objects.all()
    return render(request, 'manage_books/authors.html.jinja', {'authors': authors})

def publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'manage_books/publishers.html.jinja', {'publishers': publishers})

def series_list(request):
    series = Series.objects.all()
    return render(request, 'manage_books/series_list.html.jinja', {'series': series})

def notes(request):
    notes = Note.objects.all()
    return render(request, 'manage_books/notes.html.jinja', {'notes': notes})
