"""Provides support code for working with user list responses."""

##############################################################################
# Python imports.
from re import Pattern, compile
from typing import Final

##############################################################################
# Local imports.
from .finger_filter import FingerFilter

##############################################################################
_USER_LIST_HEADER: Final[Pattern[str]] = compile(r"^Login\s+Name\s+Login Time\s*$")
"""Regular expression to match the header of a user list in Finger output."""
_USER_ENTRY: Final[Pattern[str]] = compile(r"^(?P<username>\S+)\s{2,}.*$")
"""Regular expression to match a user entry in Finger output."""


##############################################################################
class UserListFilter(FingerFilter):
    """Filter for Finger user list responses."""

    def can_likely_convert(self, finger_content: str) -> bool:
        """Check if the filter can likely convert the given Finger content.

        Args:
            finger_content: The Finger content to check.

        Returns:
            [`True`][True] if the filter can likely convert the content;
                [`False`][False] otherwise.
        """
        return any(
            _USER_LIST_HEADER.match(line)
            for line in self.peekable_lines(finger_content)
        )

    def to_gemtext(self, finger_content: str) -> str:
        """Convert the given finger content to Gemtext.

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
                gather(f"=> {user.group('username')} {line}")
                found_users = True
            else:
                gather(line)
        gather("")
        return "\n".join(gemtext_lines) if found_users else finger_content


### _user_lists.py ends here
