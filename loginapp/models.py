from django.db import models

# Create your models here.
class LoginData(models.Model):
    USER_TYPE_CHOICES = [
        (0,'Anonymus'),
        (1,'Registered'),
    ]
    username = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=11)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES,default=0)
    email = models.EmailField(max_length=255, blank=True, null=True)  # New optional field


    def __str__(self):
        return self.username
