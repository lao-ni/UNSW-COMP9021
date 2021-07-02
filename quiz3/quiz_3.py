# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Call multibase a nonempty finite sequence of strictly positive
# integers (a_n, ..., a_0) all at most equal to 10.
# A positive integer is said to be a valid representation in the
# multibase if it is of the form x_k...x_0 with k <= n and for all
# i in {0,...,k}, x_i < a_i. Its representation in base 10 is defined as
# x_0 + x_1*a_0 + x_2*a_0*a_1 + ... + x_k*a_0*a_1*...*a_{k-1}.
#
# Determines the largest integer with a valid representation
# in the multibase, and converts representations between base
# 10 and the multibase.
#
# For instance, consider the multibase (8, 10, 6, 1).
# - 3820 is a valid representation in the multibase; it is the number
#   that in base 10 reads as 0 + 2*1 + 8*6*1 + 3*10*6*1 = 230.
# - 432, as a decimal number, can be represented in the multibase,
#   reading as 7200, since 2*6 + 7*10*6 = 432.

import sys

try: 
    multibase = [int(x) for x in input('Enter a nonempty sequence of integers '
                                        'between 1 and 10: '
                                      ).split()
                ]
    if not len(multibase) or any(b < 1 or b > 10 for b in multibase): 
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try: 
    input_multibase_representation =\
            int(input('Enter a first positive number: '))
    if input_multibase_representation < 0: 
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try: 
    input_base_10_representation =\
            int(input('Enter a second positive number: '))
    if input_base_10_representation < 0: 
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

valid_multibase_representation = True
valid_base_10_representation = True
max_number = 0
output_multibase_representation = 0
output_base_10_representation = 0

# INSERT YOUR CODE HERE
r_multibase=multibase[::-1]
for i in range(1,len(r_multibase)):
    r_multibase[i]=r_multibase[i]*r_multibase[i-1]
max_num_base=multibase[::-1]

for i in range(1,len(max_num_base)):
    max_number=(max_num_base[i]-1)*r_multibase[i-1]+max_number
max_number=max_number+max_num_base[0]-1
#print(max_num_base,r_multibase)

m1=multibase[::-1]
m2=[int(x) for x in str(input_multibase_representation)[::-1]]
if len(m2)>len(m1):
    valid_multibase_representation=False
else:
    for i in range(len(m2)) :
        if m2[i]>=m1[i]:
            valid_multibase_representation=False
            break
        else:
            if i==0:
                output_base_10_representation=output_base_10_representation+m2[0]
            elif i >0:
                output_base_10_representation=output_base_10_representation+m2[i]*r_multibase[i-1]


if input_base_10_representation > max_number:
    valid_base_10_representation=False
else:
    b=''
    num=input_base_10_representation
    for i in range(len(m1)):
        a=num//m1[i]
        #print(b,num % m1[i])
        b=str(num % m1[i])+b
        num=a
        #print(b,str(num % m1[i]))
    output_multibase_representation=int(b)







print('The largest number that can be represented in this multibase is:',
      max_number
     )
if not valid_multibase_representation:
    print(input_multibase_representation,
          'is not a valid representation in the given multibase.'
         )
else:
    print('In base 10,', input_multibase_representation,
          'reads as:', output_base_10_representation
         )
if not valid_base_10_representation:
    print(input_base_10_representation, 'cannot be represented in the '
          'given multibase.'
         )
else:
    print('In the given multibase,', input_base_10_representation,
          'reads as:', output_multibase_representation
         )





