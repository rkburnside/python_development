__author__ = 'Rich'

import random
import math
import re   # module for regular expressions

# number objects
print len(str(2**10000))
print math.pi
print math.sqrt(1039)
print random.random()
print random.choice([1,'cool','stinky',2])

# string objects        # strings are immutable
S = 'spam'
print len(S)
print S[0]
print S[2]  # indexing
print S[-1] # negative indexing
print S[1:3]
print S[0:3]
print S[:3]
print S[:]
print S
print S + 'xyz'
print S
print S * 8
S = 'z' + S[1:]
print S
S = 'spam'
print S.find('pa')
S = S.replace('pa', 'xyz')
print S

line = 'aaa,bbb,ccccc,dd'
print line.split(',')
print S.upper()
print S
print S.isdigit()
line = 'aaa,bbb,ccccc,dd\n'
print line.rsplit()

print '%s, eggs, and %s' % ('spam', 'SPAM!')    # formatting method
print dir(S)
print help(S.replace)

# pattern matching
match = re.match('hello[ \t]*(.*)world', 'hello python world')
print match.group(1)

# lists - lists ARE mutable (unlike strings). method operations DO actually change lists
L = [123, 'spam', 1.23]
print len(L)
print L[0]
print L[:-1]
print L + [4, 5, 6]
print L.pop(2)
print L

M = ['bb', 'aa', 'cc']
print M
M.sort()
print M
M.reverse()
print M

# Bounds Checking (pg 206)