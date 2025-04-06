from django.db import models

from core.utils import generate_id


class BaseModel(models.Model):
    id = models.CharField(
        max_length=255, primary_key=True, editable=False, default=generate_id
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
