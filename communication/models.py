from django.db import models
from datetime import datetime


class Post(models.Model):
    member = models.ForeignKey('accounts.Member')
    airport = models.ForeignKey('airports.Airport')
    body = models.TextField(null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.datetime_updated = datetime.now()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return u'{} - {}'.format(self.member, self.airport.icao)


class Comment(models.Model):
    member = models.ForeignKey('accounts.Member')
    post = models.ForeignKey('communication.Post')
    body = models.TextField(null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.datetime_updated = datetime.now()
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return u'{}, Comment on Post#{}'.format(self.member, self.post.id)
