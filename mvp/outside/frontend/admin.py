# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Seller, Lead, ClosingEvent


class SellerAdmin(admin.ModelAdmin):
    list_display = (u'id', 'name', 'description', 'url', 'logo', 'owned_by')
    list_filter = ('owned_by',)
    search_fields = ('name',)
admin.site.register(Seller, SellerAdmin)


class LeadAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'name',
        'address',
        'phone',
        'comment',
        'contact_name',
        'email',
        'website',
        'google_places_url',
        'closed',
        'lost',
        'repeat_at',
        'last_visited_at',
        'created',
        'updated',
        'lng',
        'lat',
        'owned_by',
        'last_visited_by',
    )
    list_filter = (
        'closed',
        'lost',
        'repeat_at',
        'last_visited_at',
        'created',
        'updated',
    )
    search_fields = ('name',)
admin.site.register(Lead, LeadAdmin)


class ClosingEventAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'user',
        'lead',
        'seller',
        'proof',
        'created',
        'updated',
    )
    list_filter = ('user', 'lead', 'seller', 'created', 'updated')
admin.site.register(ClosingEvent, ClosingEventAdmin)

