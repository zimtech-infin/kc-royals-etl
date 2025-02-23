/**
 * File: App.js
 * Version: Pre-Production
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Includes routes for Home, Login, Register, and now PlayerDetailPage.
 */

import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import Navbar from "./components/Navbar";
import { AuthProvider } from "./context/AuthContext";
import { PlayerProvider } from "./context/PlayerContext";
import Home from "./pages/Home";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import PlayerDetailPage from "./pages/PlayerDetailPage"; // <--- Import new detail page

function App() {
  return (
    <AuthProvider>
      <PlayerProvider>
        <Router>
          <Navbar />
          <main className="container mt-3">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/login" element={<LoginPage />} />
              <Route path="/register" element={<RegisterPage />} />
              {/* Route for player details: /players/:id */}
              <Route path="/players/:id" element={<PlayerDetailPage />} />
              <Route path="*" element={<Navigate to="/" />} />
            </Routes>
          </main>
        </Router>
      </PlayerProvider>
    </AuthProvider>
  );
}

export default App;
