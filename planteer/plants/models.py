from django.db import models

# Create your models here.

class Plant(models.Model):
    class Category(models.TextChoices):
        TREE = 'tree', 'Tree'
        FRUIT = 'fruit', 'Fruit'
        VEGETABLE = 'vegetable', 'Vegetable'
        FLOWER = 'flower', 'Flower'
        HERB = 'herb', 'Herb'

    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='plants/')
    category = models.CharField(max_length=50, choices=Category.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
