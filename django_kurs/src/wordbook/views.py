from django.shortcuts import render
from django.http import HttpResponseRedirect
from .import models 
from .import forms
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView


wordbooks = ['Authors', 'Genres', 'Series','Publishers']

#def word_book(request):
#    return render(request, template_name='main_wordbook.html', context={'wordbook': wordbooks})



class AuthorsList(ListView):
    model = models.Authors
    template_name = 'wordbook/authors_list.html'
   # def get_context_data(self, **kwargs):
   #     context = super().get_context_data(**kwargs)
   #     context["page_title"] = "Author's !!!"
        # context["object_list"] -имя для контекста -object_list
    #    return context

class GenresList(ListView):
    model = models.Genres
    template_name = 'wordbook/genres_list.html'
    

class SeriesList(ListView):
    model = models.Series
    template_name = 'wordbook/series_list.html'


class PublishersList(ListView):
    model = models.Publishers
    template_name = 'wordbook/publishers_list.html'




class AuthorsDetail(DetailView):
    model = models.Authors
    # context["object"] - стандартное имя для контекста -object (будет объект)
class GenresDetail(DetailView):
    model = models.Genres

class SeriesDetail(DetailView):
    model = models.Series

class PublishersDetail(DetailView):
    model = models.Publishers
    




class AuthorsCreate(CreateView):
    model = models.Authors
    #fields = ['name', 'description']
    form_class = forms.AuthorForm
    success_url = reverse_lazy('authors-list')
    # в Create  объекта не будет для контекста/
    #  потому как в шаблоне мы показываем форму. обьекта еще нет! 

class GenresCreate(CreateView):
    model = models.Genres
    form_class = forms.GenreForm
    success_url = reverse_lazy('genres-list')

class SeriesCreate(CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    success_url = reverse_lazy('series-list')

class PublishersCreate(CreateView):
    model = models.Authors
    form_class = forms.PublisherForm
    success_url = reverse_lazy('publishers-list')




class AuthorsDelete(DeleteView):
    model = models.Authors
    success_url = reverse_lazy('authors-list')
    template_name = 'wordbook/authors_confirm_delete.html'

    # context["object"] - стандартное имя для контекста -object 
#def author_create(request):
#    context = {}
#    if request.method == "POST":
#        form = forms.AuthorForm(request.POST)
#        if form.is_valid():
#            author = form.save()
#            return HttpResponseRedirect(reverse('authors-detail', kwargs={'pk' :author.pk}))
#         else:
#            context['form'] = form
#    else:
#         context['form'] = forms.AuthorsForm()
#    return render(request, template_name="create.html", context=context)
class GenresDelete(DeleteView):
    model = models.Genres
    success_url = reverse_lazy('genres-list')
    template_name = 'wordbook/genres_confirm_delete.html'

class SeriesDelete(DeleteView):
    model = models.Series
    success_url = reverse_lazy('series-list')
    template_name = 'wordbook/series_confirm_delete.html'


class PublishersDelete(DeleteView):
    model = models.Publishers
    success_url = reverse_lazy('publishers-list')
    template_name = 'wordbook/publishers_confirm_delete.html'





class AuthorsUpdate(UpdateView):
    model = models.Authors
    #fields = ['name', 'description']
    form_class = forms.AuthorForm
    #template_name = 'create.html'
    success_url = reverse_lazy('authors-list')
  #      def form_valid(self, form):
  #          Post.objects.create(Authorform.cleaned_data)
  #          return redirect(self.get_success_url())
class GenresUpdate(UpdateView):
    model = models.Genres
    form_class = forms.GenreForm
    success_url = reverse_lazy('genres-list')

class SeriesUpdate(UpdateView):
    model = models.Series
    form_class = forms.SeriesForm
    success_url = reverse_lazy('series-list')

class PublishersUpdate(UpdateView):
    model = models.Publishers
    form_class = forms.PublisherForm
    success_url = reverse_lazy('publishers-list')