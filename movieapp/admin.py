from django.contrib import admin
from .models import Category,Movielist,Review

# Register your models here.
admin.site.register(Category)


class movieadmin(admin.ModelAdmin):
    list_display =['name','slug','desc','year','language','category']
    prepopulated_fields = {'slug':('name',)}
    list_editable =['year','category','language']
admin.site.register(Movielist,movieadmin)

admin.site.register(Review)