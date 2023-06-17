
from ptdata import settings
from ptdata.utils import db, fancyprint as fp, postal


def main(*args):
    human_readable = 'Matching DGEEC and ECHE data'
    fp.start(human_readable)

    df_hei = load_dgeec()

    print(df_hei[df_hei[settings.CLEAN_POSTAL].str.len() != 8])

    df_eche = load_eche()

    print(df_eche[df_eche[settings.CLEAN_POSTAL].str.len() != 8])

    fp.end(human_readable)


def load_dgeec():
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

    return df_hei


def load_eche():
    eche_fields = [
        'organisationLegalName',
        'erasmusCodeNormalized',
        'postalCode',
        'city',
    ]

    df_eche = db.fetch(fields=eche_fields, table=settings.ECHEAPI_PREFIX)

    postal.normalize(df_eche, 'postalCode')

    return df_eche
