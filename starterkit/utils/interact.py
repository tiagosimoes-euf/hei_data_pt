

def choose_from(options):
    user_input = ''

    input_message = 'Pick an option:\n'

    for index, item in enumerate(options):
        input_message += f'{index + 1}) {item}\n'

    input_message += 'Your choice: '

    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)

    return options[int(user_input) - 1]


def provide_value(required=False):
    caveat = ' or leave empty' if not required else ''
    input_message = f'Provide a value{caveat}:\n'

    user_input = ''
    valid = False

    while not user_input and not valid:
        user_input = input(input_message)
        valid = ~required or user_input

    return user_input
