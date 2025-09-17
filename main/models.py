from django.db import models

from django.contrib.auth.models import User

import uuid

class Product(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
    ("Finisher", "Finisher"),
    ("Speedster", "Speedster"),
    ("Playmaker", "Playmaker"),
    ("Reinforcer", "Reinforcer"),
    ("Strategist", "Strategist"),
    ("Specialist", "Specialist")]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)                 
    price = models.IntegerField()                           
    description = models.TextField()                        
    thumbnail = models.URLField(blank=True, null=True)      
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)        
    is_featured = models.BooleanField(default=False)        
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=50, blank=True, null=True)
    hype =  models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def is_product_hype(self):
        return self.hype > 20
        
    def increment_hype(self):
        self.hype += 1
        self.save()

class Employee(models.Model) :
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    persona = models.TextField()
