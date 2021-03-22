from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView

from homebook import models


# Create your views here.
class HomePage(ListView):
    paginate_by = 10
    model = models.Book
    ordering = ['pk']
    template_name = "homebook/homepage.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = self.model.objects.all().order_by('pk')
        context['objects'] = books
        return context

 
class BooksList(ListView):
    paginate_by = 5
    model = models.Book
    ordering = ['-pk']
    template_name = "homebook/books_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_books = self.model.objects.all().order_by('-pk')[:3]
        context['new_books'] = new_books
        return context