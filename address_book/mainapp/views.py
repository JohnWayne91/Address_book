from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Contact
from .forms import AddContactForm


class ContactListView(ListView):
    model = Contact
    template_name = 'mainapp/base.html'
    context_object_name = 'contacts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Address book'
        return context

    def get_queryset(self):
        return Contact.objects.all().order_by('first_name', 'last_name')


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'mainapp/contact_detail.html'
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact detail'
        return context


class AddContactView(CreateView):
    form_class = AddContactForm
    template_name = 'mainapp/add_contact.html'
    success_url = reverse_lazy('base')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add contact'
        return context


class DeleteContact(DeleteView):
    model = Contact
    success_url = reverse_lazy('base')


class ContactUpdateView(UpdateView):
    model = Contact
    fields = '__all__'
    template_name = 'mainapp/contact_update_form.html'
    success_url = reverse_lazy('base')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit contact'
        return context


class SearchResultsView(ListView):
    model = Contact
    template_name = 'mainapp/search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Search result'
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Contact.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(country__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(city__icontains=query)
        )
        return object_list


