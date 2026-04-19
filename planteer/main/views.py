from django.shortcuts import render, redirect
from plants.models import Plant
from .models import Contact
from .forms import ContactForm

def home_view(request):
    plants = Plant.objects.all()
    return render(request, 'main/index.html', {"plants": plants})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:contact_messages')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {"form": form})

def contact_messages_view(request):
    contact_messages = Contact.objects.all().order_by('-created_at')
    return render(request, 'main/contact-messages.html', {"contact_messages": contact_messages})