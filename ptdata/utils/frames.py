
import pandas as pd


def dicts_to_df(dict_list):
    df = pd.DataFrame.from_dict(dict_list)

    return df


def tuples_to_df(tuples_list, columns):
    df = pd.DataFrame.from_records(tuples_list, columns=columns)

    return df


def concat(df_list):
    df = pd.concat(df_list, ignore_index=True)

    return df


def from_html(table, header=0, extract_links='all'):
    dfs = pd.read_html(
        str(table),
        flavor='bs4',
        header=header,
        extract_links=extract_links,
    )

    df = dfs[0]

    return df


def from_csv(filename):
    df = pd.read_csv(filename)

    return df
