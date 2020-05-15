
def task1(start=2000,end=3200):
    """
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence
    on a single line.
    """
    # todo: write your code here
    print(','.join(str(i) for i in range(start, end + 1) if i % 7 == 0 and i % 5 != 0))


def task2(rows=3, cols=5):
    """
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
    The element value in the i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1,¡­Y-1.

    Example:
    Suppose the following inputs are given to the program: 3, 5.
    Then, the output of the program should be:
    >>> task2(3, 5)
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    """
    # todo: write your code here
    return [[ i*j for i in range(cols)] for j in range(rows)]




def task3(password):
    """
    A website requires the users to input username and password to register.
    Write a program to check the validity of password input by users.

    Following are the criteria for checking the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    3. At least 1 letter between [A-Z]
    4. At least 1 character from [$#@]
    5. Minimum length of transaction password: 6
    6. Maximum length of transaction password: 12

    Your program should accept a password and will check them according to the above criteria.

    Example:
    If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345
    Then, the output of the program should be:

    >>> task3('ABd1234@1')
    True
    >>> task3('a F1#')
    False
    >>> task3('2w3E*')
    False
    >>> task3('2We3345')
    False
    """
    # todo: write your code here
    return (6 <= len(password) <= 12
          and any('a' <= s <= 'z' for s in password)
          and any('A' <= s <= 'Z' for s in password)
          and any('0' <= s <= '9' for s in password)
          and any(s in '#$@' for s in password))
print(task3('ABd1234@1'))
print(task3('a F1#'))
print(task3('2w3E*'))
print(task3('2We3345'))

import random
import string

def task4(n):
    """
    Write password generator function that uses the same rules as in Task 3.
    The password generator function must be able to generate all possible correct passwords.
    """
    # todo: write your code here
    char = '$@#'
    pass_gen = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + char) for i in range(n))
    print(pass_gen)
task4(10)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
