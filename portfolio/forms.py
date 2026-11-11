from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'name',
                'placeholder': 'Your Name *',
                'required': True,
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'placeholder': 'Your Email *',
                'required': True,
                'class': 'form-control',
            }),
            'phone': forms.TextInput(attrs={
                'id': 'phone',
                'placeholder': 'Your Phone',
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'id': 'message',
                'rows': 5,
                'placeholder': 'Your Message *',
                'required': True,
                'class': 'form-control',
            }),
        }
