from django.db import models
import datetime
# Create your models here.
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))
   
class Publisher(models.Model):
    name = models.CharField('Name', max_length=30, primary_key=True)
    city = models.CharField('City', max_length=30)
    country = models.CharField('Country', max_length=30)
    president = models.CharField('President', max_length=30)
    yearFounded = models.IntegerField('Year', choices=YEAR_CHOICES)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
 
    def get_absolute_url(self):
        return reverse('publisher_edit', kwargs={'pk': self.pk})

          
class Author(models.Model):
    authorNumber = models.CharField('Author Number', max_length=30, primary_key=True)
    name = models.CharField('Name', max_length=30)
    bornYear = models.IntegerField('Born Year', choices=YEAR_CHOICES)
    diedYear = models.IntegerField('Died Year', choices=YEAR_CHOICES, null=True, blank=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('author_edit', kwargs={'pk': self.pk})
               
class Book(models.Model):
    bookNumber = models.CharField('Book Number', max_length=30, primary_key=True)
    name = models.CharField('Name', max_length=50)
    publicationYear = models.IntegerField('Publication Year', choices=YEAR_CHOICES)
    pages = models.IntegerField('Pages')
    publication = models.ForeignKey(to=Publisher,on_delete=models.CASCADE,null=False,blank=False)
    author =     models.ManyToManyField(Author)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})   
 
     
class Customer(models.Model):
    customerNumber = models.CharField('Customer Number', max_length=30, primary_key=True)
    name = models.CharField('Name', max_length=30)
    street = models.CharField('Street', max_length=30)
    city = models.CharField('City', max_length=30)
    state = models.CharField('State', max_length=30)
    country = models.CharField('Country', max_length=30)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('customer_edit', kwargs={'pk': self.pk})  

     
class Sale(models.Model):
    customer = models.ForeignKey(to=Customer,on_delete=models.CASCADE,null=False,blank=False)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE,null=False,blank=False)
    date = models.DateField('Date')
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    quantity = models.PositiveIntegerField('Quantity')

    class Meta:
        ordering = ['date']
        unique_together = (("customer", "book"),)

    def __str__(self):
        return str(self.id)
        
    def get_absolute_url(self):
        return reverse('sale_edit', kwargs={'pk': self.pk}) 