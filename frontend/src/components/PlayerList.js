/**
 * File: PlayerList.js
 * Version: Fixed - v2.7
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Displays a list of players.
 * - Allows searching by name (filters removed).
 * - Each player card now routes to /players/:id for details.
 * - Ensures `players` state is properly managed.
 */

import React, { useContext, useState, useEffect } from "react";
import { PlayerContext } from "../context/PlayerContext";
import PlayerCard from "./PlayerCard";
import SearchBar from "./SearchBar";
import { Link } from "react-router-dom"; // Import Link

const PlayerList = () => {
  const { players = [] } = useContext(PlayerContext);
  const [searchQuery, setSearchQuery] = useState("");
  const [filteredPlayers, setFilteredPlayers] = useState(players);

  useEffect(() => {
    if (!players.length) return; // Prevent filtering if no players loaded

    const filtered = players.filter((player) =>
      `${player.name_first} ${player.name_last}`
        .toLowerCase()
        .includes(searchQuery.toLowerCase())
    );

    console.log("Filtered Players:", filtered); // Debugging

    setFilteredPlayers(filtered);
  }, [searchQuery, players]);

  const handleSearch = (query) => {
    setSearchQuery(query);
  };

  return (
    <div className="container mt-4">
      <SearchBar onSearch={handleSearch} />
      <div className="row">
        {filteredPlayers.length > 0 ? (
          filteredPlayers.map((player) => (
            <div key={player.id} className="col-md-4 mb-4">
              {/* Wrap the PlayerCard in a Link to /players/:id */}
              <Link
                to={`/players/${player.id}`}
                style={{ textDecoration: "none", color: "inherit" }}
              >
                <PlayerCard player={player} />
              </Link>
            </div>
          ))
        ) : (
          <p>No players found.</p>
        )}
      </div>
    </div>
  );
};

export default PlayerList;
