# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n
#   is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together
#   with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing
# the standard form decomposition of the permutation into cycles
# (see wikepedia page on permutations for details).
# - A given cycle starts with the largest value in the cycle.
# - Cycles are given from smallest first value to largest first value.
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix
# and in-place uses.


class PermutationError(Exception):
    pass


class Permutation:
    def __init__(self, *args, length=None):
        if length==None:
            if len(args)==0:
                self.p=()
                self.length=0
            else:
                if isinstance(args,tuple) and all(n in range(1,len(args)+1) for n in args):
                    self.p=args
                    self.length=len(args)
                else:
                    raise PermutationError('Cannot generate permutation from these arguments')
        elif length<0:
            raise PermutationError('Cannot generate permutation from these arguments')
        else:
            if len(args)==0:
                self.p=tuple(range(1,length+1))
                self.length=length
            else:
                if length==len(args) and isinstance(args,tuple) and all(n in range(1,len(args)+1) for n in args):
                    self.p=args
                    self.length=len(args)
                else:
                    raise PermutationError('Cannot generate permutation from these arguments')
        dic={}
        
        if self.p==():
            self.nb_of_cycles=0
        else:
            for i in range(len(self.p)):
                dic[i+1]=self.p[i]
              
            
            display=[]
            count=0
            while dic:
                st=max(dic)
                end=dic[st]
                if st==end:
                    curr=[st]
                else:
                    curr=[st,end]
                dic.pop(st)
                count+=1
                while curr[0]!=end:
                    st,end=end,dic[end]
                    dic.pop(st)
                    if  curr[0]!=end:
                        curr.append(end)
                display.append(curr)
            
            self.nb_of_cycles=count
            display=display[::-1]
            s=''
            for i  in range(len(display)):
                display[i]=tuple(display[i])
            for n in display:
                s=s+str(n)
            s = s.replace(',','')
            self.display=s     
                          
        # Replace pass above with your code

    def __len__(self):
        return len(self.p)
        # Replace pass above with your code

    def __repr__(self):
        return f'Permutation{self.p}'
        # Replace pass above with your code

    def __str__(self):
        if self.p==():
            return '()'
        else:
            return f'{self.display}'
           
        # Replace pass above with your code

    def __mul__(self, permutation):
        if self.length!=permutation.length:
            raise PermutationError('Cannot compose permutations of different lengths')
        else:
            l=[0]*self.length
            d1={}
            d2={}
            for i in range(len(self.p)):
                
                d1[i+1]=self.p[i]
            for i in range(len(permutation.p)):
                
                d2[i+1]=permutation.p[i]
            for i in range(len(l)):
                l[i]=d2[d1[i+1]]
            new_args=tuple(l)
            return  Permutation(*new_args)
        # Replace pass above with your code

    def __imul__(self, permutation):
        if self.length!=permutation.length:
            raise PermutationError('Cannot compose permutations of different lengths')
        else:
            l=[0]*self.length
            d1={}
            d2={}
            for i in range(len(self.p)):
                
                d1[i+1]=self.p[i]
            for i in range(len(permutation.p)):
                
                d2[i+1]=permutation.p[i]
            for i in range(len(l)):
                l[i]=d2[d1[i+1]]
            self.p=tuple(l)
            return  Permutation(*self.p)
        # Replace pass above with your code

    def inverse(self):
        d={}
        for i in range(len(self.p)):
                
                d[i+1]=self.p[i]
        d={value:key for key, value in d.items()}
        l=[0]*self.length
        for i in range(len(l)):
            l[i]=d[i+1]
        new_args=tuple(l)
        return  Permutation(*new_args)
        # Replace pass above with your code
        
    # Insert helper functions, if needed



                
        
