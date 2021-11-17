from django.urls import path

from .views import *


urlpatterns = [
    path('', ContactListView.as_view(), name='base'),
    path('contact/<slug:slug>/', ContactDetailView.as_view(), name='contact_detail')
]
