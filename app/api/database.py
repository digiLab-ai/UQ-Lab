import json
from pathlib import Path
import glob
import os

from . import settings


def validate_credentials(username, password):
    """
    Check if a login is valid
    """
    path = os.path.join(settings.RESOURCES_DIR, "users.json")
    with open(path) as f:
        data = json.load(f)
        return data.get(username) == password


def get_campaign_names(username):
    """
    Get a list of a single user's campaign names.
    """

    return [
        Path(os.path.basename(p)).stem
        for p in glob.glob(
            os.path.join(settings.RESOURCES_DIR, "campaigns", username, "*.csv")
        )
    ]
