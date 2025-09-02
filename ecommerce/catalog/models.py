from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits = 10 , # all the numbers combined ... 
        decimal_places = 2 # number of digits after the flaoting point
    )
    image = models.ImageField(
        upload_to='products/'
    )
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self): # for readabilty in the django admin
        return self.name



