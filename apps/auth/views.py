from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from apps.profiles.models import Profile
from django.db import transaction


# Create your views here.
class RegisterView(View):
    def get(self, request):
        return render(request, "auth/register.html")

class LoginProcessView(View):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("/login/")

class RegisterProcessView(View):
    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                # Creating the associated profile
                Profile.objects.create(user=user)

            messages.success(request, "Registration successful. You can now log in.")
            return redirect("/login/")
        except Exception as e:
            # Handle exceptions, rollback transaction
            messages.error(request, f"Registration failed: {str(e)}")
            return redirect("/register/")

