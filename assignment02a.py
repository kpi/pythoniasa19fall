"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""


def poem():
    objects = ['house that Jack built.', 'malt', 'rat,', 'cat,', 'dog,', 'cow with the crumpled horn,',
               'maiden all forlorn,', 'man all tattered and torn,', 'priest all shaven and shorn,',
               'cock that crowed in the morn,', 'farmer sowing his corn,']
    actions = ['lay in', 'ate', 'killed', 'worried', 'tossed', 'milked', 'kissed', 'married', 'waked', 'kept']

    first_rows = ['This is the ' + obj for obj in objects]
    next_rows = [''] + ['That ' + act + ' the ' + obj for act, obj in zip(actions, objects)]

    result = [[first_row] + list(reversed(next_rows[:(i + 1)])) for i, first_row in enumerate(first_rows)]
    result[-1][-1] = ''

    from itertools import chain

    return '\n'.join(chain(*result))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
