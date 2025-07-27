from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:  # solo al crear
            self.is_staff = False  # alumno no es staff
        super().save(*args, **kwargs)
