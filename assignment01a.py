"""
Assignment 1-A
==============

Update the Python script below to make it more compact and readable; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

"""

objects = ['house that Jack built.', 'malt', 'rat,', 'dog,', 'cow with the crumpled horn,', 'maiden all forlorn,',
           "man all tatter'd and torn,", 'priest all shaven and shorn,', "cock that crow'd in the morn,",
           'farmer sowing his corn,']
actions = ['lay in', 'ate', "kill'd", 'worried', "toss'd", "milk'd", 'kissed', 'married', 'waked', 'kept']

result = []
for i, obj in enumerate(objects):
    result.append(['This is ' + obj])
    if i != 0:
        result[i].append('That ' + actions[i-1] + ' the ' + objects[i-1])
    if i > 1:
        result[i] += result[i-1][1:]

for i in result:
    for j in i:
        print(j)
    print()
