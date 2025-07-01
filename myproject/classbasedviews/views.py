from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CBVModel
from .forms import CBVForm
from django.core.paginator import Paginator
from .models import Book

class CBVListView(ListView):
    model = CBVModel
    template_name = 'classbasedviews/cbv_list.html'
    context_object_name = 'cbvs'

class CBVDetailView(DetailView):
    model = CBVModel
    template_name = 'classbasedviews/cbv_detail.html'
    context_object_name = 'cbv'

class CBVCreateView(CreateView):
    model = CBVModel
    form_class = CBVForm
    template_name = 'classbasedviews/cbv_form.html'
    success_url = reverse_lazy('cbv_list')

class CBVUpdateView(UpdateView):
    model = CBVModel
    form_class = CBVForm
    template_name = 'classbasedviews/cbv_form.html'
    success_url = reverse_lazy('cbv_list')

class CBVDeleteView(DeleteView):
    model = CBVModel
    template_name = 'classbasedviews/cbv_confirm_delete.html'
    success_url = reverse_lazy('cbv_list')

class BookListView(ListView):
    model = Book
    template_name = 'classbasedviews/book_list.html'
    context_object_name = 'books'
    paginate_by = 2
    order_by = '-published_date'  # Order by published date in descending order

# def book_list_view(request):
#     books = Book.objects.all().order_by('-published_date')
#     paginator = Paginator(books, 5)  # Show 5 books per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'classbasedviews/book_list.html', {'page_obj': page_obj})
