
import os

from .base import *

# Project root directory.
SRC_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Absolute directory paths.
TMP_DIR = os.path.join(SRC_DIR, TMP_DIR)
