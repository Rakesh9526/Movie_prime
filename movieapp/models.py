from django.db import models
from django.urls import reverse

app_name='movieapp'
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='movie_categories', blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('movieapp:movie_list_by_category', args=[self.slug])


    def __str__(self):
        return "{}".format(self.name)

class Movielist(models.Model):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    desc = models.TextField()
    year = models.IntegerField()
    starring = models.CharField(max_length=250,blank=True,null=True)
    rating = models.DecimalField(max_digits=10,decimal_places=2,default=True)
    youtube_link = models.URLField(max_length=300,blank=True,null=True)
    image = models.ImageField(upload_to='movie_img')
    director = models.CharField(max_length=200, blank=True, null=True)
    producer = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    run_time = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)
        verbose_name='movie'
        verbose_name_plural='movies'

    def get_url(self):
        return reverse('movieapp:moviedetails', args=[self.category.slug, self.slug])

    def __str__(self):
        return "{}".format(self.name)

class Review(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    e_mail = models.EmailField(max_length=250)
    ph_no = models.IntegerField()
    comments = models.TextField()
    movie = models.ForeignKey(Movielist, on_delete=models.CASCADE,default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"Review by {self.name if self.name else 'Anonymous'} for {self.movie.name}"