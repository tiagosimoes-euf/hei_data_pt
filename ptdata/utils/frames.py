
import pandas as pd


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
