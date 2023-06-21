
from urllib.parse import urlparse

from ptdata import settings
from ptdata.utils import fancyprint as fp


def normalize(df, src_col):
    df[settings.CLEAN_FQDN] = None

    for i, row in df.iterrows():
        raw_url = row[src_col]
        fqdn = get_fqdn(raw_url)
        df.loc[i, settings.CLEAN_FQDN] = fqdn

    total_rows = len(df)
    total_fqdn = len(df[df[settings.CLEAN_FQDN].notnull()])

    fqdn_ratio = "{:.2%}".format(total_fqdn / total_rows)

    if total_fqdn == total_rows:
        fp.success(f'Found {fp.fgg(total_fqdn)} fully qualified domain names ({fp.fgg("100%")})')
    else:
        fp.warning(f'Found {fp.fgy(total_fqdn)} fully qualified domain names ({fp.fgy(fqdn_ratio)})')


def get_fqdn(url):
    item = str(url).lower()

    parts = item.split('//')
    if len(parts) == 1:
        parts = ['', *parts]

    item = '//'.join(parts)

    parsed = urlparse(item)
    fqdn = parsed.netloc

    # Remove common leading subdomains.
    parts = fqdn.split('.')
    parts_redux = [p.strip() for p in parts if p not in settings.SUBDOMAINS_TO_REMOVE]
    fqdn = '.'.join(list(dict.fromkeys(parts_redux)))

    # Invalidate if certain strings are present.
    for i in []:
        if fqdn.find(i) > -1:
            fqdn = ''

    # Purge hostnames left incomplete after cleaning.
    if len(fqdn.split('.')) < 2:
        fqdn = ''

    return fqdn if fqdn else None
