from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PrescriptionModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    prescription_image = models.ImageField(upload_to='prescription/')
    description = models.TextField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Prescription of {self.id} by {self.user.username}'