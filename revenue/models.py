from django.db import models

# Create your models here.

class Incoming(models.Model):
    product_name = models.CharField(max_length=200)
    money_spent = models.PositiveIntegerField()
    reason = models.TextField()
    product_image= models.ImageField(upload_to="images")
    def __str__(self):
        self.product_name
class Outgoing(models.Model):
    product_name = models.CharField(max_length=200)
    money_spent = models.PositiveIntegerField()
    reason = models.TextField()
    product_image =models.ImageField(upload_to="images")
    def __str__(self):
        self.product_name
