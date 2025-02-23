"""
File: serializers.py
Created by: K. Zimmerman
Project: kc_royals_backend
Description:
- Serializes Player, BattingStat, and PitchingStat models.
- Matches `players.json` == `models.py` 
"""

from rest_framework import serializers
from .models import Player, BattingStat, PitchingStat

class BattingStatSerializer(serializers.ModelSerializer):
    """Serializes BattingStat model for API response."""
    class Meta:
        model = BattingStat
        fields = ["id", "year", "league", "plate_appearances", "at_bats", "hits", "home_runs", "stolen_bases"]

class PitchingStatSerializer(serializers.ModelSerializer):
    """Serializes PitchingStat model for API response."""
    class Meta:
        model = PitchingStat
        fields = ["id", "year", "league", "innings_pitched", "wins", "losses", "strikeouts"]

class PlayerSerializer(serializers.ModelSerializer):
    """Serializes Player model including related batting and pitching stats."""
    
    batting_stats = BattingStatSerializer(many=True, read_only=True, source="batting")
    pitching_stats = PitchingStatSerializer(many=True, read_only=True, source="pitching")

    class Meta:
        model = Player
        fields = ["id", "name_first", "name_last", "team", "primary_position", "batting_stats", "pitching_stats"]
        depth = 1
