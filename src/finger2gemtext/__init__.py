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
from .convert import finger_to_gemtext

##############################################################################
# Exports.
__all__ = ["finger_to_gemtext"]


### __init__.py ends here
