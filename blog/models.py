
# username for this model is yashm

from django.db import models
from django.urls import reverse, reverse_lazy


class Blog(models.Model):
    title  = models.CharField(max_length = 120)
    body   = models.TextField(max_length = 3000)
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE, default = 1)
    #author  = models.ForeignKey(User, default = 1, null = True, on_delete = models.SET_NULL)
    
    def __str__(self):
        return self.title[:50]
    
    def get_absolute_url(self):
        return reverse('blog_detail', args = [str(self.id)])


