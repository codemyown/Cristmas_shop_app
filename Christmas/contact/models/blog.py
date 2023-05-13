from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to = "upload/images")
    content = models.CharField(max_length = 50)
    desc = models.TextField()
    date = models.CharField(max_length = 40)
    
    def __str__(self):
        return self.content

        
    def get_all_Data():
        return Blog.objects.all()
    
    