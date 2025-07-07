from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CBVModel
from .forms import CBVForm,BookForm
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
    paginate_by = 10
    order_by = '-published_date'  # Order by published date in descending order


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(status='draft')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'List of Drafted Books'
        context['total_books'] = Book.objects.count()
        return context
    
    def get_paginate_by(self, queryset=None):
        pages = super().get_paginate_by( queryset)
        total_pages = queryset.count()
        if total_pages < 10:
            return 4
        return 5
    

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'status', 'published_date']
    template_name = 'classbasedviews/book_form.html'
    success_url = reverse_lazy('book_list')

    def get_initial(self):
        return {
            'title': 'Default Title',
            'author': 'Default Author',
            'description': 'Default Description',
            'status': Book.DRAFT,
        }
    
from django.core.exceptions import PermissionDenied
def get_object(self, queryset = None):
    obj = super().get_object(queryset)
    if obj.created_by!= self.request.user:
        raise PermissionDenied('You do not have permmisions')
        
    return obj