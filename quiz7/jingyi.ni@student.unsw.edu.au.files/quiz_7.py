# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left
#   corner,  so the largest region consisting of connected cells all
#   filled with 1s or all filled with 0s, depending on the value stored
#   in the top left corner;
# - the size of the largest area with a checkers pattern.


from random import seed, randint
import sys


dim = 10

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))

try:
    arg_for_seed, density = (int(x) for x in 
                    input('Enter two positive integers: ').split()
                            )
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[int(randint(0, density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()

# INSERT YOUR CODE HERE

#print(grid)
c=1
ones=[(0,0)]
points_used=[(0,0)]
flag=grid[0][0]
while ones:
    #print(ones)
    p=ones.pop()
    x,y=p[0],p[1]
    
    if x>=1 and grid[x-1][y]==flag and (x-1,y) not in points_used:
        ones.append((x-1,y))
        points_used.append((x-1,y))
        c+=1
    if y>=1 and grid[x][y-1]==flag and (x,y-1) not in points_used:
        ones.append((x,y-1))
        points_used.append((x,y-1))
        c+=1

    if x<=8 and grid[x+1][y]==flag and (x+1,y) not in points_used:
        ones.append((x+1,y))
        points_used.append((x+1,y))
        c+=1

    if y<=8 and grid[x][y+1]==flag and (x,y+1) not in points_used:
        ones.append((x,y+1))
        points_used.append((x,y+1))
        c+=1
print('The size of the largest homogenous region from the top left corner is {}.'.format(c))

m=1
u=[]
for i in range(10):
    for j in range(10):
        if (i,j) not in u:
            c=1
            ones=[(i,j)]
            points_used=[(i,j)]
            while ones:
                #print(ones)
                p=ones.pop()
                x,y=p[0],p[1]
                
                if x>=1 and grid[x][y]+grid[x-1][y]==1 and (x-1,y) not in points_used:
                    ones.append((x-1,y))
                    points_used.append((x-1,y))
                    c+=1
                if y>=1 and grid[x][y]+grid[x][y-1]==1 and (x,y-1) not in points_used:
                    ones.append((x,y-1))
                    points_used.append((x,y-1))
                    c+=1

                if x<=8 and grid[x][y]+grid[x+1][y]==1 and (x+1,y) not in points_used:
                    ones.append((x+1,y))
                    points_used.append((x+1,y))
                    c+=1

                if y<=8 and grid[x][y]+grid[x][y+1]==1 and (x,y+1) not in points_used:
                    ones.append((x,y+1))
                    points_used.append((x,y+1))
                    c+=1
            if c>m:
                u=u+points_used
                m=c
            
print('The size of the largest area with a checkers structure is {}.'.format(m))

