from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate, login, views
from django.contrib.auth import models as auth_models
from django.contrib.auth import forms as auth_forms
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm

from accounts import forms, urls, models
# Create your views here.


#def login_views(request):
#    template_name = "accounts/login.html"
##    if request.method == "GET":
#        login_form = forms.LoginForm()
#        return render(
#            request,
#            template_name=template_name,
#            context={"form": login_form }
#            )
#    elif request.method == "POST":
#        login_form = forms.LoginForm(request.POST)
#        if login_form.is_valid():
#            username = login_form.username
#            password = login_form.password
#            user = authenticate(request, username=username, password=password)
#            if user is not None:
#                login(request, user)
#                return HttpResponseRedirect(reverse('authors-list'))
#            else:
#                return render(
#                request,
#                template_name=template_name, 
#                context={"form": login_form })
        # chec and login
#        else:
#            return render(
#                request,
#                template_name=template_name, 
#                context={"form": login_form })

class RegistrationView(CreateView):
    model = models.User
    form_class = auth_forms.UserCreationForm
    template_name = 'accounts/create_user.html'
    success_url = reverse_lazy('accounts:profile')
    
    def get_success_url(self, *args, **kwargs):
        usernamme = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(self.request, username=username, password=password)
        user.save()
        if user is None:
            login(self.request, user)
        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")

        return str(self.success_url)

class UserLoginView(views.LoginView):
    template_name='accounts/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()

        if url in ['/accounts/login/', '', None]:
            url = reverse_lazy('homepage')
        return url


class UserLogoutView(views.LogoutView):
    next_page = reverse_lazy('homepage')    




class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = auth_models.User
    form_class = forms.RegistrationForm
    template_name = 'accounts/update_user.html'
    success_url = reverse_lazy('accounts:profile')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        user_data, created = models.Customer.objects.get_or_create(pk=self.request.user.pk)
        user_data.save()
        context['form_ext'] = forms.RegistrationForm(instance=user_data)
        return context

    def form_valid(self, form):
        self.object = form.save()
        object_ext = models.Customer.objects.get(pk=self.request.user.pk)
        form_ext = forms.ProfileForm(self.request.POST, instance=object_ext)

        if form_ext.is_valid():
            object_ext = form_ext.save()

        return super().form_valid(form)

    def get_object(self, **kwargs):
        return self.request.user