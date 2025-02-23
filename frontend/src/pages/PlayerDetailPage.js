/**
 * File: PlayerDetailPage.js
 * Version: v2.1 - Fully Corrected
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Displays detailed player information.
 * - Ensures proper ID handling and navigation.
 * - Adds error handling for invalid player IDs.
 */

import React from "react";
import { useParams, Link } from "react-router-dom";
import PlayerDetail from "../components/PlayerDetail";

const PlayerDetailPage = () => {
  const { id } = useParams();
  const playerId = Number(id);

  if (isNaN(playerId) || playerId <= 0) {
    return (
      <div className="container mt-5">
        <Link to="/" className="btn btn-primary mb-3">
          Back to Players
        </Link>
        <div className="alert alert-danger">
          Invalid player ID. Please select a valid player.
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <Link to="/" className="btn btn-primary mb-3">
        Back to Players
      </Link>
      <PlayerDetail playerId={playerId} />
    </div>
  );
};

export default PlayerDetailPage;
