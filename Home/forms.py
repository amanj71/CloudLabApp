from django import forms

## write form classes here
class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=180, widget=forms.TextInput(attrs={
        "classs": "form-control", "placeholder": "Your Full Name",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "classs": "form-control", "placeholder": "emailadress@example.com",
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        "classs": "form-control", "placeholder": "Please add your content here",
    }))
