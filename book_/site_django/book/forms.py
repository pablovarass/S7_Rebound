from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['titulo', 'autor', 'valoracion']
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el título del libro',
                    'maxlength': 150, 
                    'required': True
                }
            ),
            'autor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el autor del libro',
                    'maxlength': 150, 
                    'required': True
                }
            ),
            'valoracion': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la valoración del libro',
                    'min': 0,  # Valor mínimo
                    'max': 10000, 
                    'required': True
                }
            )
        }
