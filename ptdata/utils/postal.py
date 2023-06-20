
import re

from ptdata import settings
from ptdata.utils import fancyprint as fp


def normalize(df, src_col):
    df[settings.CLEAN_CP7] = None
    df[settings.CLEAN_CP4] = None

    for i, row in df.iterrows():
        postal_code = row[src_col]
        clean_cp7, clean_cp4 = clean(postal_code)
        df.loc[i, settings.CLEAN_CP7] = clean_cp7
        df.loc[i, settings.CLEAN_CP4] = clean_cp4


def clean(value):
    parts = value.split(' ')
    cp7 = None
    cp4 = None
    cp3 = None

    for i, p in enumerate(parts):
        if re.match(r'\d{4}-\d{3}', p):
            cp7 = p
            cp4 = p[0:4]
            cp3 = p[5:8]
            break
        elif re.match(r'\d{4}', p):
            cp4 = p
        elif re.match(r'\d{3}', p):
            cp3 = p

    if not cp7 and cp4:
        if cp3 and re.match(r'\d{4}-\d{3}', f'{cp4}-{cp3}'):
            cp7 = f'{cp4}-{cp3}'
        else:
            fp.warning(f'Storing partial postal code {fp.fgy(cp4)}')

    if not cp4:
        fp.error(f'Cannot find a match for {fp.fgr(value)}')

    cp7 = cp7 if cp7 else None
    cp4 = cp4 if cp4 else None

    return cp7, cp4
