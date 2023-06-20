
from ptdata import settings
from ptdata.sources import dgeec, eche
from ptdata.utils import datalifecycle as dlc, db, fancyprint as fp, frames


def main(*args):
    human_readable = 'Fetching data from all available sources'
    fp.start(human_readable)

    dgeec_filename = dgeec.fetch()
    eche_filename = eche.fetch()

    if not dgeec_filename or not eche_filename:
        fp.error('Missing data')
    else:
        fp.success('All source data is available')

        df_dgeec = frames.from_csv(dlc.tmp_path(dgeec_filename))
        dgeec.normalize(df_dgeec)
        db.save(df_dgeec, settings.DGEEC_PREFIX)

        df_eche = frames.from_csv(dlc.tmp_path(eche_filename))
        db.save(df_eche, settings.ECHEAPI_PREFIX)

    fp.end(human_readable)
