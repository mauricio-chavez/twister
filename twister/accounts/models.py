"""Accounts models for Twister project"""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to=User, 
        on_delete=models.CASCADE, 
        related_name='profile_user'
    )
    display_name = models.CharField('Name to display', max_length=15)
    avatar = models.ImageField(
        verbose_name='Avatar',
        upload_to='avatars',
        blank=True, 
        null=True
    )
    biography = models.CharField(
        verbose_name='Biography',
        max_length=100,
        blank=True,
        default=None
    )
    birthday = models.DateField('Birthday', blank=True, null=True)
    location = models.CharField('Location', max_length=15, blank=True, null=True)
    website = models.URLField('Website', blank=True, null=True)
    following = models.ManyToManyField(
        to=User, 
        blank=True, 
        related_name='profile_followers'
    )
    followers = models.ManyToManyField(
        to=User,
        blank=True,
        related_name='profile_following'
    )

    
    def __str__(self):
        return f'{ self.display_name }'
