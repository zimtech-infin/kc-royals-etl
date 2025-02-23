/**
 * File: PlayerCard.js
 * Version: Pre-Production (Fixed)
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Displays individual player information in a Bootstrap-styled card.
 * - Fixes missing player name and position issues.
 */

import React from "react";

const PlayerCard = ({ player }) => {
  return (
    <div className="card mb-3">
      <div className="card-body">
        <h5 className="card-title">
          {player.name_first} {player.name_last}{" "}
          {/* Ensure correct field names */}
        </h5>
        <p className="card-text">
          <strong>Position:</strong> {player.primary_position || "N/A"}
        </p>
        <p className="card-text">
          <strong>Team:</strong> {player.team}
        </p>
      </div>
    </div>
  );
};

export default PlayerCard;
