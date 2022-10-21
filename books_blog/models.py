from django.db import models


class PostBook(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    full_description = models.TextField(null=True)
    image = models.ImageField(upload_to='')
    author = models.CharField(max_length=255)
    pages = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
