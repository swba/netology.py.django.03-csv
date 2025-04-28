from django.db import models
from slugify import slugify


class Phone(models.Model):
    name = models.CharField(100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(255)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)