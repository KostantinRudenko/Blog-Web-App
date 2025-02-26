from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.timezone import now

from django.urls import reverse

from django.core.mail import send_mail

from blog_app.settings import DOMAIN_NAME

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
        link = reverse("user:verification", kwargs={"email":self.user.email, "uuid":self.code})
        verification_link = f"{DOMAIN_NAME}{link}"
        subject = f"Email verification for {self.user.email}"
        message = "For verification of email for {} continue by the link: {}".format(
            self.user.email,
            verification_link
        )
        send_mail(
            subject=subject,
            message=message,
            from_email="from@example.com",
            recipient_list=[self.user.email],
            fail_silently=False,
        )
    
    def is_expired(self):
        return self.expiration <= now()