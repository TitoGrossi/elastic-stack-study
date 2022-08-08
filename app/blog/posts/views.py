import logging

from django.http import HttpRequest
from django.shortcuts import render

from .models import Like


logger = logging.getLogger('mysite')


def index(request: HttpRequest):
    if not request.user.is_authenticated:
        return None
    lastes_likes = Like.objects.filter(
        user=request.user).select_related("post")[:5]
    logger.warning(
        'This is a warning!',
        exc_info=True
    )

    return render(request=request, template_name='posts/index.html', context={'lastes_likes': lastes_likes})
