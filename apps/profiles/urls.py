from django.urls import path

from apps.profiles.views import ProfileUpdate

urlpatterns = [
    path("profile/update/<str:pk>",view=ProfileUpdate.as_view(),name="profile-update"),
]