
from bs4 import BeautifulSoup, Comment

from ptdata import settings
from ptdata.utils import datalifecycle as dlc, fancyprint as fp


def fetch():
    params = {settings.PRIMARY_UPDATED_PARAM: 1}
    status, data, content_type = dlc.get(settings.PRIMARY_BASEURL, params_dict=params)

    if status:
        soup = BeautifulSoup(data.decode(), features="html.parser")

        comment = soup.find(text=lambda t: isinstance(t, Comment))
        comment.extract()

        content = soup.get_text()

        for line in content.splitlines():
            if settings.PRIMARY_UPDATED_GREP in line:
                parts = line.split(' ')

                if parts[-1] == settings.PRIMARY_UPDATED_EXPECTED:
                    fp.success('Updated date matches the expected value')
                else:
                    fp.error('Updated date does not match expected value')
                break
