from argparse import ArgumentParser
from glob import glob
from os.path import expanduser
from platform import system
from sqlite3 import OperationalError, connect

# Import requests only for robust cookie handling with domain/path
try:
    import requests
except ModuleNotFoundError:
    requests = None

try:
    from instaloader import ConnectionException, Instaloader
except ModuleNotFoundError:
    raise SystemExit("Instaloader not found.\n  pip install [--user] instaloader")


def get_cookiefile():
    default_cookiefile = {
        "Windows": "~/AppData/Roaming/Mozilla/Firefox/Profiles/*/cookies.sqlite",
        "Darwin": "~/Library/Application Support/Firefox/Profiles/*/cookies.sqlite",
    }.get(system(), "~/.mozilla/firefox/*/cookies.sqlite")
    cookiefiles = glob(expanduser(default_cookiefile))
    if not cookiefiles:
        raise SystemExit("No Firefox cookies.sqlite file found. Use -c COOKIEFILE.")
    return cookiefiles[0]


def import_session(cookiefile, sessionfile):
    print("Using cookies from {}.".format(cookiefile))
    conn = connect(f"file:{cookiefile}?immutable=1", uri=True)
    # Read full cookie attributes for reliable domain/path matching
    try:
        cookie_data = conn.execute(
            "SELECT name, value, host, path, isSecure FROM moz_cookies WHERE baseDomain='instagram.com'"
        )
    except OperationalError:
        cookie_data = conn.execute(
            "SELECT name, value, host, path, isSecure FROM moz_cookies WHERE host LIKE '%instagram.com'"
        )

    instaloader = Instaloader(max_connection_attempts=1)

    # If requests is available, create proper cookies with domain/path; else fall back
    session_jar = instaloader.context._session.cookies
    found_names = set()
    try:
        rows = list(cookie_data)
    finally:
        conn.close()

    if requests is not None:
        for name, value, host, path, is_secure in rows:
            found_names.add(name)
            # Normalize host to ensure leading dot is acceptable for subdomains
            domain = host
            try:
                cookie = requests.cookies.create_cookie(
                    name=name,
                    value=value,
                    domain=domain,
                    path=path or "/",
                    secure=bool(is_secure),
                )
                session_jar.set_cookie(cookie)
            except Exception:
                # As a fallback, set without domain/path if create_cookie fails
                session_jar.set(name, value)
    else:
        # Fallback: behave like original implementation (name/value only)
        for name, value, *_ in rows:
            found_names.add(name)
            session_jar.set(name, value)

    # Basic sanity check: sessionid cookie is required for authenticated requests
    if "sessionid" not in found_names:
        raise SystemExit(
            "No Instagram session found in Firefox cookies.\n"
            "- Ensure you are logged in to Instagram in Firefox (not private mode).\n"
            "- Use the correct Firefox profile (run with -c to point to another cookies.sqlite).\n"
            "- Then rerun: python cookies.py"
        )

    username = instaloader.test_login()
    if not username:
        # Provide clearer guidance for common causes
        raise SystemExit(
            "Not logged in. Instagram rejected the cookies (HTTP 401).\n"
            "- Confirm you are currently logged in at https://www.instagram.com/ in Firefox.\n"
            "- If recently changed password or logged out sessions, re-login in Firefox and retry.\n"
            "- Consider updating 'instaloader' (pip install -U instaloader) if the issue persists."
        )

    print("Imported session cookie for {}.".format(username))
    instaloader.context.username = username
    instaloader.save_session_to_file(sessionfile)


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("-c", "--cookiefile")
    p.add_argument("-f", "--sessionfile")
    p.add_argument("--debug", action="store_true")
    args = p.parse_args()
    try:
        if args.debug:
            cf = args.cookiefile or get_cookiefile()
            print(f"[debug] Inspecting cookies in: {cf}")
            conn = connect(f"file:{cf}?immutable=1", uri=True)
            try:
                rows = list(
                    conn.execute(
                        "SELECT name, host, path, isSecure FROM moz_cookies WHERE baseDomain='instagram.com'"
                    )
                )
            except OperationalError:
                rows = list(
                    conn.execute(
                        "SELECT name, host, path, isSecure FROM moz_cookies WHERE host LIKE '%instagram.com'"
                    )
                )
            finally:
                conn.close()
            if not rows:
                print("[debug] No instagram.com cookies found in this profile.")
            else:
                print(f"[debug] Found {len(rows)} instagram.com cookies:")
                for name, host, path, secure in rows:
                    marker = " <== sessionid" if name == "sessionid" else ""
                    print(f"  - {name} @ {host}{path} secure={bool(secure)}{marker}")
        import_session(args.cookiefile or get_cookiefile(), args.sessionfile)
    except (ConnectionException, OperationalError) as e:
        raise SystemExit("Cookie import failed: {}".format(e))
