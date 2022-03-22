from django.shortcuts import render
from .models import Contact
from django.views.generic.list import ListView
from .forms import ContactForm

def create_contact(request):
    # form = ContactForm(request.POST)
    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()

    # contacts = Contact.objects.all()
    # return render(request, 'contact-list.html', {'contacts': contacts})

    name = request.POST.get('contactname')
    phone_number = request.POST.get('phone_number')
    
    # add contact
    contact = Contact.objects.create(name=name, phone_number=phone_number)

    
    # add the contact to the contact list
    # request.objects.add(contact)

    # return template fragment with all the user's contacts
    contacts = Contact.objects.all()
    return render(request, 'contact-list.html', {'contacts': contacts})

class ContactList(ListView):
    template_name = 'contact.html'
    model = Contact
    context_object_name = 'contacts'