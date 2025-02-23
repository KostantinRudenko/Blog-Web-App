from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.mail import send_mail

# Create your models here.
class BaseUser(AbstractUser):
    is_verified = models.BooleanField(default=False)

class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=BaseUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f"Email verification object for {self.user.email}"
    
    def send_verification_email(self):
        send_mail(
            "Subject here",
            "Test verification email.",
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )