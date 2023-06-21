

def choose_from(options, required=False):
    caveat = ' or leave empty' if not required else ''
    input_message = f'Pick an option{caveat}:\n'

    user_input = ''
    valid = False

    for index, item in enumerate(options):
        input_message += f'{index + 1}) {item}\n'

    input_message += 'Your choice: '

    while user_input not in map(str, range(1, len(options) + 1)) and not valid:
        user_input = input(input_message)
        valid = ~required or user_input

    return options[int(user_input) - 1] if user_input else None


def provide_value(required=False):
    caveat = ' or leave empty' if not required else ''
    input_message = f'Provide a value{caveat}:\n'

    user_input = ''
    valid = False

    while not user_input and not valid:
        user_input = input(input_message)
        valid = ~required or user_input

    return user_input
