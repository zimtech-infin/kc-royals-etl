/**
 * File: api.js
 * Version: Pre-Production (Fixed)
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Handles API requests for fetching player data.
 * - Ensures correct data retrieval with improved error handling.
 */

import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api";

/**
 * Fetches the list of all players.
 */
export const fetchPlayers = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/players/`);
    return response.data;
  } catch (error) {
    console.error("Failed to fetch players:", error);
    return [];
  }
};

/**
 * Fetches details for a single player by ID.
 */
export const fetchPlayerDetails = async (playerId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/players/${playerId}/`); // With trailing slash
    console.log("Fetched Player Details:", response.data);
    return response.data;
  } catch (error) {
    console.error(`Failed to fetch details for player ${playerId}:`, error);
    return null;
  }
};
