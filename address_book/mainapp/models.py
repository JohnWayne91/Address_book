from django.db import models


class Contact(models.Model):
    first_name = models.CharField(blank=False, max_length=150)
    last_name = models.CharField(blank=False, max_length=150)
    phone_number = models.CharField(blank=False, max_length=20)
    photo = models.ImageField(blank=True)
    url = models.URLField(blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_full_name')
        ]


class Address(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='address')
    country = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=100)
    street = models.CharField(blank=True, max_length=300)
