
from unidecode import unidecode


def compare_spelling(first, second):
    richest_spelling = None

    if first == second:
        return first

    if unidecode(first).casefold() == unidecode(second).casefold():
        if first.casefold() == unidecode(second).casefold():
            richest_spelling = second
        elif unidecode(first).casefold() == second.casefold():
            richest_spelling = first

    return richest_spelling
