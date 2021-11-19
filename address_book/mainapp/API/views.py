from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.filters import SearchFilter

from .serializers import ContactSerializer
from ..models import Contact


class ContactListApiView(ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name', 'phone_number', 'country', 'city']


class ContactDetailApiView(RetrieveUpdateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = 'pk'


class ContactCreateApiView(CreateAPIView):
    serializer_class = ContactSerializer

