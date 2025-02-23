/**
 * File: auth.js
 * Version: Pre-Production
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Handles authentication API requests (Login, Logout, Register).
 */

import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api";

export const login = async (username, password) => {
  const response = await axios.post(`${API_BASE_URL}/token/`, {
    username,
    password,
  });
  sessionStorage.setItem("token", response.data.access);
  return response.data;
};

export const logout = () => {
  sessionStorage.removeItem("token");
};

export const register = async (username, password) => {
  const response = await axios.post(`${API_BASE_URL}/register/`, {
    username,
    password,
  });
  return response.data;
};
