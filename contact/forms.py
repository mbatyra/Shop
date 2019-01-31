from django import forms

class conatactForm(forms.Form):
    Imie_i_Nazwisko = forms.CharField(required=False, max_length=100, help_text='100 znakow max.')
    email = forms.EmailField(required=True)
    Wiadomosc = forms.CharField(required=True, widget=forms.Textarea)