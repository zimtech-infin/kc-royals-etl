"""
File: permissions.py
Created by: K. Zimmerman
Project: kc_royals_backend
Description:
- Defines custom permissions for role-based access control.
- Allows only authenticated admin users to modify player data.
- General users can view data but cannot modify it.
"""

from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """Grants permission only to admin users."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff
