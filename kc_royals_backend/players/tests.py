"""
File: tests.py
Version: Pre-Production
Created by: K. Zimmerman
Project: kc_royals_backend
Description:
- Defines automated backend unit tests.
- Tests authentication, player listing, and player creation.
- Ensures role-based permissions are enforced.
"""

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Player

class PlayerAPITestCase(APITestCase):
    """Integration tests for the Player API."""

    def setUp(self):
        """Create test user and sample player."""
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpass")
        self.client.login(username="admin", password="adminpass")
        self.player = Player.objects.create(
            id=1001, first_name="John", last_name="Doe", team="KC",
            birth_date="1995-06-15", height_feet=6, weight=180,
            throws="R", bats="R", position="Pitcher"
        )

    def test_get_players(self):
        """Ensure all users can retrieve player data."""
        response = self.client.get("/api/players/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_player_admin(self):
        """Ensure an admin user can create a player."""
        data = {
            "id": 1002, "first_name": "Mike", "last_name": "Smith", "team": "KC",
            "birth_date": "1997-04-10", "height_feet": 6, "weight": 190,
            "throws": "R", "bats": "R", "position": "Catcher"
        }
        response = self.client.post("/api/players/manage/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_player_non_admin(self):
        """Ensure a regular user cannot create a player."""
        self.client.logout()
        response = self.client.post("/api/players/manage/", {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
