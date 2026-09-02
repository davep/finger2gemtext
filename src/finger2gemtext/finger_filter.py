"""Provides the base finger filter class."""

##############################################################################
# Python imports.
from abc import ABC, abstractmethod
from collections.abc import Iterator


##############################################################################
class FingerFilter(ABC):
    """Base class for finger filters."""

    def __init__(self, peekable_lines: int = 10) -> None:
        """Initialise the filter class.

        Args:
            peekable_lines: The number of lines to peek at when deciding the content type.
        """
        self._peekable_lines = max(1, peekable_lines)
        """The number of lines to peek at when deciding the content type."""

    def peekable_lines(self, finger_content: str) -> Iterator[str]:
        """The number of lines to peek at when deciding the content type."""
        for line_number, line in enumerate(finger_content.splitlines()):
            if line_number >= self._peekable_lines:
                break
            yield line

    @abstractmethod
    def can_likely_convert(self, finger_content: str) -> bool:
        """Check if the filter can likely convert the given Finger content.

        Args:
            finger_content: The Finger content to check.

        Returns:
            True if the filter can likely convert the content; False otherwise.
        """

    def to_gemtext(self, finger_content: str) -> str:
        """Convert the given finger content to Gemtext.

        Args:
            finger_content: The Finger content to convert.

        Returns:
            The converted Gemtext content.
        """
        return finger_content


### finger_filter.py ends here
