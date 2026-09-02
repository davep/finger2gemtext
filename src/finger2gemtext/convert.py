"""Provides a simple finger to Gemtext converter."""

##############################################################################
# Local imports.
from ._user_lists import convert_user_list_to_gemtext, looks_like_user_list


##############################################################################
def finger_to_gemtext(finger_content: str) -> str:
    """Convert Finger content to Gemtext.

    Args:
        finger_content: The Finger content to convert.

    Returns:
        The converted Gemtext content.
    """
    return (
        convert_user_list_to_gemtext(finger_content)
        if looks_like_user_list(finger_content)
        else finger_content
    )


### convert.py ends here
