from django import forms
from .models import GenreType, Album, Review

class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'

