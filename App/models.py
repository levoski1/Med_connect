from django.db import models

# Create your models here.

class Participant(models.Model):
    user_type_choice = (
         ('patient', 'Patient'),
         ('doctor', 'Doctor')
     ) 
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    user_type = models.CharField(max_length=10, choices=user_type_choice)
    created_at = models.DateTimeField()
   

    def __str__(self):
        return self.email
    
