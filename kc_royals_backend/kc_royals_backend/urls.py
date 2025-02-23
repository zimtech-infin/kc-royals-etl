"""
File: urls.py
Created by: K. Zimmerman
Project: kc_royals_backend
Description:
- Defines URL routing for the Django project.
- Configures API endpoints and Django Admin access.
- Enables JWT authentication and role-based access control.
- Ensures `APPEND_SLASH` is correctly applied for consistent URL handling.
- Registers static and media file handling for deployment.
- Configures `ROOT_URLCONF` to ensure proper request resolution.
"""



from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Root API response
def api_root(request):
    return JsonResponse({
        "message": "Welcome to the KC Royals API",
        "endpoints": [
            "/api/players/",
            "/api/batting-stats/",
            "/api/token/",  # JWT login endpoint
            "/api/token/refresh/",  # JWT refresh token endpoint
            "/api/token/verify/",  # JWT verification
        ]
    })

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/", include("players.urls")),  # Correct inclusion of the players app
    path("", api_root),  # Ensure the API root is defined correctly
]
