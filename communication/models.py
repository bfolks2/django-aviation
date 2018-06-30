from django.db import models


class Post(models.Model):
    member = models.ForeignKey('accounts.Member')
    airport = models.ForeignKey('airports.Airport')
    body = models.TextField(null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    member = models.ForeignKey('accounts.Member')
    post = models.ForeignKey('communication.Post')
    body = models.TextField(null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now_add=True)
