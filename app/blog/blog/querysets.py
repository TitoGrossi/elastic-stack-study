# from django.db import models
from django.db.models.query import QuerySet
from asgiref.sync import sync_to_async


class AsyncQuerySet(QuerySet):
    """queryset with async support for db calls"""

    async def get(self, *args, **kwargs):
        """async support for get"""
        return await sync_to_async(super().get, thread_sensitive=True)(*args, **kwargs)

    async def create(self, *args, **kwargs):
        """async support for create"""
        return await sync_to_async(super().create, thread_sensitive=True)(*args, **kwargs)

    async def update(self, **kwargs):
        """async support for update"""
        return await sync_to_async(super().update, thread_sensitive=True)(**kwargs)

    async def delete(self):
        """async support for delete"""
        return await sync_to_async(super().delete, thread_sensitive=True)()

    async def count(self):
        """async support for count"""
        return await sync_to_async(super().count, thread_sensitive=True)()

    async def aggregate(self, *args, **kwargs):
        """async support for aggregate"""
        return await sync_to_async(super().aggregate, thread_sensitive=True)(*args, **kwargs)

    async def first(self):
        """async support for first"""
        return await sync_to_async(super().first, thread_sensitive=True)()

    async def last(self):
        """async support for last"""
        return await sync_to_async(super().last, thread_sensitive=True)()
