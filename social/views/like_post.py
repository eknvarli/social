from django.shortcuts import redirect, get_object_or_404
from social.models import Post, Like
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required
def like_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if Like.objects.filter(from_user=request.user, post=post).exists():
        return JsonResponse({'message': 'Postu zaten beğendin.'})

    else:
        Like.objects.create(
            from_user=request.user,
            post=post
        )

        likes_count = post.likes.count()
        return JsonResponse({'message': 'Post başarıyla beğenildi.', 'likes_count': likes_count})