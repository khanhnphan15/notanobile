from django import forms
from .models import Reservation


class ReserveTableForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = Reservation
        fields = '__all__'
        exclude = ['user', 'name', 'email']
