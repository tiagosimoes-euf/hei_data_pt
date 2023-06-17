
import re

from ptdata import settings
from ptdata.utils import fancyprint as fp


def normalize(df, src_col):
    df[settings.CLEAN_POSTAL] = None

    for i, row in df.iterrows():
        postal_code = row[src_col]
        clean_postal_code = clean(postal_code)
        df.loc[i, settings.CLEAN_POSTAL] = clean_postal_code


def clean(value):
    parts = value.split(' ')
    match = None
    cp4 = None
    cp3 = None

    for i, p in enumerate(parts):
        if re.match(r'\d{4}-\d{3}', p):
            match = p
            break
        elif re.match(r'\d{4}', p):
            cp4 = p
        elif re.match(r'\d{3}', p):
            cp3 = p

    if not match and cp4:
        if cp3 and re.match(r'\d{4}-\d{3}', f'{cp4}-{cp3}'):
            match = f'{cp4}-{cp3}'
        else:
            fp.warning(f'Storing partial postal code {fp.fgy(cp4)}')
            match = cp4

    if not match:
        fp.error(f'Cannot find a match for {fp.fgr(value)}')

    return match if match else None
