/**
 * File: AuthContext.js
 * Version: Pre-Production
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Provides authentication state and methods for login/logout.
 */

import { createContext, useState } from "react";
import { login, logout } from "../api/auth";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  const handleLogin = async (credentials) => {
    const userData = await login(credentials.username, credentials.password);
    setUser(userData);
  };

  const handleLogout = () => {
    logout();
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{ user, login: handleLogin, logout: handleLogout }}
    >
      {children}
    </AuthContext.Provider>
  );
};
