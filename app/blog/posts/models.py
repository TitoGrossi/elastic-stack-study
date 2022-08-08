from typing import Any

from django.db import models
from django.contrib.auth.models import User

from blog.querysets import AsyncQuerySet
# from django.db.models import BaseManager


class Post(models.Model):
    """"""
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(null=False, blank=False, max_length=255)
    content = models.TextField(null=False, blank=False)

    # objects: BaseManager[Any] = AsyncQuerySet.as_manager()
    objects = AsyncQuerySet.as_manager()

    class Meta:
        db_table = "post"


class Like(models.Model):
    user = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post, null=False,
        related_name="likes",
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("user", "post"),
                name="unique_like_per_user",
            ),
        )

        db_table = "like"
