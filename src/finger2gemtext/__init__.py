"""A simple finger to Gemtext converter."""

##############################################################################
# Python imports.
from importlib.metadata import version

######################################################################
# Main library information.
__author__ = "Dave Pearson"
__copyright__ = "Copyright 2026, Dave Pearson"
__credits__ = ["Dave Pearson"]
__maintainer__ = "Dave Pearson"
__email__ = "davep@davep.org"
__version__: str = version("finger2gemtext")
__licence__ = "MIT"

##############################################################################
# Local imports.
from .available_services import AvailableServicesFilter
from .convert import finger_to_gemtext
from .finger_filter import FingerFilter
from .user_lists import UserListFilter

##############################################################################
# Exports.
__all__ = [
    "AvailableServicesFilter",
    "finger_to_gemtext",
    "FingerFilter",
    "UserListFilter",
]


### __init__.py ends here
