/**
 * File: StatsChart.js
 * Version: Pre-Production
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Displays player stats using Chart.js.
 */

import React, { useEffect, useState } from "react";
import { fetchPlayerDetails } from "../api/api";
import { Bar } from "react-chartjs-2";

const StatsChart = ({ playerId }) => {
  const [player, setPlayer] = useState(null);

  useEffect(() => {
    fetchPlayerDetails(playerId).then(setPlayer);
  }, [playerId]);

  if (!player) return <p>Loading...</p>;

  const data = {
    labels: ["Games", "Hits", "Home Runs", "Stolen Bases"],
    datasets: [
      {
        label: `${player.first_name} ${player.last_name} Stats`,
        data: [
          player.stats.games,
          player.stats.hits,
          player.stats.home_runs,
          player.stats.stolen_bases,
        ],
        backgroundColor: ["#002F6C", "#C4A000", "#002F6C", "#C4A000"],
      },
    ],
  };

  return <Bar data={data} />;
};

export default StatsChart;
