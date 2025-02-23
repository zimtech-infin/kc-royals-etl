
"""
File: apps.py
Created by: K. Zimmerman
Project: kc_royals_backend
Description:
- Defines the Django application configuration for the `players` app.
- Registers the `players` app within the Django project.
- Ensures proper app initialization and compatibility with Django settings.
"""



from django.apps import AppConfig


class PlayersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'players'
