from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES_CHOICES = [
    ('sales', 'sales'),
    ('support', 'support'),
    ('management', 'management'),
]


class Member(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    role = models.CharField(
        max_length=20,
        choices=ROLES_CHOICES,
        blank=True,
        default="")
    is_staff = models.BooleanField(default=True)
    email = models.EmailField(unique=True)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
