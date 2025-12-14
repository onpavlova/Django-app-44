from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]  # цена не может быть отрицательной
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # Связь ForeignKey с разными вариантами on_delete
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # при удалении категории поле становится NULL
        null=True,
        blank=True,
        default=None,  # значение по умолчанию
        related_name='product_list'  # другое имя для обратной связи
    )

    def __str__(self):
        return f'Product: {self.name} {self.description} price = {self.price} category {self.category}'