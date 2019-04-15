from django.shortcuts import render

from .models import Contacts

def index(request):

    contacts = Contacts.objects.all()

    context = {
        'contacts' : contacts
    }
    return render(request, 'contacts/index.html',context)

