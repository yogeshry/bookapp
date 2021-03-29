from django import forms

from .models import Book, Publisher, Author, Customer, Sale

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['bookNumber'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['publication'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['publicationYear'].widget.attrs = {
            'class': 'form-control col-md-6'
        } 
        self.fields['pages'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = Book
        fields = ('name', 'bookNumber', 'publication','publicationYear','pages','author')
        widgets = {
                    'author': forms.CheckboxSelectMultiple()
                }
class PublisherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PublisherForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['city'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['country'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['president'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['yearFounded'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
        }

    class Meta:
        model = Publisher
        fields = ('name', 'city', 'country','president','yearFounded')

class AuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['authorNumber'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['bornYear'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
        }        
        self.fields['diedYear'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'required': False,
        }

    class Meta:
        model = Author
        fields = ('authorNumber', 'name', 'bornYear','diedYear')

class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields['book'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['customer'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['date'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['price'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['quantity'].widget.attrs = {
            'class': 'form-control col-md-6',
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
        self.fields['customerNumber'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['street'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['city'].widget.attrs = {
            'class': 'form-control col-md-6'
        }        
        self.fields['state'].widget.attrs = {
            'class': 'form-control col-md-6'
        }        
        self.fields['country'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Customer
        fields = ('customerNumber', 'name', 'street','city','state','country')