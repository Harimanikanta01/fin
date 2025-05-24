from django.db import models
# Create your models here.
class Nari(models.Model):
    id=models.CharField(max_length=200,primary_key=True)
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    discount=models.CharField(max_length=200)
    image=models.FileField(upload_to="images/")
def __str__(self):
    return f"{self.id}"
class Banner(models.Model):
    id=models.TextField(max_length=20,primary_key=True)
    img=models.FileField(upload_to='images/')
def __str__(self):
    return {self.id}
class Create(models.Model):
    name=models.TextField(max_length=100)
    password=models.TextField(max_length=100)
def __str__(self):
    return f"{self.name}"
class Circle(models.Model):
    id=models.TextField(max_length=20,primary_key=True)
    image=models.FileField(upload_to="images/")
    text=models.TextField(max_length=200)
class P1(models.Model):
    id=models.TextField(max_length=10,primary_key=True)
    image=models.FileField(upload_to='images/')
    name=models.TextField(max_length=100)
    def __str__(self):
        return f'{self.id}'
class P2(models.Model):
    id=models.TextField(max_length=10,primary_key=True)
    image=models.FileField(upload_to='images/')
    name=models.TextField(max_length=100)
    def __str__(self):
        return f'{self.id}'
class Add(models.Model):
    id=models.TextField(max_length=10,primary_key=True)
    images=models.FileField(upload_to='images/')
    def __str__(self):
        return f'{self.id}'
class Discount(models.Model):
    id=models.TextField(max_length=10,primary_key=True)
    image=models.FileField(upload_to='images/')
    name=models.TextField(max_length=100)
    def __str__(self):
        return f'{self.id}'
class Mobile(models.Model):
    id= models.CharField(max_length=100,primary_key=True)
    img=models.FileField(upload_to="images/")
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=50)
    discount=models.CharField(max_length=10)
    discription=models.CharField(max_length=200)


# Account model
class account(models.Model):
    name = models.CharField(max_length=20)
    no = models.CharField(max_length=11)
    password = models.CharField(max_length=12)  
    def __str__(self):
        return self.name  
class Cart(models.Model):
    id= models.CharField(max_length=100,primary_key=True)
    img=models.CharField(max_length=300)
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=50)
    discount=models.CharField(max_length=10)
    

    def __str__(self):
        return f"Cart for {self.id}"
class product3(models.Model):
    name=models.CharField(max_length=20)
    images=models.FileField(upload_to='images/')
class Oh(models.Model):
    name=models.CharField(max_length=100)
