from django.db import models

class Picture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='pictures/')

    def __str__(self):
        return self.title
