/**
 * File: AuthButtons.js
 * Version: Pre-Production
 * Created by: K. Zimmerman
 * Project: kc_royals_backend
 * Description:
 * - Displays Login or Logout button based on authentication state.
 */

import React, { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { Link } from "react-router-dom";

const AuthButtons = () => {
  const { user, logout } = useContext(AuthContext);

  return user ? (
    <button className="btn btn-danger" onClick={logout}>
      Logout
    </button>
  ) : (
    <>
      <Link className="btn btn-light me-2" to="/login">
        Login
      </Link>
      <Link className="btn btn-light" to="/register">
        Register
      </Link>
    </>
  );
};

export default AuthButtons;
