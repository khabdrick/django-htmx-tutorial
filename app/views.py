from django.http import HttpResponse
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

def delete_contact(request, pk):
    # remove the contact from list.
    contact_id = Contact.objects.get(id=pk)
    contact_id.delete()
    # return template fragment with all the user's films
    contacts = Contact.objects.all()
    return render(request, 'contact-list.html', {'contacts': contacts})

def check_name(request):
    name = request.POST.get('contactname')
    if Contact.objects.filter(name=name).exists():
        print (name)
        return HttpResponse("<div style='color: red;'>This name already exist</div>")
    else:
        return HttpResponse("<div style='color: green;'>This name does not exist</div>")