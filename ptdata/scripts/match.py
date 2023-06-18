
from ptdata import settings
from ptdata.utils import db, fancyprint as fp, postal


def main(*args):
    human_readable = 'Matching DGEEC and ECHE data'
    fp.start(human_readable)

    df_hei = load_dgeec()
    df_eche = load_eche()

    df_match = df_eche[[
        'erasmusCodeNormalized',
        'postalCode',
        settings.CLEAN_POSTAL,
    ]].copy()

    for col in ['codigoEstabelecimento', 'codigoPostal']:
        df_match[col] = None

    total = len(df_match)
    matches = 0

    for i, row in df_hei.iterrows():
        match_value = row[settings.CLEAN_POSTAL]
        df_partial = df_match[df_match[settings.CLEAN_POSTAL] == match_value]

        if df_partial.empty:
            fp.error(f'No matches found for {fp.fgr(match_value)}')
        elif len(df_partial) > 1:
            fp.warning(f'Too many matches found for {fp.fgy(match_value)}')
            print(df_partial)
        else:
            fp.success(f'Found a match for {fp.fgg(match_value)}')
            matches += 1
            # row_match = df_partial.squeeze()

    if matches != total:
        fp.warning(f'Matched {fp.fgy(matches)} out of {fp.fgy(total)} entries')

    fp.end(human_readable)


def load_dgeec():
    human_readable = 'Processing postal codes in DGEEC data'
    fp.start(human_readable)

    dgeec_fields = [
        'nomeEstabelecimento',
        'depende',
        'codigoEstabelecimento',
        'codigoPostal',
        'concelho',
    ]

    df_dgeec = db.fetch(fields=dgeec_fields, table=settings.PRIMARY_PREFIX)
    df_hei = df_dgeec[df_dgeec['depende'].isnull()].copy()

    postal.normalize(df_hei, 'codigoPostal')
    report(df_hei)

    fp.end(human_readable)

    return df_hei


def load_eche():
    human_readable = 'Processing postal codes in ECHE data'
    fp.start(human_readable)

    eche_fields = [
        'organisationLegalName',
        'erasmusCodeNormalized',
        'postalCode',
        'city',
    ]

    df_eche = db.fetch(fields=eche_fields, table=settings.ECHEAPI_PREFIX)

    postal.normalize(df_eche, 'postalCode')
    report(df_eche)

    fp.end(human_readable)

    return df_eche


def report(df):
    df_issues = df[df[settings.CLEAN_POSTAL].str.len() != 8]
    if df_issues.empty:
        fp.success('Found valid postal codes for all entries')
    else:
        df_missing = df[df[settings.CLEAN_POSTAL].isnull()]
        if not df_missing.empty:
            fp.error(f'Missing {fp.fgr(len(df_missing))} postal codes')

        df_partial = df_issues[df_issues[settings.CLEAN_POSTAL].notnull()]
        if not df_partial.empty:
            fp.warning(f'Found {fp.fgy(len(df_partial))} partial postal codes')
