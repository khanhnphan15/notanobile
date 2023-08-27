from django import forms
from .models import Meal


class MealForm(forms.ModelForm):
    image_file = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = Meal
        fields = ['name', 'description', 'price', 'people', 'preparation_time']
