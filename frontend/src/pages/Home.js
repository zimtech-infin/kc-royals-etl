/**
 * File: Home.js
 * Version: Pre-Production
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Displays hero section and player list.
 */

import React from "react";
import Hero from "../components/Hero";
import PlayerList from "../components/PlayerList";

const Home = () => {
  return (
    <div>
      <Hero />
      <div className="container mt-4">
        <h2 className="text-gold">MLB Players</h2>
        <p>Enter your favorite player's name in the search box.</p>
        <PlayerList />
      </div>
    </div>
  );
};

export default Home;
