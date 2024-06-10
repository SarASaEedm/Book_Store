from django.db import models

# Create your models here.
# models.py


class Book(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    no_of_pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(upload_to='bookindex/images/', null=True, blank=True)

    def __str__(self):
        return self.title
