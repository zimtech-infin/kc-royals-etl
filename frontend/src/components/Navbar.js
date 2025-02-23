/**
 * File: Navbar.js
 * Version: v2.1 - Revised
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Uses Bootstrap classes to align Login/Register on the right, no toggle or extras.
 * - Login button now links directly to Django Admin backend.
 */

import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

const Navbar = () => {
  const { user, logout } = useContext(AuthContext);

  return (
    <nav className="navbar px-3" style={{ backgroundColor: "#002f6c" }}>
      <div className="d-flex w-100 justify-content-between align-items-center">
        <Link className="navbar-brand fw-bold text-white" to="/">
          KC Royals
        </Link>
        <div>
          {user ? (
            <>
              <span className="text-white me-3">Hello, {user.username}</span>
              <button className="btn btn-danger" onClick={logout}>
                Logout
              </button>
            </>
          ) : (
            <>
              <a
                className="btn btn-light me-2"
                href="http://localhost:8000/admin/login/?next=/admin/"
              >
                Login
              </a>
            </>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
