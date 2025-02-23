/**
 * File: index.js
 * Version: Pre-Production
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Entry point for React frontend.
 * - Imports Bootstrap and global styles.
 */

import React from "react";
import ReactDOM from "react-dom/client";

/* Import Bootstrap CSS */
import "bootstrap/dist/css/bootstrap.min.css";

/* (Optional) If you need Bootstrap JS for components like modals, dropdowns, etc. */
import "bootstrap/dist/js/bootstrap.bundle.min.js";

/* Import your global styles.css AFTER Bootstrap (to override if needed) */
import "./styles.css";

import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
