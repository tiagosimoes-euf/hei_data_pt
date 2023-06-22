
from ptdata import settings
from ptdata.utils import datalifecycle as dlc, db, fancyprint as fp


def main(*args):
    human_readable = 'Export verified data for ECHE'
    fp.start(human_readable)

    verified_fields = [
        *settings.VERIFIED_REF,
        *settings.VERIFIED_COLS,
    ]

    df_verified = db.fetch(fields=verified_fields, table='verified')
    df_verified.dropna(subset=settings.VERIFIED_COLS, how='all', inplace=True)

    df_verified_csv = df_verified.to_csv(index=False)
    dlc.write(df_verified_csv.encode(), 'verified.PT.csv')

    fp.end(human_readable)
