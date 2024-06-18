from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=50,)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=True)
    # cover = models.ImageField(upload_to='covers/', blank=True)

    date_time_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} : {self.author}'

    def get_absolute_url(self):  # canonical url
        return reverse('product_detail', args=[self.id])


class Comment(models.Model):
    text = models.TextField()
    date_time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} : {self.text}'

