__author__ = 'Rich'

import sys

# import myfile
from myfile import title
import threenames

print(sys.platform)
print(2**100)
# hello = input()
# print hello

# print 'input something: '
# print input()

print title

print threenames.a + threenames.b + threenames.c
print threenames.a, threenames.b, threenames.c
print dir(threenames)

