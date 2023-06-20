
import os

from .base import *

try:
    from .local import *
except ImportError:
    print('WARNING: Could not import local settings.')

# Project root directory.
SRC_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Absolute directory paths.
TMP_DIR = os.path.join(SRC_DIR, TMP_DIR)
