import copy
def takeSecond(elem):
    return elem[0][1]
def removeblank(list):
    for i in list:
        while '' in i:
            i.remove('')
        while '\n' in i:
            i.remove('\n')
    while [] in list:
        list.remove([])
    return list
def findperiod(list):
    period=0
    for i in range(1,len(list[0])//2+1):
        found=True
        for line in list:
            for j in range(len(line)-i-1):
                if line[j]!=line[j+i]:
                    found=False
                    break
            if found==False:
                break
        if found==True:
            period=i
            break
    return period
class FriezeError(Exception):
    pass
class Frieze:
    def __init__(self,file):
        self.name=file[0:-4]
        self.frieze=[]
        data=open(file)
        line=data.readline()
        self.frieze.append([x for x in line.split(' ')])
        while line:
            line=data.readline()
            self.frieze.append([x for x in line.split(' ')])
        data.close()
        self.frieze=removeblank(self.frieze)
        self.data=[]
        for i in self.frieze:
            try:
                self.data.append([int(j) for j in i])
            except:
                raise FriezeError('Incorrect input')
        if len(self.data)<3 or len(self.data)>17:
            raise FriezeError('Incorrect input')
        elif len(self.data[0])<5 or len(self.data[0])>51:
            raise FriezeError('Incorrect input')
        for linedata in self.data:
            if len(linedata)!=len(self.data[0]):
                raise FriezeError('Incorrect input')
                for value in linedata:
                    if value not in [x for x in range(16)]:
                        raise FriezeError('Incorrect input')
        if self.data[0][-1]!=0:
            raise FriezeError('Input does not represent a frieze')
        for value in self.data[0]:
            if value not in [0,4,8,12]:
                raise FriezeError('Input does not represent a frieze')
        for linedata in self.data:
            if linedata[-1] not in [0,1]:
                raise FriezeError('Input does not represent a frieze')
        for value in self.data[-1]:
            if value not in [0,1,2,3,4,5,6,7]:
                raise FriezeError('Input does not represent a frieze')
        for i in range(len(self.data)):
            if self.data[i][0] in [1,3,5,7,9,11,13,15]:
                if self.data[i][-1]!=1:
                    raise FriezeError('Input does not represent a frieze')
            #elif self.data[i][0]==0 and self.data[i+1][0] not in [1,3,5,7,9,11,13,15]: #和课上讲的两头需要粘起来有关系
                #if self.data[i][-1]!=0:
                    #raise FriezeError('Input does raise not represent a frieze')
                #elif self.data[i][-2]==4 or self.data[i-1][-2]>8 or self.data[i+1][-2] in [3,6,10,7,15,11,14] or self.data[i+1][-1]==1:
                    #raise FriezeError('Input does raise not represent a frieze')
            #else:
                #if self.data[i][-2]!=4 and self.data[i-1][-2]<8 and self.data[i+1][-2] not in [3,6,10,7,15,11,14] and self.data[i+1][-1]!=1:
                    #raise FriezeError('Input does raise not represent a frieze')  
            for j in range(len(self.data[i])):
                    if self.data[i][j]>=8:
                        if self.data[i+1][j] in [2,3,6,7,10,11,14,15]:
                            raise FriezeError('Input does not represent a frieze')
        self.period=findperiod(self.data)
        if self.period<=1:
            raise FriezeError('Input does not represent a frieze')
        self.dict={}
        self.datacopy=copy.deepcopy(self.data)
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                direct=[]
                if self.datacopy[i][j]==0:
                    direct.append(0)
                if self.datacopy[i][j]>=8:
                    direct.append(8)
                    self.datacopy[i][j]-=8
                if self.datacopy[i][j]>=4:
                    direct.append(4)
                    self.datacopy[i][j]-=4
                if self.datacopy[i][j]>=2:
                    direct.append(2)
                    self.datacopy[i][j]-=2    
                if self.datacopy[i][j]==1:
                    direct.append(1)
                    self.datacopy[i][j]-=1
                self.dict[(j,i)]=direct
        self.rightline=[]
        for (x,y) in self.dict.keys():
            if 4 not in self.dict[(x,y)]:
                continue
            while 4 in self.dict[(x,y)]:
                if x-1<0:
                    start=(x,y)
                    self.dict[(x,y)].remove(4)
                    break 
                elif 4 not in self.dict[(x-1,y)]:
                    start=(x,y)
                    self.dict[(x,y)].remove(4)
                    break
                else:
                    x=x-1
            p=1
            while 4 in self.dict[(start[0]+p,start[1])]:
                self.dict[(start[0]+p,start[1])].remove(4)
                p=p+1
            self.rightline.append((start,(start[0]+p,start[1])))
        self.downline=[]
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                if 1 not in self.dict[(x,y)]:
                    continue
                while 1 in self.dict[(x,y)]:
                    if y+1>len(self.data)-1:
                        start=(x,y)
                        self.dict[(x,y)].remove(1)
                        break 
                    elif 1 not in self.dict[(x,y+1)]:
                        start=(x,y)
                        self.dict[(x,y)].remove(1)
                        break
                    else:
                        y=y+1
                p=1
                while 1 in self.dict[(start[0],start[1]-p)]:
                    self.dict[(start[0],start[1]-p)].remove(1)
                    p=p+1
                self.downline.append(((start[0],start[1]-p),start))
        self.uprightline=[]
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                if 2 not in self.dict[(x,y)]:
                    continue
                while 2 in self.dict[(x,y)]:
                    if x-1<0 or y+1>len(self.data)-1:
                        start=(x,y)
                        self.dict[(x,y)].remove(2)
                        break 
                    elif 2 not in self.dict[(x-1,y+1)]:
                        start=(x,y)
                        self.dict[(x,y)].remove(2)
                        break
                    else:
                        y=y+1
                        x=x-1
                p=1
                while 2 in self.dict[(start[0]+p,start[1]-p)]:
                    self.dict[(start[0]+p,start[1]-p)].remove(2)
                    p=p+1
                self.uprightline.append((start,(start[0]+p,start[1]-p)))    
        self.uprightline.sort(key=takeSecond)
        self.downrightline=[]
        for (x,y) in self.dict.keys():
            if 8 not in self.dict[(x,y)]:
                continue
            while 8 in self.dict[(x,y)]:
                if x-1<0 or y-1<0:
                    start=(x,y)
                    self.dict[(x,y)].remove(8)
                    break 
                elif 8 not in self.dict[(x-1,y-1)]:
                    start=(x,y)
                    self.dict[(x,y)].remove(8)
                    break
                else:
                    y=y-1
                    x=x-1
            p=1
            while 8 in self.dict[(start[0]+p,start[1]+p)]:
                self.dict[(start[0]+p,start[1]+p)].remove(8)
                p=p+1
            self.downrightline.append((start,(start[0]+p,start[1]+p)))
            
            
    def horizontalreflection(self,list):
        for line in list:
            if ((line[0][0],len(self.data)-1-line[0][1]),(line[1][0],len(self.data)-1-line[1][1])) not in list and ((line[1][0],len(self.data)-1-line[1][1]),(line[0][0],len(self.data)-1-line[0][1])) not in list: 
                return False
        return True
    def glidhor(self,list):
        for line in list:
            if line[0][0]>=self.period and line[1][0]>=self.period and line[0][0]<=2*self.period and line[1][0]<=2*self.period and line[0][0]+0.5*self.period<=len(self.data[0])-1 and line[1][0]+0.5*self.period<=len(self.data[0])-1:
                point1=(int(line[0][0]+self.period/2),len(self.data)-1-line[0][1])
                point2=(int(line[1][0]+self.period/2),len(self.data)-1-line[1][1])
                if (point1,point2) not in list and (point2,point1) not in list:
                    return False
            else:
                pass
        return True
                
    def verticalreflection(self,list):
        for i in [x for x in range(self.period+1,2*self.period)]+[x+0.5 for x in range(self.period+1,2*self.period)]:
            for line in list:
                if 2*i-line[0][0]>=i-self.period/2 and 2*i-line[0][0]<=i+self.period/2 and 2*i-line[1][0]>=i-self.period/2 and 2*i-line[1][0]<=i+self.period/2:
                    point1=(int(2*i-line[0][0]),line[0][1])
                    point2=(int(2*i-line[1][0]),line[1][1])
                    if (point1,point2) not in list and (point2,point1) not in list:
                        judge=0
                        break
                    else:
                        judge=1
                else:
                    pass
            if judge==1:
                return True
        return False
    def rotation(self,list):
        for i in [x for x in range(self.period+1,2*self.period)]+[x+0.5 for x in range(self.period+1,2*self.period)]:
            for line in list:
                if 2*i-line[0][0]>=i-self.period/2 and 2*i-line[0][0]<=i+self.period/2 and 2*i-line[1][0]>=i-self.period/2 and 2*i-line[1][0]<=i+self.period/2:
                    point1=(int(2*i-line[0][0]),len(self.data)-1-line[0][1])
                    point2=(int(2*i-line[1][0]),len(self.data)-1-line[1][1])
                    if (point1,point2) not in list and (point2,point1) not in list:
                        judge=0
                        break
                    else:
                        judge=1
                else:
                    pass
            if judge==1:
                return True
        return False
    def display(self):
        f=open(self.name+'.tex','w')
        start=r'''\documentclass[10pt]{article}
\usepackage{tikz}
\usepackage[margin=0cm]{geometry}
\pagestyle{empty}

\begin{document}

\vspace*{\fill}
\begin{center}
\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]
% North to South lines'''        
        f.write(start)
        northtosouth=[]
        for line in self.downline:
            northtosouth.append('\n    'r'\draw '+str(line[0]).replace(' ','')+' -- '+str(line[1]).replace(' ','')+';')
        f.writelines(northtosouth)
        f.write('\n'r'% North-West to South-East lines') 
        nwtose=[]
        for line in self.downrightline:
            nwtose.append('\n    'r'\draw '+str(line[0]).replace(' ','')+' -- '+str(line[1]).replace(' ','')+';')
        f.writelines(nwtose)
        f.write('\n'r'% West to East lines')
        wtoe=[]
        for line in self.rightline:
            wtoe.append('\n    'r'\draw '+str(line[0]).replace(' ','')+' -- '+str(line[1]).replace(' ','')+';')
        f.writelines(wtoe)        
        f.write('\n'r'% South-West to North-East lines') 
        swtone=[]
        for line in self.uprightline:
            swtone.append('\n    'r'\draw '+str(line[0]).replace(' ','')+' -- '+str(line[1]).replace(' ','')+';')
        f.writelines(swtone)
        f.write('\n'r'''\end{tikzpicture}
\end{center}
\vspace*{\fill}

\end{document}''')
        f.write('\n')
            
        
        
        f.close()
    def analyse(self):
        sym=[]
        self.totalline=self.downline+self.rightline+self.uprightline+self.downrightline
        if self.glidhor(self.totalline)==True:
            sym.append('glided horizontal reflection')          
        if self.horizontalreflection(self.totalline)==True: 
            sym.append('horizontal reflection')
        if self.verticalreflection(self.totalline)==True:
            sym.append('vertical reflection')
        if self.rotation(self.totalline)==True:
            sym.append('rotation')
        if len(sym)==1:
            print('Pattern is a frieze of period '+str(self.period)+' that is invariant under translation'+'\n        and '+sym[0]+' only.')
        elif len(sym)==2:
            if sym[-1]=='rotation':
                print('Pattern is a frieze of period '+str(self.period)+' that is invariant under translation,'+'\n        '+sym[0]+' and '+sym[1]+' only.')
            else:
                print('Pattern is a frieze of period '+str(self.period)+' that is invariant under translation,'+'\n        '+sym[0][0:-11]+' and '+sym[1][0:-11]+' reflections only.')
        elif len(sym)==3:
            print('Pattern is a frieze of period '+str(self.period)+' that is invariant under translation,'+'\n        '+sym[0][0:-11]+' and '+sym[1][0:-11]+' reflections, and '+sym[2]+' only.')
        elif len(sym)==0:
             print('Pattern is a frieze of period '+str(self.period)+' that is invariant under translation only.')

        
#a=Frieze('frieze_6-1.txt')
# downright=a.downrightline
# right=a.rightline
#down=a.downline
# upright=a.uprightline
#a.analyse()
#a.display()

