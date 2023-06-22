
from ptdata import settings
from ptdata.sources import dgeec, eche
from ptdata.utils import db, fancyprint as fp, frames, interact


def main(*args):
    df_dgeec = dgeec.load_for_match()
    df_eche = eche.load_for_match()

    matches = match_clean(df_dgeec, df_eche)
    columns = [
        settings.ECHEAPI_ID,
        settings.DGEEC_ID,
        'comments'
    ]
    df_match = frames.tuples_to_df(matches, columns=columns)

    db.save(df_match, 'match')


def match_clean(df_dgeec, df_eche):
    human_readable = 'Matching DGEEC and ECHE data'
    fp.start(human_readable)

    matches = []

    eche_fqdn = df_eche[settings.CLEAN_FQDN].to_list()
    eche_fqdn_dups = [f for f in eche_fqdn if eche_fqdn.count(f) > 1]
    eche_fqdn_dups = list(set(eche_fqdn_dups))

    for i, row in df_eche.iterrows():
        eche_name = row[settings.ECHEAPI_NAME]
        eche_code = row[settings.ECHEAPI_ID]
        eche_fqdn = row[settings.CLEAN_FQDN]
        eche_cp7 = row[settings.CLEAN_CP7]

        df_match_fqdn = df_dgeec[df_dgeec[settings.CLEAN_FQDN] == eche_fqdn]

        if len(df_match_fqdn) > 1:
            df_match_fqdn = df_match_fqdn[df_match_fqdn['depende'].isnull()].copy()

        if not df_match_fqdn.empty:
            if len(df_match_fqdn) == 1:
                msg = 'Automatically matched by FQDN'
                matches.append((eche_code, get_match_id(df_match_fqdn, eche_name), msg))
            else:
                fp.warning(f'Multiple matches for FQDN {fp.fgy(eche_fqdn)}')
                print(df_eche.loc[[i]][settings.ECHEAPI_DISPLAY_COLS])
                print(df_match_fqdn[settings.DGEEC_DISPLAY_COLS])

                options = df_match_fqdn[settings.DGEEC_ID].to_list()
                selected = interact.choose_from(options)

                if selected:
                    df_match_sel = df_match_fqdn[df_match_fqdn[settings.DGEEC_ID] == selected]
                    msg = 'Manually matched by FQDN'
                    matches.append((eche_code, get_match_id(df_match_sel, eche_name), msg))

        if eche_code not in [x for x, y, z in matches]:
            df_match_cp7 = df_dgeec[df_dgeec[settings.CLEAN_CP7] == eche_cp7]

            if len(df_match_cp7) > 1:
                df_match_cp7 = df_match_cp7[df_match_cp7['depende'].isnull()].copy()

            if not df_match_cp7.empty:
                if len(df_match_cp7) == 1:
                    msg = 'Automatically matched by postal code'
                    matches.append((eche_code, get_match_id(df_match_cp7, eche_name), msg))
                else:
                    fp.warning(f'Multiple matches for CP7 {fp.fgy(eche_cp7)}')
                    print(df_eche.loc[[i]][settings.ECHEAPI_DISPLAY_COLS])
                    print(df_match_cp7[settings.DGEEC_DISPLAY_COLS])

                    options = df_match_cp7[settings.DGEEC_ID].to_list()
                    selected = interact.choose_from(options)

                    if selected:
                        df_match_sel = df_match_cp7[df_match_cp7[settings.DGEEC_ID] == selected]
                        msg = 'Manually matched by postal code'
                        matches.append((eche_code, get_match_id(df_match_sel, eche_name), msg))

        if eche_code not in [x for x, y, z in matches]:
            fp.warning(f'Cannot match any data for {fp.fgy(eche_code)}')
            print(df_eche.loc[[i]][settings.ECHEAPI_DISPLAY_COLS])

            raw_value = interact.provide_value()
            value = int(raw_value) if raw_value.isdigit() else None
            if value and value in df_dgeec[settings.DGEEC_ID].to_list():
                df_match_value = df_dgeec[df_dgeec[settings.DGEEC_ID] == value]
                msg = 'Manually provided value'
                matches.append((eche_code, get_match_id(df_match_value, eche_name), msg))
            else:
                fp.error(f'No matches for {fp.fgr(eche_code)}')

    fp.notice(f'Matched {fp.fgc(len(matches))} out of {fp.fgc(len(df_eche))}')

    fp.end(human_readable)

    return matches


def get_match_id(df_match, eche_name):
    match = df_match.squeeze()
    dgeec_name = match[settings.DGEEC_NAME]
    fp.success(f'{fp.fgg(eche_name)} mapped to {fp.fgg(dgeec_name)}')

    return match[settings.DGEEC_ID]
