from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    photo = models.ImageField(max_length=100)
    
    def __str__(self):
        return self.name
    
