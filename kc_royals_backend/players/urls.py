"""
File: urls.py
Created by: K. Zimmerman
Project: kc_royals_backend
Description:
- Defines URL routing for the players API.
"""

from django.urls import path
from .views import (
    PlayerListView,
    PlayerCreateView,
    PlayerDetailView,
    BattingStatListView,
    PitchingStatListView,
)

urlpatterns = [
    path("players/", PlayerListView.as_view(), name="player-list"),
    path("players/manage/", PlayerCreateView.as_view(), name="player-create"),
    path("players/<int:pk>/", PlayerDetailView.as_view(), name="player-detail"),
    path("batting-stats/", BattingStatListView.as_view(), name="batting-stats"),
    path("pitching-stats/", PitchingStatListView.as_view(), name="pitching-stats"),
]
