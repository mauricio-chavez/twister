"""Posts models for Twister project"""

from ..accounts.models import Profile
from django.db import models


class Post(models.Model):
    message = models.CharField('Twist message', max_length=280)
    profile = models.ForeignKey(Profile, null=True, on_delete=models.DO_NOTHING)
    replies = models.ManyToManyField('Post')
    likes = models.ManyToManyField(Profile, related_name='post_likes')
    retwists = models.ManyToManyField(Profile, related_name='post_retwists')
    created = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.profile.display_name} : { self.message[:15] }'

    
    class Meta:
        ordering = ('-created',)