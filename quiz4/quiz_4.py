# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Generates a list L of random positive integers, at least one
# of which is strictly positive, and prints out:
# - a list "fractions" of strings of the form 'a/b' such that:
#   . a <= b,
#   . a*n and b*n both occur in L for some n, and
#   . a/b is in reduced form
# enumerated from smallest fraction to largest fraction
#  (0 and 1 are exceptions, being represented as such rather than as
# 0/1 and 1/1);
# - if "fractions" contains 1/2, then the fact that 1/2 belongs to "fractions";
# - otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
#  if that member is unique;
# - otherwise, the two members "closest_1" and "closest_2" of "fractions" that
# are closest to 1/2, in their natural order.


import sys
from random import seed, randint
from math import gcd
from fractions import Fraction
from time import sleep

try:
    arg_for_seed, length, max_value = (int(x) for x in
                      input('Enter three nonnegative integers: ').split()
                                      )
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

sleep(0.01)
seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
num=[]
spot_on, closest_1, closest_2 = [None] * 3

# INSERT YOUR CODE HERE
if len(L)==1:
    fractions.append(str(L[0]))
    closest_1='1'
else:
    L.sort()
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            a=L[i]
            b=L[j]
            if b !=0:
                c=gcd(a,b)
                if a/b not in num:
                    if a/b==0:
                        fractions.append('0')
                        num.append(0)
                    elif a/b==1:
                        fractions.append('1')
                        num.append(1)
                    else:
                        fractions.append( str(a//c)+'/'+str(b//c))
                        num.append(a/b)
    if '1' not in fractions:
        fractions.append('1')
    fractions.sort(key = lambda x: Fraction(x))

    if '1/2' in fractions:
        spot_on='1/2'
    else:
        dis=1

        for x in fractions:
            if abs(0.5-Fraction(x))<dis:
                dis=abs(0.5-Fraction(x))
                closest_1=x
                closest_2=None
            elif abs(0.5-Fraction(x))==dis:
                closest_2=x

print('\nThe fractions no greater than 1 that can be built from L, '
      'from smallest to largest, are:'
     )
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')
