from django import forms
from .models import Reservation


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
        fields = '__all__'
