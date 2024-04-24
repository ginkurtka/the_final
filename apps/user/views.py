from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.booking.models import Booking

# from apps.booking.models import Booking, 
from apps.user.forms import LoginForm, CreateUserForm


def us_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(
                request=request,
                username=username,
                password=password
            )

            if user is not None:
                auth.login(request, user=user)

                return redirect('router:booking:all_booking')

    context = {
        "form": form
    }

    return render(
        request=request,
        template_name='user/login.html',
        context=context
    )


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('router:user:login')

    context = {
        "form": form
    }

    return render(
        request=request,
        template_name='user/register.html',
        context=context
    )


@login_required(login_url='router:user:login')
def us_info(request):
    user = get_object_or_404(User, id=request.user.id)

    # booking = Booking.objects.all()
    # Booking.objects.filter(user_id = user.id)
    booking_id = Booking.objects.filter(user_id = 3)
    # print(f'{booking.}')
    print(f'{booking_id}')

    
    # print(f"==>> user: {user.id}")
    # find_user = User.objects.get(id=user.id)
    # print(f"==>> find_user.name : {find_user.first_name} {find_user.last_name}")
    return redirect('router:user:register')


@login_required(login_url='router:user:login')
def us_logout(request):
    auth.logout(request=request)
    return redirect('router:user:login')
