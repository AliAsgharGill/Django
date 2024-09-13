from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    USER_TYPE_CHOICE = [
        ('FE', 'Front-end Developer'),
        ("BE", "Back-end Developer"),
        ("FS", "Fullstack Developer"),
    ]
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user_image/", null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    type  = models.CharField(max_length=2, choices=USER_TYPE_CHOICE)
    work_role = models.TextField(default="")
    
    def __str__(self):
        return str(self.username)
