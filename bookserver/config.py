# ************************************
# |docname| - BookServer configuration
# ************************************
# Configure settings here.
# Default provided here may be `overridden by environment variables <https://fastapi.tiangolo.com/advanced/settings/>`_.
#
#
# Imports
# =======
# These are listed in the order prescribed by `PEP 8`_.
#
# Standard library
# ----------------
from pathlib import Path

# Third-party imports
# -------------------
from pydantic import BaseSettings

# Local application imports
# -------------------------
# None.


# Settings
# ========
class Settings(BaseSettings):
    # Pydantic provides a wonderful utility to handle settings.  The beauty of it
    # is that you can specify variables with or without default values, and Pydantic
    # will check your environment variables, in a case insensitive way. So that
    # if you have PROD_DBURL set in the environment it will be set as the value
    # for prod_dburl in settings.
    # This is a really nice way to keep from
    # committing any data you want to keep private.

    google_ga: str = ""

    # Either ``development``, ``production``, or ``test``, per `this code <setting.dev_dburl>`.
    config: str = "development"  # production or test

    # `Database setup <setting.dev_dburl>`.
    prod_dburl: str = "sqlite:///./runestone.db"
    dev_dburl: str = "sqlite:///./runestone_dev.db"
    test_dburl: str = "sqlite:///./runestone_test.db"

    # Configure ads.
    adsenseid: str = ""
    num_banners: int = 0
    serve_ad: bool = False

    # :index:`docs to write`: **What's this?**
    library_path: str = "/Users/bmiller/Runestone"
    dbserver: str = "sqlite"

    # Specify the directory to serve books from.
    book_path: Path = Path(__file__).parents[1] / "books"

    secret: str = "supersecret"
    web2py_private_key: str


settings = Settings()