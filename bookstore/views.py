# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Author, Publisher, Book, Customer, Sale
from .forms import AuthorForm,PublisherForm,CustomerForm,SaleForm,BookForm
from django import forms
class PublisherList(ListView): 
    model = Publisher

class PublisherDetail(DetailView): 
    model = Publisher

class PublisherCreate(SuccessMessageMixin, CreateView): 
    model = Publisher
    form_class = PublisherForm
    success_url = reverse_lazy('publisher_list')
    success_message = "Publisher successfully created!"

class PublisherUpdate(SuccessMessageMixin, UpdateView): 
    model = Publisher
    form_class = PublisherForm
    success_url = reverse_lazy('publisher_list')
    success_message = "Publisher successfully updated!"

class PublisherDelete(SuccessMessageMixin, DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher_list')
    success_message = "Publisher successfully deleted!"

class BookList(ListView): 
    model = Book

class BookDetail(DetailView): 
    model = Book

class BookCreate(SuccessMessageMixin, CreateView): 
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')
    success_message = "Book successfully created!"

class BookUpdate(SuccessMessageMixin, UpdateView): 
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')
    success_message = "Book successfully updated!"

class BookDelete(SuccessMessageMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    success_message = "Book successfully deleted!"

class CustomerList(ListView): 
    model = Customer

class CustomerDetail(DetailView): 
    model = Customer

class CustomerCreate(SuccessMessageMixin, CreateView): 
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')
    success_message = "Customer successfully created!"

class CustomerUpdate(SuccessMessageMixin, UpdateView): 
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')
    success_message = "Customer successfully updated!"

class CustomerDelete(SuccessMessageMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')
    success_message = "Customer successfully deleted!"

class AuthorList(ListView): 
    model = Author

class AuthorDetail(DetailView): 
    model = Author

class AuthorCreate(SuccessMessageMixin, CreateView): 
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')
    success_message = "Author successfully created!"

class AuthorUpdate(SuccessMessageMixin, UpdateView): 
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')
    success_message = "Author successfully updated!"

class AuthorDelete(SuccessMessageMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')
    success_message = "Author successfully deleted!"


class SaleList(ListView): 
    model = Sale

class SaleDetail(DetailView): 
    model = Sale

class SaleCreate(SuccessMessageMixin, CreateView): 
    model = Sale
    form_class = SaleForm
    success_url = reverse_lazy('sale_list')
    success_message = "Sale successfully created!"

class SaleUpdate(SuccessMessageMixin, UpdateView): 
    model = Sale
    form_class = SaleForm
    success_url = reverse_lazy('sale_list')
    success_message = "Sale successfully updated!"

class SaleDelete(SuccessMessageMixin, DeleteView):
    model = Sale
    success_url = reverse_lazy('sale_list')
    success_message = "Sale successfully deleted!"