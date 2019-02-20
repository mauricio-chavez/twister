"""Posts models for Twister project"""

from ..accounts.models import Profile
from django.db import models


class Post(models.Model):
    message = models.CharField('Twist message', max_length=280)
    profile = models.ForeignKey(
        to=Profile,
        null=True,
        on_delete=models.DO_NOTHING
    )
    replies = models.ManyToManyField(
        to='Post',
        blank=True
    )
    supports = models.ManyToManyField(
        to=Profile,
        related_name='post_likes',
        blank=True
    )
    retwists = models.ManyToManyField(
        to=Profile,
        related_name='post_retwists',
        blank=True
    )
    created = models.DateField(auto_now=True)

    def __str__(self):
        if len(self.message[:15]) <= 15:
            return f'{self.profile.display_name} : { self.message[:15] }'
        return f'{self.profile.display_name} : { self.message[:15] }...'

    
    class Meta:
        ordering = ['-created']