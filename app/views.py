from .models import Contact
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model
from django.shortcuts import render

def create_contact(request):
    name = request.POST.get('contactname')
    phone_number = request.POST.get('phone_number')
    
    # add film
    contact = Contact.objects.create(name=name, phone_number=phone_number)
    
    # add the contact to the contact list
    request.contacts.add(contact)

    # return template fragment with all the user's films
    contacts = request.films.all()
    return render(request, 'contact-list.html', {'contacts': contacts})

class FilmList(ListView):
    template_name = 'contact.html'
    model = Contact
    context_object_name = 'contacts'