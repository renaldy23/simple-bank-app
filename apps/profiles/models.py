from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel


# Create your models here.
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)

    class Meta:
        db_table = "profiles"
