from PIL import Image
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(default='user_default.png', upload_to='profile_image')

    def __str__(self):
        return f'{self.user.username} profile image'

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height > 150 or img.width>150:
            output_size=(150,150)
            img.thumbnail(output_size)
            img.save(self.image.path)