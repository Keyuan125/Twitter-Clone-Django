from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True,  # This means that if no data insert to this field, it will be null
        help_text='The one who posts this tweet', # This will show up in the admin page
    )
    content = models.CharField(max_length=255) # Should be 255 (2^x-1) instead of 256 because there is a '\0' at the end
    created_at = models.DateTimeField(auto_now_add=True)