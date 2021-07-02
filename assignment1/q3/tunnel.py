import os.path
import sys
from collections import deque

tunnel_file= input('Please enter the name of the file you want to get data from: ')
if not os.path.exists(tunnel_file):
    print('Sorry, there is no such file.')
    sys.exit()

with open (tunnel_file) as f:
    two_line=[]
    for line in f:
        #print(line.strip()=='')
        if line.strip():
            two_line.append(line.strip())
    #print(two_line)
    try:
        if len(two_line)!=2:
            raise ValueError
        ceiling=[int(x) for x in two_line[0].strip().split()]
        floor=[int(x) for x in two_line[1].strip().split()]
        if len(ceiling)!=len(floor) or len(ceiling)<2 or len(floor)<2 :
            raise ValueError
        for i in range(len(floor)):
            if ceiling[i]<=floor[i]:
                raise ValueError

    except ValueError:
        print('Sorry, input file does not store valid data.')
        sys.exit()
    #print(ceiling,floor)

    #q1
    up=ceiling[0]
    down=floor[0]
   
    for i in range(1,len(floor)):
        if ceiling[i]<up:
            up=ceiling[i]
        if floor[i]>down:
            down=floor[i]
        if up<=down:
            break
    ans1=i
    print('From the west, one can into the tunnel over a distance of {}'.format(ans1))

    #q2
    ans2=0
    for i  in range(len(floor)):
        up=ceiling[i]
        down=floor[i]
   
        for j in range(i+1,len(floor)):
            if ceiling[j]<up:
                up=ceiling[j]
            if floor[j]>down:
                down=floor[j]
            if up<=down:
                break
        if j==len(floor)-1 and up>down:
            j=j+1

        res=j-i
        if res>ans2:
            ans2=res
    print('Inside the tunnel, one can into the tunnel over a maximum distance of {}'.format(ans2))
    
