from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from products.models import Product
from django.http import HttpResponse
from profiles.models import UserProfile

from django.conf import settings

from .forms import ContactForm


def index(request):
    """
    A view to return the index page with the latest 3 products
    displayed on the latest arrival section.
    """
    latest_products = Product.objects.all()  
    no_of_products = len(latest_products)
    print(no_of_products)
    latest_arrival_1 = get_object_or_404(Product, pk=(no_of_products - 2))
    latest_arrival_2 = get_object_or_404(Product, pk=(no_of_products - 1))
    latest_arrival_3 = get_object_or_404(Product, pk=(no_of_products))

    # Prefill the email address field on the contact form
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        contact_form = ContactForm(initial={"email": profile.default_email})
    else:
        contact_form = ContactForm()

    context = {
        'latest_arrival_1': latest_arrival_1,
        'latest_arrival_2': latest_arrival_2,
        'latest_arrival_3': latest_arrival_3,
        'contact_form': contact_form,
    }
    template = 'home/index.html'
    return render(request, template, context)


def contactform(request):
    """
    Send an email to Bubbles when users
    want to share a feedback via contact form
    """
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        name = contact_form.cleaned_data['name']
        email = contact_form.cleaned_data['email']
        message = contact_form.cleaned_data['message']
        try:
            send_mail(
                f"You've got a message from {name} ({email}) on contact form.",
                f"Message: {message}",
                email,
                [settings.DEFAULT_FROM_EMAIL],
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

    return redirect('contact_ack')


def contact_ack(request):
    """
    A view to render thank you page after site visitors send a contact form
    """
    return render(request, 'home/acknowledgement.html')