import os.path
import sys

from collections import defaultdict

# THE NAME OF THE FILE YOU WILL WORK WITH
cable_file= input('Please enter the name of the file you want to get data from: ')
if not os.path.exists(cable_file):
    print('Sorry, there is no such file.')
    sys.exit()

with open (cable_file) as f:
    #flag=0
    a=''
    for line in f.readlines():
        line=line.strip('\n')
        a=a+' '+line
    #print(a)   
    try:
        cable=[int(x) for x in a.split()]
        if len(cable)<2 or cable[0]<=0:
            raise ValueError
        else:
            for i in range(1,len(cable)):
                if cable[i]<=0 or cable[i]<=cable[i-1]:
                    raise ValueError
    except ValueError:
        #flag=1
        print('Sorry, input file does not store valid data.')
        sys.exit()
    #print(cable)
    
    #the length of the longest good ride
    max_count=1
    interval=cable[1]-cable[0]
    cur_count=1
    for i in range(1,len(cable)):
        if cable[i]-cable[i-1]==interval:
            cur_count+=1
            #print(cur_count,cable[i])
        else:
            if cur_count>max_count:
                max_count=cur_count
            interval=cable[i]-cable[i-1]
            cur_count=2
    if cur_count>max_count:
                max_count=cur_count
    if  max_count==len(cable):
        print('The ride is perfect!')
    else:
        print('The ride could be better...')
    print('The longest good ride has a length of: {}'.format(max_count-1))


    #how many pillars to remove to build a perfect ride from the remaining ones.
    if len(cable)==2:
        res=0
    else:
        dp = [{} for i in range(len(cable))]
        ans=0
        for i in range(1,len(cable)):
            for j in range(i):
                dis=cable[i]-cable[j]
                x=dp[j].get(dis,1)+1
                dp[i][dis]=x
            ans=max(ans,max(dp[i].values()))
        res=len(cable)-ans
    print('The minimal number of pillars to remove to build a perfect ride from the rest is: {}'.format(res))


