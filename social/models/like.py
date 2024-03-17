from django.db import models
from social.models import Post
from account.models import CustomUser


class Like(models.Model):
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='likes')
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'like'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return self.post.title