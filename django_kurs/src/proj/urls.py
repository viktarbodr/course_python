"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wordbook import views as book_views
from wordbook import models

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_views.word_book, name='wordbook'),

    path('authors-list/', book_views.AuthorsList.as_view(), name='authors-list'),
    path('authors-create/', book_views.AuthorsCreate.as_view(), name='authors-create'),
    path('authors-detail/<int:pk>/', book_views.AuthorsDetail.as_view(), name='authors-detail'),
    path('authors-delete/<int:pk>/', book_views.AuthorsDelete.as_view(), name='authors-delete'),
    path('authors-update/<int:pk>/', book_views.AuthorsUpdate.as_view(),name='authors-update'),

    path('genres-list/', book_views.GenresList.as_view(), name='genres-list'),
    path('genres-create/', book_views.GenresCreate.as_view(), name='genres-create'),
    path('genres-detail/<int:pk>/', book_views.GenresDetail.as_view(), name='genres-detail'),
    path('genres-delete/<int:pk>/', book_views.GenresDelete.as_view(), name='genres-delete'),
    path('genres-update/<int:pk>/', book_views.GenresUpdate.as_view(),name='genres-update'),

    path('series-list/', book_views.SeriesList.as_view(), name='series-list'),
    path('series-create/', book_views.SeriesCreate.as_view(), name='series-create'),
    path('series-detail/<int:pk>/', book_views.SeriesDetail.as_view(), name='series-detail'),
    path('series-delete/<int:pk>/', book_views.SeriesDelete.as_view(), name='series-delete'),
    path('series-update/<int:pk>/', book_views.SeriesUpdate.as_view(),name='series-update'),

    path('publishers-list/', book_views.PublishersList.as_view(), name='publishers-list'),
    path('publishers-create/', book_views.PublishersCreate.as_view(), name='publishers-create'),
    path('publishers-detail/<int:pk>/', book_views.PublishersDetail.as_view(), name='publishers-detail'),
    path('publishers-delete/<int:pk>/', book_views.PublishersDelete.as_view(), name='publishers-delete'),
    path('publishers-update/<int:pk>/', book_views.PublishersUpdate.as_view(),name='publishers-update')
] 
