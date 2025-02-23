/**
 * File: routes.js
 * Version: Pre-Production
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Defines frontend routes using React Router.
 * - Routes include Home, Player Detail, Login, and Register.
 */

import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import PlayerDetailPage from "./pages/PlayerDetailPage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import Navbar from "./components/Navbar";

const AppRoutes = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/player/:id" element={<PlayerDetailPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
