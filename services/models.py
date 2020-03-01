from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.CharField(max_length=30, null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title
