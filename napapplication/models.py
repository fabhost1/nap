from django.db import models

# Create your models here.
class medical(models.Model):
    name=models.TextField(max_length=30)
    address=models.TextField(max_length=50)
    image=models.ImageField(blank=True)
    url=models.TextField(max_length=200)
    class Meta:
        db_table = 'medical'
class shoppingmall(models.Model):
    name=models.TextField(max_length=30)
    address=models.TextField(max_length=50)
    image=models.ImageField(blank=True)
    url=models.TextField(max_length=200)
    class Meta:
        db_table = 'shoppingmall'
class coffeshop(models.Model):
    name=models.TextField(max_length=30)
    address=models.TextField(max_length=50)
    image=models.ImageField(blank=True)
    url=models.TextField(max_length=200)
    class Meta:
        db_table = 'coffeshop'