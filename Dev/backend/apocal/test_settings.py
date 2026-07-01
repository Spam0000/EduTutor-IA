"""
Settings for the local pytest suite.

The application keeps PostgreSQL as its runtime database in settings.py. Tests
run against SQLite so contributors can execute them without a Docker/Postgres
service available on the host machine.
"""

from .settings import *  # noqa: F401,F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "test.sqlite3",  # noqa: F405
    }
}

