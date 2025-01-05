from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
from django.core.exceptions import ValidationError

# Create your models here.
def validate_image_format(image):
    valid_extensions = ['.jpg', '.jpeg', '.png']
    ext = os.path.splitext(image.name)[1].lower()

    if ext not in valid_extensions:
        raise ValidationError(f"Unsupported file format: {ext}. Allowed formats are: {', '.join(valid_extensions)}.")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg',
        upload_to='profile_pics',
        validators=[validate_image_format]
    )
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) 
            img.save(self.image.path)
