# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Randomly generates a grid with 0s and 1s, whose dimension is controlled
# by user input, as well as the density of 1s in the grid, and finds out,
# for given step_number >= 1 and step_size >= 2, the number of stairs of
# step_number many steps, with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest
# step sizes, and for a given step size, from stairs with the smallest number
# of steps to stairs with the largest number of stairs.


from random import seed, randint
import sys
from collections import defaultdict
from collections import Counter
import time

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0))
                              for j in range(len(grid))
                             )
             )

try:
    arg_for_seed, density, dim = (int(x) for x in 
                        input('Enter three positive integers: ').split()
                                 )
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
time.sleep(0.001)

seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

# INSERT YOUR CODE HERE
#print(grid)
if dim%2==0:
    maxsize=int(dim/2)
else:
    maxsize=int((dim+1)/2)

for size in range(2,maxsize+1):
    #print('For steps of size {}, we have:'.format(size))
    d=defaultdict(int)
    i_min=size-1
    j_min=size*2-2
    for i in range(i_min,dim):
        for j in range(j_min,dim):
            
                flag=0
                for k in range(j+2-2*size,j+1-size+1):
                    if grid[i+1-size][k]==0:
                        flag=1
                for p in range(i+1-size,i+1):
                    if grid[p][j+1-size]==0:
                        flag=1
                for q in range(j+1-size,j+1):
                    if grid[i][q]==0:
                        flag=1
                if flag==0:
                    d[(i,j)]=d[(i+1-size,j+1-size)]+1
                    if d[(i+1-size,j+1-size)]!=0:
                        d[(i+1-size,j+1-size)]=0
    count=Counter(d.values()) 
    #print(d)
    #print(size,count)
    if d!={}:
        print()
        print('For steps of size {}, we have:'.format(size))
    s=sorted(count.keys())
    for k in s:
        if k!=0:
            #print(k)
            if k==1 and count[k]==1:
                print('     {} stair with {} step'.format(count[k],k)) 
            elif k==1:
                print('     {} stairs with {} step'.format(count[k],k))
            elif count[k]==1:
                print('     {} stair with {} steps'.format(count[k],k))
            else:
                print('     {} stairs with {} steps'.format(count[k],k))





                
    
