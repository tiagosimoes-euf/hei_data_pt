
from ptdata import settings
from ptdata.utils import db, fancyprint as fp, interact, unicode


def main(*args):
    df_eche = db.fetch(table=settings.ECHEAPI_PREFIX)
    df_verified = df_eche[settings.VERIFIED_REF].copy()

    for col in settings.VERIFIED_COLS:
        df_verified[col] = None

    df_dgeec = db.fetch(table=settings.DGEEC_PREFIX)

    df_match = db.fetch(table='match')

    for i, row in df_match.iterrows():
        verified_item = {}

        eche_id = row[settings.ECHEAPI_ID]
        df_eche_match = df_eche[df_eche[settings.ECHEAPI_ID] == eche_id]
        eche_match = df_eche_match.squeeze()
        eche_name = eche_match[settings.ECHEAPI_NAME]

        verified_item[settings.ECHEAPI_ID] = eche_id

        dgeec_id = row[settings.DGEEC_ID]
        df_dgeec_match = df_dgeec[df_dgeec[settings.DGEEC_ID] == dgeec_id]
        dgeec_match = df_dgeec_match.squeeze()
        dgeec_name = dgeec_match[settings.DGEEC_NAME]

        richest_name = unicode.compare_spelling(eche_name, dgeec_name)

        if richest_name:
            fp.success(f'Storing {fp.fgg(richest_name)} as {fp.sb(settings.ECHEAPI_NAME)} for {fp.fgg(eche_id)}')
            verified_item[settings.ECHEAPI_NAME] = richest_name
            verified_item[settings.ECHEAPI_NAME_LANG] = settings.DEFAULT_LANG
        else:
            fp.warning(f'ECHE has {fp.fgy(eche_name)} as legal name for {fp.fgy(eche_id)}')
            fp.info(f'How should {fp.fgb(dgeec_name)} be stored?')
            selected = interact.choose_from([
                settings.ECHEAPI_NAME,
                settings.ECHEAPI_DISPLAY,
            ])
            fp.notice(f'Storing {fp.fgc(dgeec_name)} as {fp.sb(selected)} for {fp.fgc(eche_id)}')
            verified_item[selected] = dgeec_name
            verified_item[f'{selected}Lang'] = settings.DEFAULT_LANG

        if settings.ECHEAPI_NAME in verified_item:
            map_verified(verified_item, dgeec_match)

        attach_verified(verified_item, df_verified)

    db.save(df_verified, 'verified')


def map_verified(item, row):
    item['street'] = row['morada']

    cp_parts = row['codigoPostal'].split(' ')

    item['postalCode'] = cp_parts[0]

    cp_city = ' '.join(cp_parts[1:])
    municipality = row['concelho']
    is_seat = cp_city.casefold() == municipality.casefold()
    city = municipality if is_seat else f'{cp_city.title()}, {municipality}'

    item['city'] = city

    item['cityLang'] = settings.DEFAULT_LANG

    item['webpage'] = row['website']


def attach_verified(item, df):
    item_id = item[settings.ECHEAPI_ID]
    df_match = df[df[settings.ECHEAPI_ID] == item_id]
    match = df_match.squeeze()
    index = match.name

    for key, value in item.items():
        df.loc[index, key] = value
