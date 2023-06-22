
import json
from datetime import date

from ptdata import settings
from ptdata.utils import datalifecycle as dlc, db, fancyprint as fp, frames, postal, url


def fetch(refresh=False):
    human_readable = 'Fetching data from ECHE API'
    fp.start(human_readable)

    filename = f'{settings.ECHEAPI_PREFIX}{settings.SEP}{str(date.today())}.csv'

    if refresh or not dlc.file_exists(dlc.tmp_path(filename)):
        status, data, content_type = dlc.get(settings.ECHEAPI_URL)

        if status:
            decoded = json.loads(data)
            df_eche = frames.dicts_to_df(decoded)
            df_eche_csv = df_eche.to_csv(index=False)
            dlc.write(df_eche_csv.encode(), filename)
            fp.success(f'{fp.fgg("ECHE")} data has been retrieved')
        else:
            fp.error(f'{fp.fgr("ECHE")} data is not available')
            filename = None
    else:
        fp.success(f'{fp.fgg("ECHE")} data is available and up to date')

    fp.end(human_readable)

    return filename


def load_for_match():
    human_readable = 'Loading ECHE data for matching'
    fp.start(human_readable)

    eche_fields = [
        'organisationLegalName',
        'erasmusCodeNormalized',
        'postalCode',
        'webpage',
    ]

    df_eche = db.fetch(fields=eche_fields, table=settings.ECHEAPI_PREFIX)
    df_eche = df_eche[eche_fields].copy()

    postal.normalize(df_eche, 'postalCode')
    url.normalize(df_eche, 'webpage')
    db.save(df_eche, table='match_eche')

    fp.end(human_readable)

    return df_eche
