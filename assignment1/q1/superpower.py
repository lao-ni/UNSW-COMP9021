import sys
try:

    power=[int(x) for x in input("Please input the heroes' powers: ").split()]
    
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()

try:
    nb_of_swiches=int(input('Please input the number of power flips: '))
    if nb_of_swiches>len(power) or nb_of_swiches<0 :
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()

#print(power,nb_of_swiches) 

#frist
power1=power.copy()
for i  in range(nb_of_swiches):
    loc=power1.index(min(power1))
    power1[loc]=-power1[loc]
    
print('Possibly flipping the power of the same hero many times, the greatest achievable power is {}.'.format(sum(power1)))

#second
power2=power.copy()
power2.sort()
for i in range(nb_of_swiches):
    power2[i]=-power2[i]
    #print(power2)
print('Flipping the power of the same hero at most once, the greatest achievable power is {}.'.format(sum(power2)))
    
#third
power3=power.copy()
min_sum=sum(power3[0:nb_of_swiches])
for i in range(1,len(power3)-nb_of_swiches+1):
    if sum(power3[i:i+nb_of_swiches])<min_sum:
        min_sum=sum(power3[i:i+nb_of_swiches])
    
ans3=sum(power3)-2*min_sum
print('Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {}.'.format(ans3))

#fourth
power4=power.copy()
if len(power4)==1:
    ans4=power4[0]
else:

    for i in range(1,len(power4)):
        power4[i]=min(power4[i],power4[i]+power4[i-1])
        ans4=min(power4)
if ans4>0:
    ans4=0
res=sum(power)-2*ans4
print('Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {}.'.format(res))

