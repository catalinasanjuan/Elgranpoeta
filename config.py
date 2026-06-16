
import os
from urllib.parse import urlparse, unquote

# Prefer a single connection URL when available (Railway provides MYSQL_URL).
# If MYSQL_URL is present, parse it and build db_config accordingly.
# Otherwise, read the individual MYSQL_* env vars. Do NOT fall back to localhost.

_mysql_url = os.getenv("MYSQL_URL")

if _mysql_url:
    _p = urlparse(_mysql_url)
    _user = unquote(_p.username) if _p.username else os.getenv("MYSQL_USER")
    _password = unquote(_p.password) if _p.password else os.getenv("MYSQL_PASSWORD")
    _host = _p.hostname
    _port = _p.port
    _database = _p.path.lstrip('/') if _p.path else os.getenv("MYSQL_DATABASE")
else:
    _user = os.getenv("MYSQL_USER")
    _password = os.getenv("MYSQL_PASSWORD")
    _host = os.getenv("MYSQL_HOST")
    _database = os.getenv("MYSQL_DATABASE")
    _port = int(os.getenv("MYSQL_PORT")) if os.getenv("MYSQL_PORT") else None

# Build db_config for mysql.connector. Do not set "localhost" as a default.
db_config = {
    "user": _user,
    "password": _password,
    "host": _host,
    "database": _database,
}

if _port:
    try:
        db_config["port"] = int(_port)
    except Exception:
        pass

# Temporary debug prints to verify Railway env at runtime
print("DB HOST:", db_config.get("host"))
print("DB USER:", db_config.get("user"))
print("DB DATABASE:", db_config.get("database"))
print("DB PORT:", db_config.get("port"))
