from django.shortcuts import render
from .models import Contact
from django.views.generic.list import ListView

def create_contact(request):

    name = request.POST.get('contactname')
    phone_number = request.POST.get('phone_number')
    
    # add contact
    contact = Contact.objects.create(name=name, phone_number=phone_number)
    contacts = Contact.objects.all()
    return render(request, 'contact-list.html', {'contacts': contacts})

class ContactList(ListView):
    template_name = 'contact.html'
    model = Contact
    context_object_name = 'contacts'