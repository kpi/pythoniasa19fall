"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():
    list1 = ["This is ", "That "]
    list2 = ["lay in ", "ate ", "killed ", "worried ", "tossed ", "milked ", "kissed ",
             "married ", "waked ", "kept "]
    list3 = ["the house that Jack built.", "the malt", "the rat,", "the cat,", "the dog,",
             "the cow with the crumpled horn,", "the maiden all forlorn,", "the man all tattered and torn,",
             "the priest all shaven and shorn,", "the cock that crowed in the morn,", "the farmer sowing his corn,"]
    list=""
    for i in range(len(list3)):
        list+=list1[0] + list3[i]+"\n"
        for j in range(i - 1, -1, -1):
            list+=list1[1] + list2[j] + list3[j] +"\n"
        if i < len(list3)-1 :
            list+="\n"
    return list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
