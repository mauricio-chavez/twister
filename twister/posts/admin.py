"""Admin config for posts app"""

from django.contrib import admin

from  .models import Post


admin.site.register(Post)
