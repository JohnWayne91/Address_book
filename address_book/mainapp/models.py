from django.db import models
from django.urls import reverse


class Contact(models.Model):
    first_name = models.CharField(blank=False, max_length=150)
    last_name = models.CharField(blank=False, max_length=150)
    phone_number = models.CharField(blank=False, max_length=20)
    photo = models.ImageField(blank=True)
    url = models.URLField(blank=True)
    country = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=100)
    street = models.CharField(blank=True, max_length=300)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_full_name')
        ]

    def get_absolute_url(self):
        return reverse('contact_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

