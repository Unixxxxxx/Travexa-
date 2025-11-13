from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})
