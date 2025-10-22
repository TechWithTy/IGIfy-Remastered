from __future__ import annotations

import os
from typing import Optional, Tuple

from instagrapi import Client


def create_client(
    username: str,
    password: str,
    session_path: Optional[str] = None,
    proxy: Optional[str] = None,
    delay_range: Tuple[int, int] = (2, 5),
    request_timeout: int = 10,
) -> Client:
    """
    Create and configure an instagrapi Client with optional session loading.

    - Loads settings from `session_path` if provided and exists.
    - Applies proxy, delay_range, and request timeout.
    - Attempts login-by-session if `session_path` contains a valid sessionid (settings JSON),
      falls back to standard login with username/password.

    Returns a logged-in Client.
    """
    cl = Client()

    # Pacing / timeouts first
    try:
        cl.delay_range = (int(delay_range[0]), int(delay_range[1]))
    except Exception:
        pass
    try:
        cl.request_timeout = int(request_timeout)
    except Exception:
        pass

    if proxy:
        try:
            cl.set_proxy(proxy)
        except Exception:
            pass

    # Load settings if available
    if session_path and os.path.exists(session_path):
        try:
            cl.load_settings(session_path)
        except Exception:
            # Ignore loading failures; proceed to login
            pass

    # Login (reuses cookies/settings if available)
    cl.login(username, password)

    # Persist settings for stability
    try:
        # If caller provided a path, reuse it; else fallback to local file
        out_path = session_path or os.path.join(os.path.dirname(__file__), "..", "igfi_session.json")
        cl.dump_settings(os.path.abspath(out_path))
    except Exception:
        pass

    return cl

