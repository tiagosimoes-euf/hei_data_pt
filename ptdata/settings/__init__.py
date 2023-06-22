
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

# Aggregated field sets.
CLEAN_COLS = [
    CLEAN_CP4,
    CLEAN_CP7,
    CLEAN_FQDN,
]

DGEEC_DISPLAY_COLS = [
    DGEEC_NAME,
    DGEEC_ID,
    *CLEAN_FQDN,
]

ECHEAPI_DISPLAY_COLS = [
    ECHEAPI_NAME,
    ECHEAPI_ID,
    *CLEAN_FQDN,
]

# Reference columns for verified data.
VERIFIED_REF = [
    ECHEAPI_ID,
    ECHEAPI_PIC,
]

# ECHE API source name fields.
ECHEAPI_NAME_LANG = f'{ECHEAPI_NAME}Lang'
ECHEAPI_DISPLAY_LANG = f'{ECHEAPI_DISPLAY}Lang'
