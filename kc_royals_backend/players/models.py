"""
File: models.py
Created by: K. Zimmerman
Project: kc_royals_backend
Description:
- Defines Player, BattingStat, and PitchingStat models.
- Ensures exact field names match `players.json`.
- Adds default values to prevent migration issues.
"""

from django.db import models

class Player(models.Model):
    """
    Represents a baseball player with attributes matching `players.json`.

    Fields:
    - id: Auto-incremented primary key.
    - name_first: First name of the player.
    - name_use: Preferred name (if different from first name).
    - name_last: Last name of the player.
    - team: Team abbreviation (e.g., "KC" for Kansas City Royals).
    - birth_date: Player's birth date (optional).
    - height_feet: Height of the player in feet (optional).
    - height_inches: Additional inches for height (optional).
    - weight: Player's weight in pounds (optional).
    - throws: Throwing hand (L = Left, R = Right).
    - bats: Batting hand (L = Left, R = Right, S = Switch).
    - primary_position: Player’s primary position (2-character code).
    """
    id = models.AutoField(primary_key=True)
    name_first = models.CharField(max_length=50)
    name_use = models.CharField(max_length=50, null=True, blank=True)
    name_last = models.CharField(max_length=50)
    team = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    height_feet = models.IntegerField(null=True, blank=True)
    height_inches = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    throws = models.CharField(max_length=1, choices=[("L", "Left"), ("R", "Right")])
    bats = models.CharField(max_length=1, choices=[("L", "Left"), ("R", "Right"), ("S", "Switch")])
    primary_position = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return f"{self.name_first} {self.name_last}"

class BattingStat(models.Model):
    """
    Stores batting statistics for each player per season.

    Fields:
    - player: ForeignKey linking to Player model.
    - year: The season year.
    - league: League abbreviation (optional).
    - org_abbreviation: Organization/team abbreviation.
    - plate_appearances, at_bats, games: Batting-related game statistics.
    - runs, hits, doubles, triples, home_runs: Offensive performance metrics.
    - bases_on_balls: Walks (default 0).
    - strikeouts, sacrifices, sacrifice_flies, stolen_bases, caught_stealing: Additional stats.
    """
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="batting")
    year = models.IntegerField()
    league = models.CharField(max_length=10, null=True, blank=True)
    org_abbreviation = models.CharField(max_length=10, default="")
    plate_appearances = models.IntegerField(default=0)
    at_bats = models.IntegerField(default=0)
    games = models.IntegerField(default=0)
    games_started = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    doubles = models.IntegerField(default=0)
    triples = models.IntegerField(default=0)
    home_runs = models.IntegerField(default=0)
    bases_on_balls = models.IntegerField(default=0)
    strikeouts = models.IntegerField(default=0)
    sacrifices = models.IntegerField(default=0)
    sacrifice_flies = models.IntegerField(default=0)
    stolen_bases = models.IntegerField(default=0)
    caught_stealing = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.name_last} ({self.year}) Batting Stats"

class PitchingStat(models.Model):
    """
    Stores pitching statistics for each player per season.

    Fields:
    - player: ForeignKey linking to Player model.
    - year: The season year.
    - league: League abbreviation (optional).
    - org_abbreviation: Organization/team abbreviation.
    - games, games_started, complete_games, games_finished: Pitching game statistics.
    - innings_pitched: Number of innings pitched.
    - wins, losses, saves: Performance metrics.
    - total_batters_faced, at_bats: Batters faced and at-bats against.
    - hits, doubles, triples, home_runs: Hit-related statistics.
    - bases_on_balls: Walks (default 0).
    - strikeouts: Number of strikeouts recorded.
    """
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="pitching")
    year = models.IntegerField()
    league = models.CharField(max_length=10, null=True, blank=True)
    org_abbreviation = models.CharField(max_length=10, default="")
    games = models.IntegerField(default=0)
    games_started = models.IntegerField(default=0)
    complete_games = models.IntegerField(default=0)
    games_finished = models.IntegerField(default=0)
    innings_pitched = models.FloatField(default=0.0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    total_batters_faced = models.IntegerField(default=0)
    at_bats = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    doubles = models.IntegerField(default=0)
    triples = models.IntegerField(default=0)
    home_runs = models.IntegerField(default=0)
    bases_on_balls = models.IntegerField(default=0)
    strikeouts = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.name_last} ({self.year}) Pitching Stats"
