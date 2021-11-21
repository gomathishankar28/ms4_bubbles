from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile)
    order = Order.objects.filter(user_profile=profile)
    print(order)
    if not(order):
        template = 'profiles/profile_new.html'
        return render(request, template)
    else:
        order = profile.orders.latest('order_number')
        template = 'profiles/profile.html'
        context = {
            'profile': profile,
            'on_profile_page': True,
            'order': order,
        }
        return render(request, template, context)
        

@login_required
def order_history(request):
    """ Display the user's order history. """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
        'on_profile_page': True,
    }
    return render(request, template, context)


@login_required
def edit_profile(request):
    """ Display the user's edit profile details form. """

    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Check if form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    template = 'profiles/edit_profile.html'
    context = {
        'form': form,
        'on_profile_page': True,
    }
    return render(request, template, context)