from django.utils import timezone
from django.db import models

class Record(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    meetup = models.DateField(default=timezone.now)
    notification_sent = models.BooleanField(default=False)  

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
# Create your models here.
