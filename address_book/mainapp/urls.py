from django.urls import path

from .views import *


urlpatterns = [
    path('', ContactListView.as_view(), name='base'),
    path('contact/<pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('add-contact/', AddContactView.as_view(), name='add_contact'),
    path('delete/<int:pk>/', DeleteContact.as_view(), name='delete_contact'),
    path('update/<int:pk>/edit', ContactUpdateView.as_view(), name='update_contact'),
    path('search/', SearchResultsView.as_view(), name='search_results')
]
