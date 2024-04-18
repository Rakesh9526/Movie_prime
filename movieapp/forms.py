from django import forms
from .models import Review, Movielist, Category

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'e_mail', 'ph_no', 'comments', 'movie', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the movie and category fields
        self.fields['movie'].queryset = Movielist.objects.all()  # You can customize this queryset as needed
        self.fields['category'].queryset = Category.objects.all()  # You can customize this queryset as needed
