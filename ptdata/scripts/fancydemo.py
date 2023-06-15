
from ptdata.utils import fancyprint as fp


def main(*args):
    print()
    print('**************')
    print('* FancyPrint *')
    print('**************')
    print()

    print(fp.fancyformat('Style', prefix=True))

    print(fp.fancyformat('0 Neutral'))
    print(fp.fancyformat('1 Bold', style='1'))
    print(fp.fancyformat('2 Muted', style='2'))
    print(fp.fancyformat('3 Italic', style='3'))
    print(fp.fancyformat('4 Underline', style='4'))

    input('\nPress Enter to continue...')

    print()

    print(fp.fancyformat('Foreground color', prefix=True))

    print(fp.fancyformat('31 Red', fg='31'))
    print(fp.fancyformat('32 Green', fg='32'))
    print(fp.fancyformat('33 Yellow', fg='33'))
    print(fp.fancyformat('34 Blue', fg='34'))
    print(fp.fancyformat('35 Purple', fg='35'))
    print(fp.fancyformat('36 Cyan', fg='36'))
    print(fp.fancyformat('37 Light grey', fg='37'))

    input('\nPress Enter to continue...')

    print()

    print(fp.fancyformat('Background color', prefix=True))

    print(fp.fancyformat('41 Red', bg='41'))
    print(fp.fancyformat('42 Green', bg='42'))
    print(fp.fancyformat('43 Yellow', bg='43'))
    print(fp.fancyformat('44 Blue', bg='44'))
    print(fp.fancyformat('45 Purple', bg='45'))
    print(fp.fancyformat('46 Cyan', bg='46'))
    print(fp.fancyformat('47 Light grey', bg='47'))

    input('\nPress Enter to continue...')

    print()

    print(fp.fancyformat('Indent', prefix=True))

    fp.fancyoutput('No indent')
    fp.fancyoutput('1 space', indent=1)
    fp.fancyoutput('2 spaces', indent=2)
    fp.fancyoutput('3 spaces', indent=3)
    fp.fancyoutput('4 spaces', indent=4)

    input('\nPress Enter to continue...')

    print()

    print(fp.fancyformat('Utilities', prefix=True))

    fp.success('Display a success message.')
    fp.notice('Display a notice.')
    fp.warning('Display a warning.')
    fp.error('Display an error.')
    fp.info('Display information.')

    print()
