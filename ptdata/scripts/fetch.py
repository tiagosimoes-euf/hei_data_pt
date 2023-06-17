
from ptdata.sources import dgeec, eche
from ptdata.utils import fancyprint as fp


def main(*args):
    human_readable = 'Fetching data from all available sources'
    fp.start(human_readable)

    dgeec_filename = dgeec.fetch()
    eche_filename = eche.fetch()

    if dgeec_filename and eche_filename:
        fp.success('All source data is available')
    else:
        fp.error('Missing data')

    fp.end(human_readable)
