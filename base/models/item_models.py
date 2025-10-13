from django.db import models
from django.utils.crypto import get_random_string
import os

def generate_unique_id():
    return get_random_string(length=22)

def upload_image_to(instance, filename):
    item_id = instance.item.id
    return os.path.join('static', 'items', item_id, filename)

class Tag(models.Model):
    slug = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
    

class Category(models.Model): # slugField 欲しいかも
    slug = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.CharField(primary_key=True, max_length=22, editable=False, default=generate_unique_id)
    name = models.CharField(max_length=100, default="")
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(default="", blank=True)
    sold_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_image_to, default="", blank=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='items', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='items', blank=True)

    def __str__(self):
        return self.name
