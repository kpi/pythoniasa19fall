"""
Assignment 1-A
==============

Write function that generates the text below; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

>>> print(poem())
This is the house that Jack built.
---
This is the malt
That lay in the house that Jack built.
---
This is the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cock that crowed in the morn,
That waked the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the farmer sowing his corn,
That kept the cock that crowed in the morn,
That waked the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
<BLANKLINE>
"""


def poem():
    objects = ['house that Jack built.', 'malt', 'rat,', 'cat,', 'dog,', 'cow with the crumpled horn,',
               'maiden all forlorn,', 'man all tattered and torn,', 'priest all shaven and shorn,',
               'cock that crowed in the morn,', 'farmer sowing his corn,']
    actions = ['lay in', 'ate', 'killed', 'worried', 'tossed', 'milked', 'kissed', 'married', 'waked', 'kept']

    first_rows = ['This is the ' + obj for obj in objects]
    next_rows = ['---'] + ['That ' + act + ' the ' + obj for act, obj in zip(actions, objects)]

    result = [[first_row] + list(reversed(next_rows[:(i + 1)])) for i, first_row in enumerate(first_rows)]
    result[-1][-1] = ''

    from itertools import chain

    return '\n'.join(chain(*result))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
