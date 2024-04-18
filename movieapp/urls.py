from django.urls import path

from movieapp import views

app_name="movieapp"

urlpatterns = [
    path('',views.home,name='home'),
    path('category/<slug:category_slug>/', views.movie_list_by_category, name='movie_list_by_category'),
    path('category/<slug:category_slug>/<slug:movie_slug>/', views.moviedetails, name='moviedetails'),
    path('review/',views.movie_review,name='movie_review'),
    path('thanks/',views.thank_page,name='thank_page'),


]