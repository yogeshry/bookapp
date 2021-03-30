from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('book/view/<str:pk>', views.BookDetail.as_view(), name='book_view'),
    path('book/new', views.BookCreate.as_view(), name='book_new'),
    path('book/edit/<str:pk>', views.BookUpdate.as_view(), name='book_edit'),
    path('delete/<str:pk>', views.BookDelete.as_view(), name='book_delete'),
    path('author', views.AuthorList.as_view(), name='author_list'),
    path('author/view/<str:pk>', views.AuthorDetail.as_view(), name='author_view'),
    path('author/new', views.AuthorCreate.as_view(), name='author_new'),
    path('author/edit/<str:pk>', views.AuthorUpdate.as_view(), name='author_edit'),
    path('author/delete/<str:pk>', views.AuthorDelete.as_view(), name='author_delete'),
    path('customer', views.CustomerList.as_view(), name='customer_list'),
    path('customer/view/<str:pk>', views.CustomerDetail.as_view(), name='customer_view'),
    path('customer/new', views.CustomerCreate.as_view(), name='customer_new'),
    path('customer/edit/<str:pk>', views.CustomerUpdate.as_view(), name='customer_edit'),
    path('customer/delete/<str:pk>', views.CustomerDelete.as_view(), name='customer_delete'),
    path('sale', views.SaleList.as_view(), name='sale_list'),
    path('sale/view/<int:pk>', views.SaleDetail.as_view(), name='sale_view'),
    path('sale/new', views.SaleCreate.as_view(), name='sale_new'),
    path('sale/edit/<int:pk>', views.SaleUpdate.as_view(), name='sale_edit'),
    path('sale/delete/<int:pk>', views.SaleDelete.as_view(), name='sale_delete'),
    path('publication', views.PublicationList.as_view(), name='publication_list'),
    path('publication/view/<str:pk>', views.PublicationDetail.as_view(), name='publication_view'),
    path('publication/new', views.PublicationCreate.as_view(), name='publication_new'),
    path('publication/edit/<str:pk>', views.PublicationUpdate.as_view(), name='publication_edit'),
    path('publication/delete/<str:pk>', views.PublicationDelete.as_view(), name='publication_delete'),
]