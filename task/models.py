

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    price = models.IntegerField(default=0) 
    broker=models.CharField(max_length=25, null=True, blank=True)
    deadline=models.DateTimeField(auto_now_add=False , null=True, blank=True)       
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
