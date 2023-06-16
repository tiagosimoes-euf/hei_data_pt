
import os
import time
from datetime import date

import requests

from ptdata import settings
from ptdata.utils import fancyprint as fp


def get(url, path_args=None, params_dict=None):
    fp.info(fp.fgb('Fetching data from remote source...'))

    if path_args:
        url = '/'.join([url, *path_args])

    response = requests.get(url, params_dict)
    time.sleep(1)

    if response.status_code == requests.codes.ok:
        fp.success(f'GET {fp.fgg(response.url)}')
        fp.notice(f'Content type: {fp.fgc(response.headers["content-type"])}')
        status = True
    else:
        fp.error(f'GET {fp.fgr(response.url)}')
        fp.notice(f'Response status code: {fp.fgc(response.status_code)}')
        status = False

    return status, response.content, response.headers["content-type"]


def post(url, data_dict):
    fp.info(fp.fgb('Posting data to remote form...'))

    response = requests.post(url, data_dict)
    time.sleep(1)

    if response.status_code == requests.codes.ok:
        fp.success(f'POST {fp.fgg(response.url)}')
        fp.notice(f'Content type: {fp.fgc(response.headers["content-type"])}')
        status = True
    else:
        fp.error(f'POST {fp.fgr(response.url)}')
        fp.notice(f'Response status code: {fp.fgc(response.status_code)}')
        status = False

    return status, response.content, response.headers["content-type"]


def write_dated(bytes, source, filedate='', subset='index', ext='csv'):
    filedate = filedate if filedate else str(date.today())
    filename = f'{source}{settings.SEP}{filedate}{settings.SEP}{subset}.{ext}'

    write(bytes, filename)


def write(bytes, filename):
    fp.info(fp.fgb('Writing data to local file...'))

    filename = os.path.join(settings.TMP_DIR, filename)
    display_dirname = fp.sm(os.path.join(os.path.dirname(filename), ''))

    with open(filename, 'wb') as _file:
        _file.write(bytes)

    if not os.path.isfile(filename):
        display_basename = fp.fgr(os.path.basename(filename))
        fp.error(f'Could not write to {display_dirname}{display_basename}')
    else:
        display_basename = fp.fgg(os.path.basename(filename))
        fp.success(f'Saved file: {display_dirname}{display_basename}')


def read_dated(source, filedate='', subset='index', ext='html'):
    filedate = filedate if filedate else str(date.today())
    filename = f'{source}{settings.SEP}{date}{settings.SEP}{subset}.{ext}'

    return read(filename)


def read(filename):
    fp.info(fp.fgb('Reading data from local file...'))

    filename = os.path.join(settings.TMP_DIR, filename)
    try:
        with open(filename, 'r') as _file:
            content = _file.read()
    except IOError:
        fp.error(f'File not found: {filename}')
        return ''

    return content
