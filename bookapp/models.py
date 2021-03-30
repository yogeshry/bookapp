from django.db import models
import datetime
# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator


class Publication(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    foundedIn =models.PositiveIntegerField("Founded In",
            validators=[
                MinValueValidator(1200), 
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Use the following format: <YYYY>")
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    president = models.CharField( max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
 
    def get_absolute_url(self):
        return reverse('publication_edit', kwargs={'pk': self.pk})

          
class Author(models.Model):
    number = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    bornIn =models.PositiveIntegerField(
        "Born In",
            validators=[
                MinValueValidator(1200), 
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Use the following format: <YYYY>")
    diedIn = models.PositiveIntegerField(
        "Died In",
            validators=[
                MinValueValidator(1200), 
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Use the following format: <YYYY>", null=True, blank=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('author_edit', kwargs={'pk': self.pk})
               
class Book(models.Model):
    number = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    publishedIn =models.PositiveIntegerField(
        "Published In",
            validators=[
                MinValueValidator(1200), 
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Use the following format: <YYYY>")
    publication = models.ForeignKey(to=Publication,on_delete=models.CASCADE)
    author =     models.ManyToManyField(Author)
    pages = models.PositiveIntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})   
 
     
class Customer(models.Model):
    number = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=30)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('customer_edit', kwargs={'pk': self.pk})  

     
class Sale(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    date = models.DateField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ['date']
        unique_together = (("customer", "book"),)

    def __str__(self):
        return str(self.id)
        
    def get_absolute_url(self):
        return reverse('sale_edit', kwargs={'pk': self.pk}) 