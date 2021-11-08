from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, placeholder="Imię")
    email = forms.EmailField(required=True, placeholder="Email")
    phone = forms.IntegerField(required=True,placeholder="Numer Telefonu")
    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        placeholder="Wiadomość"
    )