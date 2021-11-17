from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Contact
from .forms import AddContactForm


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


class AddContactView(CreateView):
    form_class = AddContactForm
    template_name = 'mainapp/add_contact.html'
    success_url = reverse_lazy('base')


class DeleteContact(DeleteView):
    model = Contact
    success_url = reverse_lazy('base')


class ContactUpdateView(UpdateView):
    model = Contact
    fields = '__all__'
    template_name = 'mainapp/contact_update_form.html'
    success_url = reverse_lazy('base')



