"""Provides support code for working with user list responses."""

##############################################################################
# Python imports.
from re import Pattern, compile
from typing import Final

##############################################################################
_USER_LIST_HEADER: Final[Pattern[str]] = compile(r"^Login\s+Name\s+Login Time\s*$")
"""Regular expression to match the header of a user list in Finger output."""
_USER_ENTRY: Final[Pattern[str]] = compile(r"^(?P<username>\S+)\s{2,}.*$")
"""Regular expression to match a user entry in Finger output."""

##############################################################################
_PEEKABLE_LINES: Final[int] = 10
"""Number of lines to peek at when checking for a user list."""


##############################################################################
def looks_like_user_list(finger_content: str) -> bool:
    """Check if the Finger content looks like a user list.

    Args:
        finger_content: The Finger content to check.

    Returns:
        True if the content looks like a user list; False otherwise.
    """
    for line_number, line in enumerate(finger_content.splitlines()):
        if _USER_LIST_HEADER.match(line):
            return True
        if line_number > _PEEKABLE_LINES:
            break
    return False


##############################################################################
def convert_user_list_to_gemtext(finger_content: str) -> str:
    """Convert a Finger user list to Gemtext.

    Args:
        finger_content: The Finger content to convert.

    Returns:
        The converted Gemtext content.
    """
    gemtext_lines: list[str] = []
    gather = gemtext_lines.append
    converting = False
    found_users = False
    for line in finger_content.splitlines():
        if _USER_LIST_HEADER.match(line):
            gather(line)
            converting = True
            continue
        if converting and (user := _USER_ENTRY.match(line)) is not None:
            gather(f"=> /finger/{user.group('username')} {line}")
            found_users = True
        else:
            gather(line)
    gather("")
    return "\n".join(gemtext_lines) if found_users else finger_content


### _user_lists.py ends here
