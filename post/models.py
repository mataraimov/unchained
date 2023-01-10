from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='post_image/')
    post_date = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
