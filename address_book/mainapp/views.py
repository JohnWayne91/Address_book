from django.views.generic import ListView, DetailView

from .models import Contact, Address


class ContactListView(ListView):
    model = Contact
    template_name = 'mainapp/base.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.all().order_by('first_name', 'last_name')


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'mainapp/contact_detail.html'
    context_object_name = 'contact'
    slug_url_kwarg = 'slug'

