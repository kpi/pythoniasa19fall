"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():
    lib = [
    'This is the farmer sowing his corn,',
    "That kept the cock that crowed in the morn,",
    'That waked the priest all shaven and shorn,',
    "That married the man all tattered and torn,",
    'That kissed the maiden all forlorn,',
    "That milked the cow with the crumpled horn,",
    'That tossed the dog,',
    'That worried the cat,',
    'That killed the rat,',
    'That ate the malt',
    'That lay in the house that Jack built.'
    ]

    the_poem = ''
    for sentence in reversed(lib):
        the_poem += 'This is ' + sentence[sentence.find('the'): ] + '\n'
        if sentence != lib[-1]: the_poem += '\n'.join(lib[ lib.index(sentence)+1 : ]) + '\n'
        the_poem += '\n'

    the_poem = ''.join(the_poem[:-1])
    return the_poem


if __name__ == '__main__':
    import doctest
    doctest.testmod()

