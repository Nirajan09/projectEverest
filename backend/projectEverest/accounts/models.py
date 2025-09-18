import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)

    email = models.EmailField(unique=True, db_index=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)

    is_active = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
