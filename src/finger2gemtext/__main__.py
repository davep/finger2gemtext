##############################################################################
# Python imports.
import fileinput

##############################################################################
# Local imports.
from .convert import finger_to_gemtext


##############################################################################
def convert() -> None:
    """Parse the input from stdin or files and print the parsed Gemtext."""
    with fileinput.input() as finger_content:
        print(finger_to_gemtext("".join(finger_content)))


##############################################################################
if __name__ == "__main__":
    convert()


### __main__.py ends here
