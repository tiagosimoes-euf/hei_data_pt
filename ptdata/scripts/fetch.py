
from ptdata.sources import dgeec
from ptdata.utils import fancyprint as fp


def main(*args):
    human_readable = 'Fetching data from all available sources'
    fp.start(human_readable)

    dgeec.fetch()

    fp.end(human_readable)
