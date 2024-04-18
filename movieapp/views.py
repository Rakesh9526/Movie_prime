from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Movielist,Category,Review
from django.urls import reverse
from .forms import ReviewForm
from django.contrib import messages

# Create your views here.

def home(req):
    cat_movie=Category.objects.all()
    all_movies=Movielist.objects.all()
    return render(req,'index.html',{'cat_movie':cat_movie,'all_movies':all_movies})

def movie_list_by_category(request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    movies = Movielist.objects.filter(category=category)
    return render(request,'category_page.html', {'category': category, 'movies': movies})

def moviedetails(req,category_slug,movie_slug):
    movie_details = get_object_or_404(Movielist,slug=movie_slug)
    return render(req,'movie_details.html',{'movie_details': movie_details})


def movie_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            # Assuming you have a way to determine movie and category
            review.movie = Movielist.objects.first()  # You need to set the movie based on your logic
            review.category = Category.objects.first()  # You need to set the category based on your logic
            review.save()
            return redirect('moviedetails', category_slug=review.category.slug, movie_slug=review.movie.slug)
    else:
        form = ReviewForm()
    return render(request, 'index.html', {'form': form})

def thank_page(req):
    return render(req,'thankyou.html')