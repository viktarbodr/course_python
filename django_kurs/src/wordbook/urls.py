from django.urls import path
from . import views


app_name = 'wordbook'

urlpatterns = [
    path('authors-list/', views.AuthorsList.as_view(), name='authors-list'),
    path('authors-create/', views.AuthorsCreate.as_view(), name='authors-create'),
    path('authors-detail/<int:pk>/', views.AuthorsDetail.as_view(), name='authors-detail'),
    path('authors-delete/<int:pk>/', views.AuthorsDelete.as_view(), name='authors-delete'),
    path('authors-update/<int:pk>/', views.AuthorsUpdate.as_view(),name='authors-update'),

    path('genres-list/', views.GenresList.as_view(), name='genres-list'),
    path('genres-create/', views.GenresCreate.as_view(), name='genres-create'),
    path('genres-detail/<int:pk>/', views.GenresDetail.as_view(), name='genres-detail'),
    path('genres-delete/<int:pk>/', views.GenresDelete.as_view(), name='genres-delete'),
    path('genres-update/<int:pk>/', views.GenresUpdate.as_view(),name='genres-update'),

    path('series-list/', views.SeriesList.as_view(), name='series-list'),
    path('series-create/', views.SeriesCreate.as_view(), name='series-create'),
    path('series-detail/<int:pk>/', views.SeriesDetail.as_view(), name='series-detail'),
    path('series-delete/<int:pk>/', views.SeriesDelete.as_view(), name='series-delete'),
    path('series-update/<int:pk>/', views.SeriesUpdate.as_view(),name='series-update'),

    path('publishers-list/', views.PublishersList.as_view(), name='publishers-list'),
    path('publishers-create/', views.PublishersCreate.as_view(), name='publishers-create'),
    path('publishers-detail/<int:pk>/', views.PublishersDetail.as_view(), name='publishers-detail'),
    path('publishers-delete/<int:pk>/', views.PublishersDelete.as_view(), name='publishers-delete'),
    path('publishers-update/<int:pk>/', views.PublishersUpdate.as_view(),name='publishers-update'),
]