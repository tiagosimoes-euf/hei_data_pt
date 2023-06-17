
import json
from datetime import date

from ptdata import settings
from ptdata.utils import datalifecycle as dlc, fancyprint as fp, frames


def fetch(refresh=False):
    human_readable = 'Fetching data from ECHE API'
    fp.start(human_readable)

    filename = f'{settings.ECHEAPI_PREFIX}{settings.SEP}{str(date.today())}.csv'

    if refresh or not dlc.file_exists(filename):
        status, data, content_type = dlc.get(settings.ECHEAPI_URL)

        if status:
            decoded = json.loads(data)
            df_eche = frames.to_df(decoded)
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
