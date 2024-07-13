from enum import Enum
from typing import Callable

# Define the enums
class PrintMode(Enum):
    LINE_MODE = 1
    VERBOSE_MODE = 2
    PARAGRAPH_MODE = 3
    CUSTOM_MODE = 4

class PriSec(Enum):
    PRIMARY = 1
    SECONDARY = 2

# Utility functions to convert enums to strings
def as_string_print_mode(val: PrintMode) -> str:
    if val == PrintMode.LINE_MODE:
        return "LINE_MODE"
    elif val == PrintMode.VERBOSE_MODE:
        return "VERBOSE_MODE"
    elif val == PrintMode.PARAGRAPH_MODE:
        return "PARAGRAPH_MODE"
    elif val == PrintMode.CUSTOM_MODE:
        return "CUSTOM_MODE"
    else:
        return "???"

def as_string_pri_sec(val: PriSec) -> str:
    if val == PriSec.PRIMARY:
        return "PRIMARY"
    elif val == PriSec.SECONDARY:
        return "SECONDARY"
    else:
        return "???"

# Operator overloading for printing enums
def print_enum(enum_val) -> str:
    if isinstance(enum_val, PrintMode):
        return as_string_print_mode(enum_val)
    elif isinstance(enum_val, PriSec):
        return as_string_pri_sec(enum_val)
    else:
        return "???"



# Example usage of the enums and utility functions
print(print_enum(PrintMode.LINE_MODE))       # Output: LINE_MODE
print(print_enum(PrintMode.VERBOSE_MODE))    # Output: VERBOSE_MODE
print(print_enum(PriSec.PRIMARY))            # Output: PRIMARY
print(print_enum(PriSec.SECONDARY))          # Output: SECONDARY
