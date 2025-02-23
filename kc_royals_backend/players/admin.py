"""
File: admin.py
Created by: K. Zimmerman
Project: kc_royals_backend
Description:
- Customizes Django Admin panel branding (title & header).
- Changes "View Site" link to "View Frontend" and links to React frontend.
"""

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html
from .models import Player, BattingStat, PitchingStat

# Customize Django Admin Branding
admin.site.site_header = "KC Royals Backend Admin"
admin.site.site_title = "KC Royals Admin Portal"
admin.site.index_title = "Welcome to the KC Royals Backend"

# Change "View Site" to "View Frontend" (Redirect to React Frontend)
admin.site.site_url = "http://localhost:3000/"

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("id", "name_first", "name_last", "team", "primary_position")
    search_fields = ("name_first", "name_last", "team")
    list_filter = ("team", "primary_position")

@admin.register(BattingStat)
class BattingStatAdmin(admin.ModelAdmin):
    list_display = ("player", "year", "league", "plate_appearances", "hits", "home_runs", "stolen_bases")
    search_fields = ("player__name_last", "player__name_first", "year")
    list_filter = ("year", "league")

@admin.register(PitchingStat)
class PitchingStatAdmin(admin.ModelAdmin):
    list_display = ("player", "year", "league", "innings_pitched", "wins", "losses", "strikeouts")
    search_fields = ("player__name_last", "player__name_first", "year")
    list_filter = ("year", "league")

# Register Django's built-in User model
admin.site.unregister(User)  # Remove default User view
admin.site.register(User, UserAdmin)  # Register with UserAdmin
