from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    TITLE_MAX_LENGTH = 25

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    def __str__(self):
        return self.title


class Expense(models.Model):
    AMOUNT_MAX_DIGITS = 10
    AMOUNT_DECIMAL_PLACES = 2
    AMOUNT_MIN_VALUE = 0.01

    date = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    amount = models.DecimalField(
        max_digits=AMOUNT_MAX_DIGITS,
        decimal_places=AMOUNT_DECIMAL_PLACES,
        validators=(
            MinValueValidator(AMOUNT_MIN_VALUE),
        )
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
