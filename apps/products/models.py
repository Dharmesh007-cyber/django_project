from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",     # 👈 reverse FK
    )
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
