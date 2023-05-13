from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 40)
    phone = models.IntegerField(default = 0)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    