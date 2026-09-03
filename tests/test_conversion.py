"""Test the finger to Gemtext conversion."""

##############################################################################
# Python imports.
from pathlib import Path

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Library imports.
from finger2gemtext.convert import finger_to_gemtext


##############################################################################
def _example(source: str, example_type: str) -> str:
    """Get the example data for a test.

    Args:
        source: The name of the source file (sans extension).
        example_type: The type of example data to get (e.g., "source", "expected").

    Returns:
        The contents of the example file.
    """
    return (
        Path(__file__).parent / "examples" / f"{source}.{example_type}.txt"
    ).read_text(encoding="utf-8")


##############################################################################
def example(name: str) -> tuple[str, str]:
    """Get the source and target data for a test.

    Args:
        name: The name of the source file (sans extension).

    Returns:
        A tuple containing the contents of the source and target files.
    """
    return _example(name, "source"), _example(name, "target")


##############################################################################
@mark.parametrize(
    "source, target",
    [
        ("", ""),
        ("This is a test.", "This is a test."),
        ("Login Name Login Time", "Login Name Login Time"),
        ("Login  Name  Login Time", "Login  Name  Login Time"),
        example("graph.no"),
        example("redterminal.org"),
        example("user-list"),
        example("tilde.club"),
        example("typed-hole.org"),
        example("not-available-services"),
    ],
)
def test_conversion(source: str, target: str) -> None:
    """Test that the input is unchanged."""
    assert finger_to_gemtext(source) == target


### test_conversion.py ends here
