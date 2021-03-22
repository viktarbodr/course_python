from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, RedirectView, UpdateView, ListView, CreateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, ImproperlyConfigured
from cart import models as cart_models
from orders.models import Orders
from homebook.models import Book
from . import forms

# Create your views here.

class OrdersList(LoginRequiredMixin, ListView):
    model = Orders
    template_name = 'orders/orders_list.html'
    login_url = '/accounts/login/'
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["сart"]= cart_models.CartProduct.objects.all()
        context["pk"]= self.request.session.get('cart')
        return context

    def get_queryset(self):
        q = self.request.GET.get('q') 
        qs = super().get_queryset()
        if q:
           qs = qs.filter(name__icontains=q)
        return qs

      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Book"
        field_to_sort_on = self.request.GET.get('field')
        direction_to_sort_on = self.request.GET.get('direction')
        q = self.request.GET.get('q') 
        context['search_form'] = forms.SearchForm(
            initial={
                'q': q,
                'field': field_to_sort_on,
                'direction': direction_to_sort_on, 
            })
        context['field_to_sort_on'] = field_to_sort_on
        context['direction_to_sort_on'] = direction_to_sort_on
        return context


class OrdersDetail(LoginRequiredMixin, DetailView):
    model=Orders
    login_url = '/accounts/login/'
       
    
class OrdersDelete(LoginRequiredMixin, DeleteView):
    success_url=reverse_lazy('orders:orders')
    model=Orders
    login_url = '/accounts/login/' 

class OrdersCreate(LoginRequiredMixin, CreateView):
    success_url=reverse_lazy('orders:information-orders')
    model = Orders
    fields=( 'first_name', 'last_name', 'address', 'phone', 'cart', 'purchase_type', 'comment') 
    login_url = '/accounts/login/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # cart_pk = self.request.session.get('cart')
        context["сart"]= cart_models.CartProduct.objects.all()
        # context["pk"]= self.request.session.get('cart')
        # context["cart_pk"]= Cart.objects.all()
        # self.cart.save()
        return context
    def total_book_price(self):
        all_book = self.book.all()
        total = 0
        for book in all_book:
            total += book.total_price
        return total
    
class OrdersUpdate(LoginRequiredMixin, UpdateView): 
    model=Orders
    success_url=reverse_lazy('orders:orders')
    fields=( 'first_name', 'last_name', 'address', 'phone', 'cart', 'purchase_type', 'comment') 
    login_url = '/accounts/login/'
    
