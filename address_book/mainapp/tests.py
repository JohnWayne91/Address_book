from django.test import TestCase

from .models import Contact


class ContactModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Contact.objects.create(
            first_name='Test',
            last_name='Testovich',
            phone_number='093-552-39-58',
            url='https://www.youtube.com/',
            country='TestLand',
            city='Testopolis',
            street='Testovaya 28'
        )

    def test_first_name_label(self):
        contact = Contact.objects.get(pk=1)
        field_label = contact._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name(self):
        contact = Contact.objects.get(pk=1)
        first_name = contact.first_name
        self.assertEquals(first_name, 'Test')

    def test_last_name_label(self):
        author = Contact.objects.get(pk=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_last_name(self):
        contact = Contact.objects.get(pk=1)
        last_name = contact.last_name
        self.assertEquals(last_name, 'Testovich')

    def test_country(self):
        contact = Contact.objects.get(pk=1)
        country = contact.country
        self.assertEquals(country, 'TestLand')

    def test_city(self):
        contact = Contact.objects.get(pk=1)
        city = contact.city
        self.assertEquals(city, 'Testopolis')

    def test_street(self):
        contact = Contact.objects.get(pk=1)
        street = contact.street
        self.assertEquals(street, 'Testovaya 28')

    def test_phone_number(self):
        contact = Contact.objects.get(pk=1)
        phone_number = contact.phone_number
        self.assertEquals(phone_number, '093-552-39-58')

    def test_url(self):
        contact = Contact.objects.get(pk=1)
        url = contact.url
        self.assertEquals(url, 'https://www.youtube.com/')

    def test_get_absolute_url(self):
        contact = Contact.objects.get(id=1)
        self.assertEquals(contact.get_absolute_url(), '/contact/1/')

