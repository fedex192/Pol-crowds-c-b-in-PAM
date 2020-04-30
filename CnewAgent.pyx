cdef class Agent(object):

    cdef public int opinion
    cdef public double persuasion
    cdef public double threshold
    
    def __init__(self, opinion, persuasion,Ct=1.0):

        self.opinion=opinion
        self.persuasion=persuasion
        self.threshold=Ct
           
    cpdef int getopinion(self):

        return self.opinion

    cpdef double getpersuasion(self):

        return self.persuasion

    cpdef double getthreshold(self):

        return self.threshold        
        
    cpdef void change(self,double delta,double k, int case,bint ismax, double Cmax=3.0):

        if case==1:
            if ismax:
                self.persuasion=self.getpersuasion()-delta
            else: 
                self.persuasion=self.getpersuasion()+delta
        elif case==2:
            if not ismax:
                self.persuasion=self.getpersuasion()-delta
            else: 
                self.persuasion=self.getpersuasion()+delta
        elif case==3:
            if self.getopinion()!=0:
                if ismax:
                    self.persuasion=self.getpersuasion()-delta
                else:
                    self.persuasion=self.getpersuasion()+delta
            elif self.getopinion()==0:
                if ismax:
                    self.persuasion=self.getpersuasion()-k*delta
                else: 
                    self.persuasion=self.getpersuasion()+k*delta
                
                
        if self.getthreshold()<self.getpersuasion():
            self.opinion=1
        elif -(self.getthreshold())>self.getpersuasion():
            self.opinion=-1
        else: 
            self.opinion=0    
            
        if self.getpersuasion()>Cmax:
            self.persuasion=Cmax
        elif self.getpersuasion()<-Cmax:
            self.persuasion=-Cmax          

               

cdef class Argumentativeagent(Agent):

    cdef public int tipo
    cdef public relevancevector
    cdef public int totalargs
    cdef public recencyvector

    def __init__(self, tipo, relevancevector, recencyvector, persuasion, totalargs, opinion=0, Ct=1.0):

        self.tipo=tipo
        self.totalargs=totalargs
        if tipo==1:
            opinion=persuasion
            Ct=1.0       
        Agent.__init__(self,opinion, persuasion,Ct)
        self.relevancevector=relevancevector
        self.recencyvector=recencyvector
  
    
    def getrelevancevector(self):
        return self.relevancevector
    
    def getrecencyvector(self):
        return self.recencyvector
        
    cpdef void changepersuasion(self,list listofarguments,double Cmax=3.0):
        cdef:
            double newpersuasion
            int allargs, arg,i
            list positiveindexes,negativeindexes
            
            
        if self.tipo==1:
            print('MassiveError')
            pass
        
        else:          
            newpersuasion=0
            allargs=len(self.relevancevector)
            
            if sum(self.relevancevector)>self.totalargs:
                print 'muy mal'
                print sum(self.relevancevector)
            #else:
             #   pass
                
            positiveindexes=[]
            negativeindexes=[]

            for arg in range(allargs/2):
                if self.getrelevancevector()[(allargs/2-1)-arg]==1:
                    positiveindexes.append((allargs/2-1)-arg)
            for arg in range(allargs/2):
                if self.getrelevancevector()[(allargs-1)-arg]==1:
                    negativeindexes.append((allargs-1)-arg)
            

            positiveindexes=sorted(positiveindexes)
            negativeindexes=sorted(negativeindexes)
            
            for i in range(self.totalargs):                            
                if len(positiveindexes)!=0 and len(negativeindexes)!=0:                                                                       
                        if positiveindexes[-1]>=negativeindexes[-1]-(allargs/2):
                            newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                            positiveindexes.pop()
                        elif positiveindexes[-1]<negativeindexes[-1]-(allargs/2):           
                            newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                            negativeindexes.pop()
                        else:                            
                            print 'FATAL ERROR'
                            #return positiveindexes,negativeindexes,self.totalargs
                            #return 'what?'
                elif len(positiveindexes)==0 and len(negativeindexes)!=0:
                        newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                        negativeindexes.pop()
                elif len(negativeindexes)==0 and len(positiveindexes)!=0:
                        newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                        positiveindexes.pop()
                else:
                    break

            
            
            self.persuasion=newpersuasion        
                    
            if self.getthreshold()<self.getpersuasion():
                self.opinion=1
            elif -(self.getthreshold())>self.getpersuasion():
                self.opinion=-1
            else: 
                self.opinion=0    
            
            if self.getpersuasion()>Cmax:
                self.persuasion=Cmax
            elif self.getpersuasion()<-Cmax:
                self.persuasion=-Cmax
                
    def addargument(self,newindex):
        if self.tipo==1:
            if self.relevancevector[newindex]==0 and self.recencyvector[newindex]==0:
                self.relevancevector[newindex]=1 
                self.recencyvector[newindex]=self.totalargs+1 
                for recency in range(len(self.recencyvector)):
                    if self.recencyvector[recency]>0:
                        self.recencyvector[recency]-=1 
                for recency in range(len(self.recencyvector)): 
                    if self.recencyvector[recency]==0:
                        self.relevancevector[recency]=0
            elif self.relevancevector[newindex]==1 and self.recencyvector[newindex]!=0:
                oldrecency=self.recencyvector[newindex]
                self.recencyvector[newindex]=self.totalargs+1
                for recency in range(len(self.recencyvector)):
                    if self.recencyvector[recency]>oldrecency:
                        self.recencyvector[recency]-=1
            else:
                print 'ojo'
        elif self.tipo==3:
            
                allpos=(len(self.relevancevector)/2)
                if newindex>allpos-1: #por ejemplo, 29.
                    if self.relevancevector[newindex-allpos]==1: 
                        self.relevancevector[newindex-allpos]=0
                    else:
                        self.relevancevector[newindex]=1 
                elif newindex<allpos:
                    if self.relevancevector[newindex+allpos]==1: 
                        self.relevancevector[newindex+allpos]=0
                    else:
                        self.relevancevector[newindex]=1
                else:
                    print 'what2?'
               
                
                minpos=[]
                minneg=[]
                if sum(self.relevancevector)>self.totalargs:
                    for i in range(allpos):
                        if self.relevancevector[i]==1:
                            minpos=i
                            break
                    for i in range(allpos):
                        if self.relevancevector[i+allpos]==1:
                            minneg=i
                            break 
                    if minpos!=[] and minneg!=[]:
                        if minpos<minneg-allpos:
                            self.relevancevector[minpos]=0
                        else:
                            self.relevancevector[minneg]=0        
                    elif minpos==[] and minneg!=[]:
                        self.relevancevector[minneg]=0  
                    elif minneg==[] and minpos!=[]:
                        self.relevancevector[minpos]=0
                    else:
                        print 'oh no'
                            

        elif self.tipo==2:

                self.relevancevector[newindex]=1
                allpos=(len(self.relevancevector)/2)
                            
                minpos=[]
                minneg=[]
                if sum(self.relevancevector)>self.totalargs:
                    for i in range(allpos):
                        if self.relevancevector[i]==1:
                            minpos=i
                            break
                    for i in range(allpos):
                        if self.relevancevector[i+allpos]==1:
                            minneg=i
                            break 
                    if minpos!=[] and minneg!=[]:
                        if minpos<minneg:
                            self.relevancevector[minpos]=0
                        elif minpos>minneg:
                            self.relevancevector[minneg+allpos]=0
                        else:
                            if newindex==minpos:
                                self.relevancevector[newindex+allpos]=0
                            elif newindex==minneg+allpos:
                                self.relevancevector[newindex-allpos]=0

                            else:
                                import random2 as random
                                true=random.choice([minpos,minneg+allpos])
                                self.relevancevector[true]=0
                                    
                    elif minpos==[] and minneg!=[]:
                        self.relevancevector[minneg+allpos]=0  
                    elif minneg==[] and minpos!=[]:
                        self.relevancevector[minpos]=0
                    else:
                        print 'oh no'
                        
                if sum(self.relevancevector)>self.totalargs:
                         for i in range(len(self.relevancevector)):
                            if self.relevancevector[i]==1:
                                print i             

                            
        elif self.tipo==4:

                self.relevancevector[newindex]=1
                allpos=(len(self.relevancevector)/2)
                            
                minpos=[]
                minneg=[]
                if sum(self.relevancevector)>self.totalargs:
                    for i in range(allpos):
                        if self.relevancevector[i]==1:
                            minpos=i
                            break
                    for i in range(allpos):
                        if self.relevancevector[i+allpos]==1:
                            minneg=i
                            break 
                    if minpos!=[] and minneg!=[]:
                        if minpos<minneg:
                            self.relevancevector[minpos]=0
                        elif minpos>minneg:
                            self.relevancevector[minneg+allpos]=0
                        else:
                            if newindex==minpos:
                                self.relevancevector[newindex]=0
                            elif newindex==minneg+allpos:
                                self.relevancevector[newindex]=0

                            else:
                                import random2 as random
                                true=random.choice([minpos,minneg+allpos])
                                self.relevancevector[true]=0
                                    
                    elif minpos==[] and minneg!=[]:
                        self.relevancevector[minneg+allpos]=0  
                    elif minneg==[] and minpos!=[]:
                        self.relevancevector[minpos]=0
                    else:
                        print 'oh no'
                        
                if sum(self.relevancevector)>self.totalargs:
                         for i in range(len(self.relevancevector)):
                            if self.relevancevector[i]==1:
                                print i             
                            
                      
                                                                     
    cpdef double getsimilarity(self,Agent Agent2):
        return 0.5*float((2-abs(self.getopinion()-Agent2.getopinion())))
        
    cpdef double newgetsimilarity(self,Agent Agent2):
        return (1.0/6.0)*float((6.0-abs(self.getpersuasion()-Agent2.getpersuasion())))       