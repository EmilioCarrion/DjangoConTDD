from django.db import models
from django.core.validators import MinValueValidator


class CartLine(models.Model):
    # This field is unique for this workshop purposes hehe :)
    sku = models.CharField(max_length=5, unique=True)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    # In a normal project this would not go here
    def to_dict(self):
        return {"sku": self.sku, "quantity": self.quantity}
