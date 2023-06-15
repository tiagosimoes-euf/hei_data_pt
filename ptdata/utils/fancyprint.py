

# Styles for text.

def sb(arg):
    return fancyformat(str(arg), style='1')


def sm(arg):
    return fancyformat(str(arg), style='2')


def si(arg):
    return fancyformat(str(arg), style='3')


def su(arg):
    return fancyformat(str(arg), style='4')


# Foreground colors for text with optional style, bold by default.

def fgr(arg, style='1'):
    return fancyformat(str(arg), style=str(style), fg='31')


def fgg(arg, style='1'):
    return fancyformat(str(arg), style=str(style), fg='32')


def fgy(arg, style='1'):
    return fancyformat(str(arg), style=str(style), fg='33')


def fgb(arg, style='1'):
    return fancyformat(str(arg), style=str(style), fg='34')


def fgp(arg, style='1'):
    return fancyformat(str(arg), style=str(style), fg='35')


def fgc(arg, style='1'):
    return fancyformat(str(arg), style=str(style), fg='36')


# Utilities.

def error(msg):
    prefix = fancyformat('error', style='1', bg='41', prefix=True)
    fancyoutput(str(msg), prefix, 3)


def success(msg):
    prefix = fancyformat('success', style='1', bg='42', prefix=True)
    fancyoutput(str(msg), prefix, 1)


def warning(msg):
    prefix = fancyformat('warning', style='1', bg='43', prefix=True)
    fancyoutput(str(msg), prefix, 1)


def info(msg):
    prefix = fancyformat('info', style='1', bg='44', prefix=True)
    fancyoutput(str(msg), prefix, 4)


def notice(msg):
    prefix = fancyformat('notice', style='1', bg='46', prefix=True)
    fancyoutput(str(msg), prefix, 2)


def start(msg):
    prefix = fancyformat('start', style='2', prefix=True)
    fancyoutput(sm(str(msg)), prefix, 3)


def end(msg):
    prefix = fancyformat('end', style='2', prefix=True)
    fancyoutput(sm(str(msg)), prefix, 5)


def pause():
    input(fgp('   [pause] Press Enter to continue...'))


# Core funcionality.

def fancyformat(arg, style='0', fg='39', bg='49', prefix=False):
    style = f'{style};' if style and (fg or bg) else ''
    fg = f'{fg};' if fg and bg else ''

    if prefix:
        arg = f'[{arg}]'

    return f'\033[{style}{fg}{bg}m{arg}\033[0m'


def fancyoutput(content, prefix='', indent=0):
    space = ''

    if int(indent) > 0:
        for i in range(indent):
            space = f' {space}'

    prefix = f'{prefix} ' if prefix else ''

    print(f'{space}{prefix}{content}')
