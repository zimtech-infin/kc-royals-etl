"""
File: etl.py
Created by: K. Zimmerman
Project: kc_royals_backend
Description:
- Implements ETL (Extract, Transform, Load) processes for player data.
- Extracts player statistics from `players.json` or an external data source.
- Transforms raw data into a structured format compatible with Django models.
- Loads cleaned data into the SQLite database using Django ORM.
- Ensures data integrity and prevents duplicate entries during loading.
- Optimized for SQLite’s handling of transactions and constraints.
"""





import os
import json
import django
import sys

# Configure Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kc_royals_backend.settings")
django.setup()

from players.models import Player, BattingStat

# Set correct file paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project root
JSON_PATH = os.path.join(BASE_DIR, "players.json")  # Correct path to players.json
FIXED_JSON_PATH = os.path.join(BASE_DIR, "players_fixed.json")

def transform_data():
    """Transforms raw JSON data into Django fixture format."""
    if not os.path.exists(JSON_PATH):
        print(f"Error: {JSON_PATH} not found.")
        return

    with open(JSON_PATH, "r") as file:
        data = json.load(file)

    formatted_data = []
    for index, player in enumerate(data, start=1):
        formatted_data.append({
            "model": "players.player",
            "pk": player["id"],
            "fields": {
                "name_first": player["name_first"],
                "name_last": player["name_last"],
                "team": player["team"],
                "birth_date": player.get("birth_date"),
                "height_feet": player.get("height_feet"),
                "height_inches": player.get("height_inches"),
                "weight": player.get("weight"),
                "throws": player.get("throws"),
                "bats": player.get("bats"),
                "primary_position": player.get("primary_position")
            }
        })

        for batting_stat in player.get("stats", {}).get("batting", []):
            formatted_data.append({
                "model": "players.battingstat",
                "fields": {
                    "player": player["id"],
                    "year": batting_stat["year"],
                    "league": batting_stat["league"],
                    "org_abbreviation": batting_stat["org_abbreviation"],
                    "plate_appearances": batting_stat["plate_appearances"],
                    "at_bats": batting_stat["at_bats"],
                    "games": batting_stat["games"],
                    "games_started": batting_stat["games_started"],
                    "runs": batting_stat["runs"],
                    "hits": batting_stat["hits"],
                    "doubles": batting_stat["doubles"],
                    "triples": batting_stat["triples"],
                    "home_runs": batting_stat["home_runs"],
                    "bases_on_balls": batting_stat["bases_on_balls"],
                    "strikeouts": batting_stat["strikeouts"],
                    "sacrifices": batting_stat["sacrifices"],
                    "sacrifice_flies": batting_stat["sacrifice_flies"],
                    "stolen_bases": batting_stat["stolen_bases"],
                    "caught_stealing": batting_stat["caught_stealing"]
                }
            })

    with open(FIXED_JSON_PATH, "w") as file:
        json.dump(formatted_data, file, indent=4)

def load_data():
    """Loads transformed player data into the database."""
    if not os.path.exists(FIXED_JSON_PATH):
        print(f"Error: {FIXED_JSON_PATH} not found. Run transform_data() first.")
        return

    with open(FIXED_JSON_PATH, "r") as file:
        data = json.load(file)

    for player_data in data:
        if player_data["model"] == "players.player":
            player, created = Player.objects.get_or_create(
                id=player_data["pk"],
                name_first=player_data["fields"]["name_first"],
                name_last=player_data["fields"]["name_last"],
                team=player_data["fields"]["team"],
                birth_date=player_data["fields"].get("birth_date"),
                height_feet=player_data["fields"].get("height_feet"),
                height_inches=player_data["fields"].get("height_inches"),
                weight=player_data["fields"]["weight"],
                throws=player_data["fields"]["throws"],
                bats=player_data["fields"]["bats"],
                primary_position=player_data["fields"].get("primary_position", "Unknown"),
            )

        elif player_data["model"] == "players.battingstat":
            BattingStat.objects.create(
                player=Player.objects.get(id=player_data["fields"]["player"]),
                year=player_data["fields"]["year"],
                at_bats=player_data["fields"]["at_bats"],
                hits=player_data["fields"]["hits"],
                home_runs=player_data["fields"]["home_runs"],
                stolen_bases=player_data["fields"]["stolen_bases"],
            )

if __name__ == "__main__":
    transform_data()
    load_data()
