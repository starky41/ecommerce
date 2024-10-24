from django.db import models

# Create your models here. 
from django.core.exceptions import ValidationError
from PIL import Image
from users.models import CustomUser

def validate_image_square(image):
    img = Image.open(image)
    width, height = img.size

    # Check if the width and height are equal
    if width != height:
        raise ValidationError("Image must be square (1:1 aspect ratio).")


from django.db import models

class Good(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='goods/', validators=[validate_image_square], null=True, blank=True)

    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Add this line


    def __str__(self):
        return self.name
