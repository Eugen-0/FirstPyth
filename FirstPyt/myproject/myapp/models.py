from django.db import models

# Create your models here.
class Article (models.Model):
    title = models.CharField (max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)