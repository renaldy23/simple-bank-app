import os

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.profiles.models import Profile


# Create your views here.
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ["phone","address","date_of_birth","photo"]
    template_name = "profile/update.html"
    object = "profile"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        profile = form.save(commit=False)
        old_photo = self.get_object().photo
        new_photo = form.cleaned_data.get("photo")
        print(form.cleaned_data)

        print(new_photo)

        if new_photo and old_photo and old_photo != new_photo:
            if os.path.isfile(old_photo.path):
                os.remove(old_photo.path)

        profile.is_complete = True
        profile.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Profile"
        return context

