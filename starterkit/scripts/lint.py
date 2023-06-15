
import os
import subprocess

from starterkit import settings
from starterkit.utils import fancyprint as fp


def main(*args):
    os.chdir(settings.SRC_DIR)

    fp.info(f'Enforcing style with {fp.fgb("Flake8")}')
    subprocess.run(['flake8'])

    fp.info(f'Sorting imports with {fp.fgb("isort")}')
    subprocess.run(['isort', '--apply'])
