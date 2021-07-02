# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

from collections import Counter
from random import seed, randrange, sample
import sys
from os import path


try: 
    for_seed, upper_bound, size =\
         (int(x) for x in input('Enter three nonnegative integers: ').split())
    if for_seed < 0 or upper_bound < 0 or size < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
w = len(str(upper_bound - 1))
with open('mapping.txt', 'w') as mapping:
    for (a, b) in zip(sorted(randrange(upper_bound) for _ in range(size)),
                      (randrange(upper_bound) for _ in range(size))
                     ):
        print(f'{a:{w}}', '->', b, file=mapping)                
print('Here is the mapping that has been generated:')
with open('mapping.txt') as mapping:
    for line in mapping:
        print(line, end='')
        
valid_mapping = True
most_frequent_inputs = []
function = {}

# INSERT YOUR CODE HERE
linelist=[]
left=[]
right=[]
with open('mapping.txt') as mapping:
    for line in mapping:
        if linelist and line in linelist:
            valid_mapping = False
            break
        else:
            linelist.append(line)
        line=line.split()
        left.append(int(line[0]))
        right.append(int(line[-1]))
    left_count=Counter(left)
    #print(left_count)
    max_count=0
    for k in left_count:
        if left_count[k]==1:
            #print(k)
            loc=left.index(k)
            function[k]=right[loc]
        
        if not most_frequent_inputs:
             most_frequent_inputs.append(k)
             max_count=left_count[k]
        else:
            if left_count[k]>max_count:
                most_frequent_inputs=[k]
                max_count=left_count[k]
            elif left_count[k]==max_count:
                most_frequent_inputs.append(k)




        
   
       


if not valid_mapping:
    print("Sorry, that's not a correct mapping.")
else:
    print("Ok, that's a correct mapping.")
    print('The list of most frequent inputs is:\n\t', most_frequent_inputs)
    print('The function extracted from the mapping is:\n\t', function)
