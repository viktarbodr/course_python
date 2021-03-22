from django.shortcuts import render
from django.views.generic import RedirectView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import models as auth_models
from cart import models
from homebook import models as home_models

from cart import utils


# Create your views here.
class AddToCartView(DetailView):
    model = models.Cart
    template_name = 'cart/add-book.html'
    def get_object(self, *args, **kwargs):  
        book_id = self.request.GET.get('book') 
        if not book_id:
            current_cart_pk = self.request.session.get('current_cart_pk')
            if current_cart_pk:
                current_cart = models.Cart.objects.filter(pk=current_cart_pk).first()
                return current_cart or []
            return []    
        else:
            current_cart_pk = self.request.session.get('current_cart_pk') 
            current_customer = self.request.user
            if current_customer.is_anonymous: 
                current_customer = None
            current_cart, cart_created = models.Cart.objects.get_or_create( 
                pk= current_cart_pk,
                defaults={'customer': current_customer}
            )
            if cart_created:
                self.request.session['current_cart_pk'] = current_cart.pk
            book = home_models.Book.objects.get(pk=book_id)   
            book_in_cart, book_created = models.CartProduct.objects.get_or_create(
                cart = current_cart,
                book = book,
                defaults={'quantity': 1, 'price': book.price})
            if not cart_created:
                book_in_cart.quantity += 1
                book_in_cart.save()
        return current_cart

class UpdateCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        current_cart_pk, cart_items_from_form = utils.harvest_data(self)
        if not current_cart_pk:
            return reverse("cart:add-to-cart")
        action = utils.update_items_in_cart(cart_items_from_form, current_cart_pk)   
        return reverse("cart:add-to-cart")

