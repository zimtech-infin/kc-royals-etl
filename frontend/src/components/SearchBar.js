/**
 * File: SearchBar.js
 * Version: Fixed - v2.6
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Provides a search input field to refine player results by name.
 * - Team and Position filters have been fully removed.
 * - Implements debounce for better performance.
 */

import React, { useState, useEffect } from "react";

const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState("");

  useEffect(() => {
    const delayDebounce = setTimeout(() => {
      onSearch(query);
    }, 300); // Wait 300ms after last keystroke

    return () => clearTimeout(delayDebounce); // Cleanup function
  }, [query, onSearch]);

  return (
    <div className="d-flex flex-column gap-2">
      <input
        type="text"
        className="form-control"
        placeholder="Search by name..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
    </div>
  );
};

export default SearchBar;
