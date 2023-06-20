
from datetime import date

from bs4 import BeautifulSoup, Comment

from ptdata import settings
from ptdata.utils import datalifecycle as dlc, fancyprint as fp, frames


def check_updated():
    params = {settings.DGEEC_UPDATED_PARAM: 1}
    status, data, content_type = dlc.get(settings.DGEEC_BASEURL, params_dict=params)

    if status:
        updated_date = settings.DGEEC_UPDATED_EXPECTED

        soup = BeautifulSoup(data.decode(), features="html.parser")

        comment = soup.find(text=lambda t: isinstance(t, Comment))
        comment.extract()

        content = soup.get_text()

        for line in content.splitlines():
            if settings.DGEEC_UPDATED_GREP in line:
                parts = line.split(' ')

                if parts[-1] == updated_date:
                    fp.success('Updated date matches the expected value')
                else:
                    fp.warning('Updated date does not match expected value')
                    updated_date = parts[-1]
    else:
        fp.error('Cannot verify the updated date')

    return updated_date


def fetch(refresh=False):
    human_readable = 'Fetching data from DGEEC'
    fp.start(human_readable)

    up_to_date = settings.DGEEC_UPDATED_EXPECTED == check_updated()
    filedate = settings.DGEEC_UPDATED_EXPECTED if up_to_date else str(date.today())
    filename = f'{settings.DGEEC_PREFIX}{settings.SEP}{filedate}.csv'

    if refresh or not up_to_date or not dlc.file_exists(dlc.tmp_path(filename)):
        fp.warning('Refreshing data, this may take a while...')

        data_dict = {
            'nome': None,
            'tipo': -1,
            'distrito': -1,
            'dependencia': -1,
            'search': 'Pesquisar'
        }

        url = f'{settings.DGEEC_BASEURL}{settings.DGEEC_PAGED_SUFFIX}'
        soup = fetch_page(url, 0, data_dict)

        content = soup.get_text()

        max_index = None

        for line in content.splitlines():
            if settings.DGEEC_PAGED_GREP in line:
                parts = line.split(' ')
                max_index = int(parts[0]) // 15

        if max_index:
            paged_data = []

            for i in range(0, max_index + 1):
                soup = fetch_page(url, i, data_dict)
                list = soup.find("div", {"id": "list"})
                table = list.table
                df_page = frames.from_html(table)

                clean_links(df_page)
                df_page.rename(columns=settings.DGEEC_PAGED_TO_DF, inplace=True)
                expand(df_page)

                paged_data.append(df_page)

            df_dgeec = frames.concat(paged_data)
            df_dgeec_csv = df_dgeec.to_csv(index=False)
            dlc.write(df_dgeec_csv.encode(), filename)
            fp.success(f'{fp.fgg("DGEEC")} data has been retrieved')
    else:
        fp.success(f'{fp.fgg("DGEEC")} data is available and up to date')

    fp.end(human_readable)

    return filename


def fetch_page(url, page, data_dict):
    status, data, content_type = dlc.post(f'{url}{str(page)}', data_dict=data_dict)

    soup = BeautifulSoup(data.decode(), features="html.parser")

    comment = soup.find(text=lambda t: isinstance(t, Comment))
    comment.extract()

    return soup


def clean_links(df):
    clean_headers = {(h, l): h for h, l in df.columns.to_list()}
    df.rename(columns=clean_headers, inplace=True)

    df['link'] = None

    for i, row in df.iterrows():
        for j, col in enumerate(df.columns.to_list()):
            if col != 'link':
                _value, _link = row[col]
                df.loc[i, col] = _value
                if j == 0:
                    df.loc[i, 'link'] = f'{settings.DGEEC_BASEURL}{_link[2:]}'


def expand(df):
    paged_columns = settings.DGEEC_PAGED_TO_DF.values()
    result_columns = settings.DGEEC_RESULT_TO_DF.values()
    new_columns = [c for c in result_columns if c not in paged_columns]

    for c in new_columns:
        df[c] = None

    for i, row in df.iterrows():
        _link = row['link']

        status, data, content_type = dlc.get(_link)
        soup = BeautifulSoup(data.decode(), features="html.parser")
        list = soup.find("div", {"id": "record"})
        table = list.table

        df_raw = frames.from_html(table, header=None, extract_links=None)
        df_record = df_raw.transpose(copy=True)
        headers = df_record.iloc[0].values
        df_record.columns = headers
        df_record.drop(index=0, axis=0, inplace=True)
        df_record.rename(columns=settings.DGEEC_RESULT_TO_DF, inplace=True)

        record = df_record.reset_index(drop=True).squeeze()
        for c in new_columns:
            df.loc[i, c] = record[c]


def normalize(df):
    df.replace({'': None}, inplace=True)
    df.replace({'--': None}, inplace=True)

    phone_cols = [
        'telefone',
        'outroTelefone',
        'fax',
        'outroFax',
    ]

    for col in phone_cols:
        df[col] = df[col].map(lambda x: phone_format(x))

    _sep = ';'
    _first = 'telefone'
    _second = 'outroTelefone'

    for i, row in df.iterrows():
        _first_val = row[_first] if row[_first] else ''
        if _sep in _first_val and not row[_second]:
            numbers = row[_first].split(_sep)
            df.loc[i, _first] = numbers[0]
            df.loc[i, _second] = numbers[1]


def phone_format(arg):
    arg = str(arg) if arg else ''
    arg = ''.join(arg.split(' ')).strip()
    arg = arg if arg else None

    return arg
