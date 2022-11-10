from django.db import models


class Category(models.Model):
    TITLE_MAX_LENGTH = 255

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )


class Expense(models.Model):
    AMOUNT_MAX_DIGITS = 10
    AMOUNT_DECIMAL_PLACES = 2

    date = models.DateField(
        auto_now_add=True,
    )
    amount = models.DecimalField(
        max_digits=AMOUNT_MAX_DIGITS,
        decimal_places=AMOUNT_DECIMAL_PLACES,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
