from django.shortcuts import redirect, render,get_object_or_404

from functionbasedviews.models import Book
from functionbasedviews.forms import BookForm

# Create your views here.

def book_lists(request):
    books = Book.objects.all()
    return render(request,'functionbasedviews/book_lists.html',{'books':books})

def book_detail(request,pk):
    book = get_object_or_404(Book,pk=pk)
    return render(request,'functionbasedviews/book_detail.html',{'book':book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lists')
    else:
        form = BookForm()
    return render(request,'functionbasedviews/book_create.html', {'form':form})


def book_update(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('lists')
    else:

        form = BookForm(instance=book)        
    return render(request,'functionbasedviews/book_update.html', {'form':form})


def book_delete(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('lists')
    return render(request, 'functionbasedviews/book_delete.html', {'book': book})
