from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from wordbook.models import Author
f_aut = Author.objects.first

def home_page(request):
    context = {'f_aut': f_aut}
    return render(request, template_name = 'home.html', context=context)