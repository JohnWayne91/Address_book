from django.urls import path

from.views import ContactListApiView, ContactDetailApiView, ContactCreateApiView


urlpatterns = [
    path('contact-list/', ContactListApiView.as_view(), name='contact_list'),
    path('contact-detail/<int:pk>/', ContactDetailApiView.as_view(), name='contact-detail'),
    path('create-contact/', ContactCreateApiView.as_view(), name='create-contact')
]