/**
 * File: PlayerDetail.js
 * Version: v2.2 - Fully Corrected
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Fixes incorrect stat key access.
 * - Ensures batting & pitching stats always render properly.
 * - Improves error handling and debugging.
 */

import React, { useEffect, useState } from "react";
import { fetchPlayerDetails } from "../api/api";

const PlayerDetail = ({ playerId }) => {
  const [player, setPlayer] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!playerId) return;

    fetchPlayerDetails(playerId)
      .then((data) => {
        if (!data || Object.keys(data).length === 0) {
          setError("Player not found.");
          return;
        }
        setPlayer(data);
      })
      .catch(() => setError("Error retrieving player details."));
  }, [playerId]);

  if (error) return <p className="text-danger">{error}</p>;
  if (!player) return <p>Loading...</p>;

  return (
    <div className="container mt-4">
      <h2>
        {player.name_first || "Unknown"} {player.name_last || ""}
      </h2>
      <p>
        <strong>Team:</strong> {player.team || "N/A"}
      </p>
      <p>
        <strong>Position:</strong> {player.primary_position || "N/A"}
      </p>
      <p>
        <strong>Birth Date:</strong> {player.birth_date ?? "N/A"}
      </p>
      <p>
        <strong>Throws:</strong> {player.throws ?? "N/A"}
      </p>
      <p>
        <strong>Bats:</strong> {player.bats ?? "N/A"}
      </p>

      <h3 className="mt-4">Batting Stats</h3>
      {player.stats?.batting?.length > 0 ? (
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Year</th>
              <th>League</th>
              <th>PA</th>
              <th>AB</th>
              <th>Hits</th>
              <th>HR</th>
              <th>SB</th>
            </tr>
          </thead>
          <tbody>
            {player.stats.batting.map((stat, index) => (
              <tr key={index}>
                <td>{stat.year || "N/A"}</td>
                <td>{stat.league || "N/A"}</td>
                <td>{stat.plate_appearances ?? 0}</td>
                <td>{stat.at_bats ?? 0}</td>
                <td>{stat.hits ?? 0}</td>
                <td>{stat.home_runs ?? 0}</td>
                <td>{stat.stolen_bases ?? 0}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p className="text-warning">No batting stats available.</p>
      )}

      <h3 className="mt-4">Pitching Stats</h3>
      {player.stats?.pitching?.length > 0 ? (
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Year</th>
              <th>League</th>
              <th>IP</th>
              <th>Wins</th>
              <th>Losses</th>
              <th>Strikeouts</th>
            </tr>
          </thead>
          <tbody>
            {player.stats.pitching.map((stat, index) => (
              <tr key={index}>
                <td>{stat.year || "N/A"}</td>
                <td>{stat.league || "N/A"}</td>
                <td>{stat.innings_pitched ?? 0}</td>
                <td>{stat.wins ?? 0}</td>
                <td>{stat.losses ?? 0}</td>
                <td>{stat.strikeouts ?? 0}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p className="text-warning">No pitching stats available.</p>
      )}
    </div>
  );
};

export default PlayerDetail;
