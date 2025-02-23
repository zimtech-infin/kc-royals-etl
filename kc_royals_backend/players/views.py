"""
File: views.py
Created by: K. Zimmerman
Project: kc_royals_backend
Description:
- Defines API views for Player, BattingStat, and PitchingStat.
- Implements filtering, searching, and retrieval.
- Ensures PlayerDetailView correctly returns batting & pitching stats.
"""

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Player, BattingStat, PitchingStat
from .serializers import PlayerSerializer, BattingStatSerializer, PitchingStatSerializer


class PlayerListView(generics.ListAPIView):
    """GET: Lists all players with optional filtering."""
    serializer_class = PlayerSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["primary_position", "team"]
    search_fields = ["name_last", "name_first"]

    def get_queryset(self):
        """Ensures that only non-empty players are returned."""
        return Player.objects.exclude(name_first__isnull=True).exclude(name_last__isnull=True)


class PlayerDetailView(APIView):
    """GET: Retrieves a single player by ID, including batting & pitching stats."""

    permission_classes = [AllowAny]  # Allow public access

    def get(self, request, pk):
        player = get_object_or_404(Player.objects.prefetch_related("batting", "pitching"), pk=pk)
        player_data = PlayerSerializer(player).data

        # Fetch related batting and pitching stats
        batting_stats = player.batting.all()
        pitching_stats = player.pitching.all()

        player_data["stats"] = {
            "batting": BattingStatSerializer(batting_stats, many=True).data,
            "pitching": PitchingStatSerializer(pitching_stats, many=True).data,
        }

        return Response(player_data)


class PlayerCreateView(generics.CreateAPIView):
    """POST: Creates a new player (authentication required)."""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]


class BattingStatListView(generics.ListAPIView):
    """GET: Lists all batting stats with optional filtering."""
    serializer_class = BattingStatSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["year", "player"]
    search_fields = ["player__name_last", "player__name_first"]

    def get_queryset(self):
        """Optimize query performance with prefetching."""
        return BattingStat.objects.select_related("player")


class PitchingStatListView(generics.ListAPIView):
    """GET: Lists all pitching stats with optional filtering."""
    serializer_class = PitchingStatSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["year", "player"]
    search_fields = ["player__name_last", "player__name_first"]

    def get_queryset(self):
        """Optimize query performance with prefetching."""
        return PitchingStat.objects.select_related("player")
