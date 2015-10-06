from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Seller(models.Model):
    # Fields
    name = models.TextField(null=False, blank=False, db_index=True)
    description = models.TextField(null=False, blank=False, db_index=True)
    url = models.URLField(null=True, blank=True)
    logo = models.URLField(null=True, blank=True)
    reward = models.FloatField(null=False, blank=False, default=0.00)

    # References
    owned_by = models.ForeignKey(User, null=False, blank=False)

class Lead(models.Model):
    # Fields
    name = models.TextField(null=False, blank=False, db_index=True)
    address = models.TextField(null=False, blank=False, db_index=True)
    phone = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    contact_name = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    google_places_url = models.URLField(null=True, blank=True)

    closed = models.BooleanField(default=False)
    lost = models.BooleanField(default=False)
    repeat_at = models.DateTimeField(null=True, blank=True, db_index=True)

    last_visited_at = models.DateTimeField(null=True, blank=True, db_index=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # TODO: We should replace this with GeoDjango (search, filter within radius, etc)
    lng = models.FloatField(default=0.0)
    lat = models.FloatField(default=0.0)

    # References
    owned_by = models.ForeignKey(Seller, null=True, blank=False, default=None, on_delete=models.SET_NULL)
    last_visited_by = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.SET_NULL)

class ClosingEvent(models.Model):

    # References
    user = models.ForeignKey(User,null=False,blank=False)
    lead = models.ForeignKey(Lead,null=False,blank=False)
    seller = models.ForeignKey(Seller, null = False, blank = False)

    # Fields
    proof = models.TextField(null=True,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=('user','lead','seller')