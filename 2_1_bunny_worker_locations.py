"""
Bunny Worker Locations
======================

Keeping track of Commander Lambda's many bunny workers is starting to get tricky. You've been tasked with writing a program to match bunny worker IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the work areas have an unusual layout. They are stacked in a triangular shape, and the bunny workers are given numerical IDs starting from the corner, as follows:

| 7
| 4 8
| 2 5 9
| 1 3 6 10

Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground. 

For example, the bunny worker at (1, 1) has ID 1, the bunny worker at (3, 2) has ID 9, and the bunny worker at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been adding a LOT of workers). 

Write a function solution(x, y) which returns the worker ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the worker ID can be very large, return your solution as a string representation of the number.

>>> id_number_one_based(5, 10)
96

>>> id_number_one_based(3, 2)
9

>>> size = 10
>>> for y in range(1, size):
...    y = size - y
...    for x in range(1, size):
...        print('{:>4}'.format(id_number_one_based(x, y)), end='')
...    print()
  37  47  58  70  83  97 112 128 145
  29  38  48  59  71  84  98 113 129
  22  30  39  49  60  72  85  99 114
  16  23  31  40  50  61  73  86 100
  11  17  24  32  41  51  62  74  87
   7  12  18  25  33  42  52  63  75
   4   8  13  19  26  34  43  53  64
   2   5   9  14  20  27  35  44  54
   1   3   6  10  15  21  28  36  45
"""

def triangle_number(n):
    return n * (n + 1) // 2

def id_number_zero_based(x, y):
    level = x + y
    return triangle_number(level) + x

def id_number_one_based(x, y):
    return id_number_zero_based(x - 1, y - 1) + 1

def solution(x, y):
    return str(id_number_one_based(x, y))
