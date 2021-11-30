"""
Author : Mamoun Janfor
create a function named even that will take 2 int parameters, one for starting point and the other is a counter
return a list of counter smallest even int greater than or equal to starting point in ascending order
"""


def even(start, n):
    if start % 2 == 0:
        for i in range(0, n * 2, 2):
            print(i + start)
    else:
        start = start + 1
        for i in range(0, n * 2, 2):
            print(i + start)


if __name__ == '__main__':
    a = int(input("enter a starting point: "))
    b = int(input("enter a counter: "))
    d = even(a, b)
    print(d)
