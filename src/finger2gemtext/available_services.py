"""Provides support code for working with available-services-type responses."""

##############################################################################
# Python imports.
from re import Pattern, compile
from typing import Final

##############################################################################
# Local imports.
from .finger_filter import FingerFilter

##############################################################################
_TELL: Final[str] = "available fingers"
"""String to look for in the Finger content to identify available services responses."""
_SERVICE: Final[Pattern[str]] = compile(r"^(?P<name>\S+?):?\s{2,}.*$")


##############################################################################
class AvailableServicesFilter(FingerFilter):
    """Filter for Finger available services responses."""

    def __init__(self, peekable_lines: int = 20) -> None:
        """Initialise the filter class.

        Args:
            peekable_lines: The number of lines to peek at when deciding the content type.
        """
        super().__init__(peekable_lines)

    def can_likely_convert(self, finger_content: str) -> bool:
        """Check if the filter can likely convert the given Finger content.

        Args:
            finger_content: The Finger content to check.

        Returns:
            [`True`][True] if the filter can likely convert the content;
                [`False`][False] otherwise.
        """
        return any(
            _TELL in line.lower() for line in self.peekable_lines(finger_content)
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
        found_services = False
        for line in finger_content.splitlines():
            if _TELL in line.lower():
                gather(line)
                converting = True
                continue
            if converting and (service := _SERVICE.match(line)) is not None:
                gather(f"=> /finger/{service['name']} {line}")
                found_services = True
            else:
                gather(line)
        gather("")
        return "\n".join(gemtext_lines) if found_services else finger_content


### _available_services.py ends here
