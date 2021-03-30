from django import forms
import datetime

from .models import Book, Publication, Author, Customer, Sale

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['number'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['publication'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['publishedIn'].widget.attrs = {
            'class': 'form-control col-sm-6'
        } 
        self.fields['pages'].widget.attrs = {
            'class': 'form-control col-sm-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = Book
        fields = ('name', 'number', 'publication','publishedIn','pages','author')

class PublicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PublicationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['city'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['country'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['president'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['foundedIn'].widget.attrs = {
            'class': 'form-control col-sm-6',
            'step': 'any',
        }

    class Meta:
        model = Publication
        fields = ('name', 'city', 'country','president','foundedIn')

class AuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['bornIn'].widget.attrs = {
            'class': 'form-control col-sm-6',
            'step': 'any',
        }        
        self.fields['diedIn'].widget.attrs = {
            'class': 'form-control col-sm-6',
            'step': 'any',
            'required': False,
        }

    class Meta:
        model = Author
        fields = ('number', 'name', 'bornIn','diedIn')

class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields['book'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['customer'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['date'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['price'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['quantity'].widget.attrs = {
            'class': 'form-control col-sm-6',
            'step': 'any',
        }
       
    
    class Meta:
        model = Sale
        fields = ('book', 'customer', 'date','price','quantity')    
        widgets = {
                'date': forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder':'Select a date', 'type':'date'}),
            }
class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['street'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }
        self.fields['city'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }        
        self.fields['state'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }        
        self.fields['country'].widget.attrs = {
            'class': 'form-control col-sm-6'
        }

    class Meta:
        model = Customer
        fields = ('number', 'name', 'street','city','state','country')