"""Provides a simple finger to Gemtext converter."""

##############################################################################
# Python imports.
from collections.abc import Iterable

##############################################################################
# Local imports.
from .available_services import AvailableServicesFilter
from .finger_filter import FingerFilter
from .user_lists import UserListFilter


##############################################################################
def finger_to_gemtext(
    finger_content: str, additional_filters: Iterable[type[FingerFilter]] | None = None
) -> str:
    """Convert Finger content to Gemtext.

    Args:
        finger_content: The Finger content to convert.

    Returns:
        The converted Gemtext content.
    """
    filters: Iterable[type[FingerFilter]] = (
        UserListFilter,
        AvailableServicesFilter,
        *(additional_filters or ()),
    )
    for current_filter in (candidate() for candidate in filters):
        if current_filter.can_likely_convert(finger_content):
            return current_filter.to_gemtext(finger_content)
    return finger_content


### convert.py ends here
