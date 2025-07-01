from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CBVModel
from .forms import CBVForm

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
