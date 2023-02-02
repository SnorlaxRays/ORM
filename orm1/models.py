from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Album'
    
class Song(models.Model):
    name = models.CharField(max_length=20)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Song'
        
        
#the model country 

class Country(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Country'

#the model capital

class Capital(models.Model):
    country = models.OneToOneField(Country,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=34)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Capital'
        

from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=343, null=True)
    email = models.EmailField(max_length=233,null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Customer'
        

#One-to-Many Relationship

class Country1(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Country1'

#the model city

class City(models.Model):
    country = models.ForeignKey(Country1,on_delete=models.CASCADE)
    name = models.CharField(max_length=34)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'City'
        

class Customer1(models.Model):
    name = models.CharField(max_length=343, null=True)
    email = models.EmailField(max_length=233,null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Customer1'
        
class Order(models.Model):
    customer = models.ForeignKey(Customer1,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=True)
    transaction_id = models.CharField(max_length=443,null=True)
    
    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'Order'
        
        
#ManyToMany Relationship


class Teacher(models.Model):
    first_name = models.CharField(max_length=34)
    last_name = models.CharField(max_length=34)
    email = models.EmailField(max_length=34)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'Teacher'
        
class Subject(models.Model):
    teachers = models.ManyToManyField(Teacher)
    title = models.CharField(max_length=342)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Subject'
        

class Subject1(models.Model):
    title = models.CharField(max_length=342)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Subject1'
        
class Teacher1(models.Model):
    subjects = models.ManyToManyField(Subject1)
    first_name = models.CharField(max_length=34)
    last_name = models.CharField(max_length=34)
    email = models.EmailField(max_length=34)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'Teacher1'
        

    
    

