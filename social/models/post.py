from django.db import models
from account.models import CustomUser
from autoslug import AutoSlugField


class Post(models.Model):
    title = models.CharField(max_length=170)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    content = models.TextField()
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title