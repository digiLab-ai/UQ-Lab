from pathlib import Path
import glob
import os

from . import settings


def get_exiting_campaigns():
    """
    Get a list of all exiting campaigns.
    """

    return [
        Path(os.path.basename(p)).stem
        for p in glob.glob(os.path.join(settings.RESOURCES_DIR, "campaigns", "*.csv"))
    ]
