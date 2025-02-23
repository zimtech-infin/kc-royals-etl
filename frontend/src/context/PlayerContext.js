/**
 * File: PlayerContext.js
 * Version: Pre-Production
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Fixes issue where React context was not triggering updates.
 * - Ensures state updates are detected by React.
 */

import { createContext, useState, useEffect } from "react";
import { fetchPlayers } from "../api/api";

export const PlayerContext = createContext();

export const PlayerProvider = ({ children }) => {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    fetchPlayers()
      .then((data) => {
        console.log("Fetched players:", data.length); // Debugging log
        setPlayers([...data]); // Spreading ensures React detects state change
      })
      .catch((error) => console.error("Error fetching players:", error));
  }, []);

  return (
    <PlayerContext.Provider value={{ players, setPlayers }}>
      {children}
    </PlayerContext.Provider>
  );
};
