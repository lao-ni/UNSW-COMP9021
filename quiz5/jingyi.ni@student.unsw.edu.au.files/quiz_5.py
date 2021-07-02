# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Uses National Data on the relative frequency of given names in the
# population of U.S. births, stored in a directory "names", in files
# named "yobxxxx.txt with xxxx (the year of birth)
# ranging from 1880 to 2018.
# The "names" directory is a subdirectory if the working directory.
# Prompts the user for a male first name, and finds out the years
# when this name was most popular in terms of ranking amongst male names.
# Displays the ranking, and the years in decreasing order of frequency,
# computed, for a given year, as the count of the name for the year
# divided by the sum of the counts of all male names for the year.

import os
from collections import defaultdict
import csv
from pathlib import Path
from time import sleep

cwd = Path.cwd()
possible_path_1 = cwd.parent.parent / 'names'
possible_path_2 = Path(cwd.root) / 'course' / 'data' / 'names'
if possible_path_1.exists():
    # FOR ME
    path = possible_path_1
elif possible_path_2.exists():
    # FOR ED
    path = possible_path_2
else:
    # FOR YOU, names IS A SUBDIRECTORY OF THE WORKING DIRECTORY
    path = Path('names')

# INSERT YOUR CODE HERE
names_dirname = path
if not names_dirname.exists():
    print(f'There is no directory named {names_dirname}, giving up...')
    sys.exit()
# A dictionnary where a key is a name and a value is the list of all
# years when the name was given.
years_per_name = defaultdict(list)
year_count={}
for filename in sorted(names_dirname.glob('*.txt')):
    year = int(filename.name[3 : 7])
    
    with open(filename) as file:
        csv_file = csv.reader(file)
        #count_ratio={}
        count_sum=0
        rank=0
        for name, gender, count in csv_file:
            if gender=='M':
                rank+=1
                years_per_name[name].append([year,rank,int(count)])
                #count_ratio[name]=count
                count_sum += int(count)
        year_count[year]=count_sum               
        

input_name=input('Enter a male first name: ')

if input_name not in years_per_name:
    print(input_name,'is not a male first name in my records.')
else:
    year_and_rank=years_per_name[input_name]
    year_and_rank=sorted(year_and_rank,key=lambda x: x[1])
    #print(year_and_rank)
    rank=year_and_rank[0][1]
    
    year_list=[]
    for x in year_and_rank:
        if x[1]==rank:
            year_list.append([x[0],x[2]/(year_count[x[0]])])

        else:
            break
    year_list=sorted(year_list,key=lambda x: -x[1])
    print('By decreasing order of frequency, {} was most popular in the following years:'.format(input_name))
    num=0
    for x in year_list:
        num+=1
        if num%5==1:
            print(f'{x[0]:8}', end='')
        else:
            print(f'{x[0]:5}', end='')
        if num%5==0:
            print()
         
    print()
    print('Its rank was {} then.'.format(rank))




