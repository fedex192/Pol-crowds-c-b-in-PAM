# -*- coding: utf-8 -*-
def population(P0,N=10000,Ct=1.0,Cmax=3.0,Ppl=0):

    import random
    from Agent import Agent

    if P0>=1:
        raise Exception('P0 cannot be bigger than the population')
    if Ppl>=1:
        raise Exception('Ppl cannot be bigger than the population')
    if Ct>Cmax:
        raise Exception('The threshold cannot surpass the maximum persuasion.')
        
    Ct=float(Ct)
    Cmax=float(Cmax)
       
    undpop=int(P0*N)
    againstpop=int(round((N-int(P0*N))/2))
    propop=N-undpop-againstpop
            
            
    
    undecided=[]
    prodecided=[]
    againstdecided=[]
    for i in range(undpop):
        undecided.append(Agent(0,random.uniform(-Ct,Ct),Ct))
    for i in range(propop):
        prodecided.append(Agent(1,random.uniform(Ct,Cmax),Ct))
    for i in range(againstpop):
        againstdecided.append(Agent(-1,random.uniform(-Cmax,-Ct),Ct))
    
    popul=undecided+prodecided+againstdecided
                 
    if len(popul)>N:
        popul=undecided+prodecided+againstdecided[:-1]
        random.shuffle(popul)
        return popul
    else:
        random.shuffle(popul)
        return popul
        
def maspopulation(listofarguments, N=100, numofrelevargs=10, numofproargs=5,Ct=1.0):
    '''listofarguments must have even length'''
    import random
    from Agent import Argumentativeagent
    popu=[]
    for agent in range(N):
        pros=range(len(listofarguments)/2)
        cons=range(len(listofarguments)/2, len(listofarguments))
        random.shuffle(pros)
        random.shuffle(cons)
        relevancevector=[0 for i in range(len(listofarguments))]
        recencyvector=[0 for i in range(len(listofarguments))]
        recencys=range(1,numofrelevargs+1)
        random.shuffle(recencys)
        
        for i in range(numofproargs):
            relevancevector[pros[-1]]=1
            recencyvector[pros[-1]]=recencys[-1]
            pros.pop()
            recencys.pop()
        for i in range(numofrelevargs-numofproargs):
            relevancevector[cons[-1]]=1
            recencyvector[cons[-1]]=recencys[-1]
            cons.pop()
            recencys.pop()
        persuasion=0
        count=0
        for i in range(len(listofarguments)):
            if relevancevector[i]==1:
                persuasion+=listofarguments[i].getvalence()*listofarguments[i].getimpact()
                count+=1*listofarguments[i].getimpact()
        popu.append(Argumentativeagent(1, relevancevector, recencyvector, persuasion/count, numofrelevargs, 0, Ct))
    
    return popu
 
def argumentativepopulation(listofarguments,N=10,numofrelevargs=5,Ct=1.0, Cmax=3.0,old=''):
    '''listofarguments must have even length'''
    import random2 as random
#    from newcagent import Argumentativeagent
    from CnewAgent import Argumentativeagent
    
    popu=[]
    for agent in range(N):
        #creo listas con todos los argumentos existentes, positivos y negativos. Los ordeno aleatoriamente.
        pros=range(len(listofarguments)/2)
        cons=range(len(listofarguments)/2, len(listofarguments))
        random.shuffle(pros)
        random.shuffle(cons)
        relevancevector=[0 for i in range(len(listofarguments))]
        
        #Elijo un número inicial de argumentos aleatorio para este agente.
        initialargs=random.randrange(0,numofrelevargs+1)
        while initialargs==numofrelevargs+1:
            initialargs=random.randrange(0,numofrelevargs+1) #podría pedir más, pero igual la persuasión depende sólo de 5, así que da igual.
        
        #Elijo un número inicial de argumentos positivos aleatorio para este agente.
        posargs=random.randrange(0,initialargs+1)
        while posargs==initialargs+1:
            posargs=random.randrange(0,initialargs+1)
         
        #Por la regla de los argumentos iguales, tengo que revisar que los que voy a agregar no vienen con su counter.
        allargs=len(relevancevector)
        tobeusedcons=[]
        if posargs!=0:
            tobeusedpros=pros[-posargs:] #tomo los pro que voy a usar.
        else:
            tobeusedpros=[]
        i=initialargs-posargs
        
        if old=='True':
            while i>0 and cons!=[]:
                if (cons[-1]-allargs/2) not in tobeusedpros:
                    tobeusedcons.append(cons[-1])
                    cons.pop()
                    i-=1
                else:
                    cons.pop()
        else:
            if i!=0:
                tobeusedcons=cons[-i:] #tomo los pro que voy a usar.

        
 #probé con posargs=0. Probar con posargs=initialargs y con el caso mixto.           
        
                  
        proused=[]
        consused=[]
        
        #Asigno posargs argumentos positivos para el agente.
        for i in range(len(tobeusedpros)):
            relevancevector[tobeusedpros[-1]]=1
            proused.append(tobeusedpros.pop())
        #Asigno los restantes argumentos negativos para el agente.
        for i in range(len(tobeusedcons)):            
            relevancevector[tobeusedcons[-1]]=1
            consused.append(tobeusedcons.pop())
            
        positiveindexes=sorted(proused)
        negativeindexes=sorted(consused)
                
        #Ahora calculo la persuasión en función de estos argumentos
        newpersuasion=0
        
        for i in range(initialargs):
            #Si tengo argumentos positivos y negativos, me fijo el más fuerte entre ambos grupos, y agrego ese.
                if len(positiveindexes)!=0 and len(negativeindexes)!=0:
                    if positiveindexes[-1]>negativeindexes[-1]-(allargs/2.0): #En el caso de 60 args, el 59 es como el 29 en índices. O sea, -30.
                        newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                        positiveindexes.pop()
                    elif positiveindexes[-1]<negativeindexes[-1]-(allargs/2.0):           
                        newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                        negativeindexes.pop()
                    elif positiveindexes[-1]==negativeindexes[-1]-(allargs/2.0): #agregué este elif al sacar lo de aniquilación
                        used=random.choice([positiveindexes[-1],negativeindexes[-1]])
                        newpersuasion+=listofarguments[used].getvalence()*listofarguments[used].getimpact()/float(allargs/2.0)
                        if used==positiveindexes[-1]:
                            positiveindexes.pop()
                        else:
                            negativeindexes.pop()
                    else:
                        print 'whyyyy?'
            #Si sólo tengo argumentos negativos, de una los agrego.
                elif len(positiveindexes)==0 and len(negativeindexes)!=0:
                    newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                    negativeindexes.pop()
            #Si sólo tengo argumentos positivos, de una los agrego.
                elif len(negativeindexes)==0 and len(positiveindexes)!=0:
                        newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                        positiveindexes.pop()
                else:
                    pass
                    #print 'this can not be right'
                    #return 'this can not be right'
      
        #Ahora, calculo la opinión.          
        if Ct<=newpersuasion:
            opinion=1
        elif -(Ct)>=newpersuasion:
            opinion=-1
        else: 
            opinion=0    
        
        #Por último, reviso que la persuasión no sea mayor a Cmax o -Cmax.
        if newpersuasion>Cmax:
            newpersuasion=Cmax
        elif newpersuasion<-Cmax:
            newpersuasion=-Cmax
        
        
        popu.append(Argumentativeagent(2, relevancevector, 0, newpersuasion, numofrelevargs, opinion, Ct))
    
    return popu   
    
        
def specialpopulation(P0,N=10000,Ct=1.0,newCt=0.5,Cmax=3.0,Ppl=0):

    import random
    from Agent import Agent
       
    Ct=float(Ct)
    Cmax=float(Cmax)
       
    undpop=int(P0*N)
    againstpop=int(round((N-int(P0*N))/2))
    propop=N-undpop-againstpop
             
            
    
    undecided=[]
    prodecided=[]
    againstdecided=[]
    rest=undpop/2
    newlength=undpop-rest
    for i in range(newlength):
        undecided.append(Agent(0,random.uniform(newCt,Ct),Ct))
    for i in range(rest):
        undecided.append(Agent(0,random.uniform(-Ct,-newCt),Ct))                
    for i in range(propop):
        prodecided.append(Agent(1,random.uniform(Ct,Cmax),Ct))
    for i in range(againstpop):
        againstdecided.append(Agent(-1,random.uniform(-Cmax,-Ct),Ct))
    
    popul=undecided+prodecided+againstdecided
                 
    if len(popul)>N:
        popul=undecided+prodecided+againstdecided[:-1]
        random.shuffle(popul)
        return popul
    else:
        random.shuffle(popul)
        return popul

def nonrandompopulation(P0,N=10000,Ct=1.0,Cmax=3.0,Ppl=0):

    import random
    from Agent import Agent

    if P0>=1:
        raise Exception('P0 cannot be bigger than the population')
    if Ppl>=1:
        raise Exception('Ppl cannot be bigger than the population')
    if Ct>Cmax:
        raise Exception('The threshold cannot surpass the maximum persuasion.')
        
    Ct=float(Ct)
    Cmax=float(Cmax)
       
    undpop=int(P0*N)
    againstpop=int(round((N-int(P0*N))/2))
    propop=N-undpop-againstpop
            
            
    
    undecided=[]
    prodecided=[]
    againstdecided=[]
    for i in range(undpop):
        undecided.append(Agent(0,random.uniform(-Ct,Ct),Ct))
    for i in range(propop):
        prodecided.append(Agent(1,random.uniform(Ct,Cmax),Ct))
    for i in range(againstpop):
        againstdecided.append(Agent(-1,random.uniform(-Cmax,-Ct),Ct))
    
    popul=undecided+prodecided+againstdecided
                 
    if len(popul)>N:
        popul=undecided+prodecided+againstdecided[:-1]
        #random.shuffle(popul)
        return popul
    else:
        #random.shuffle(popul)
        return popul
        
        
def distributedpopulation(P0,N=10000,Ct=1.0,Cmax=3.0,alpha=5):
    import numpy as np
    import random
    from Agent import Agent
        
    Ct=float(Ct)
    Cmax=float(Cmax)
       
    undpop=int(P0*N)
    againstpop=int(round((N-int(P0*N))/2))
    propop=N-undpop-againstpop
    
    
            
            
    
    undecided=[]
    prodecided=[]
    againstdecided=[]
    undecidedpersuasions=[]
    for i in range(undpop):
        undecided.append(Agent(0,(np.random.beta(alpha,alpha)-0.5)*2,Ct))
        undecidedpersuasions.append((np.random.beta(alpha,alpha)-0.5)*2)
    for i in range(propop):
        prodecided.append(Agent(1,random.uniform(Ct,Cmax),Ct))
    for i in range(againstpop):
        againstdecided.append(Agent(-1,random.uniform(-Cmax,-Ct),Ct))
    
    popul=undecided+prodecided+againstdecided
    return popul,undecidedpersuasions             
    #if len(popul)>N:
    #    popul=undecided+prodecided+againstdecided[:-1]
    #    random.shuffle(popul)
    #    return popul
    #else:
    #    random.shuffle(popul)
    #    return popul    
    
def distributedpopulation2(P0,N=10000,Ct=1.0,Cmax=3.0,alpha=0.1,mult=2):
    import numpy as np
    import random
    from Agent import Agent
        
    Ct=float(Ct)
    Cmax=float(Cmax)
       
    undpop=int(P0*N)
    againstpop=int(round((N-int(P0*N))/2))
    propop=N-undpop-againstpop
    
    
            
            
    
    undecided=[]
    prodecided=[]
    againstdecided=[]
    undecidedpersuasions=[]
    for i in range(undpop):
        undecided.append(Agent(0,(np.random.beta(alpha*mult,alpha)-0.5)*2,Ct))
        undecidedpersuasions.append((np.random.beta(alpha*mult,alpha)-0.5)*2)
    for i in range(propop):
        prodecided.append(Agent(1,random.uniform(Ct,Cmax),Ct))
    for i in range(againstpop):
        againstdecided.append(Agent(-1,random.uniform(-Cmax,-Ct),Ct))
    
    popul=undecided+prodecided+againstdecided
    return popul,undecidedpersuasions             
    #if len(popul)>N:
    #    popul=undecided+prodecided+againstdecided[:-1]
    #    random.shuffle(popul)
    #    return popul
    #else:
    #    random.shuffle(popul)
    #    return popul    
    
def distributedpopulation3(P0,N=10000,Ct=1.0,Cmax=3.0,alpha=5,case=0.1):
    import numpy as np
    import random
    from Agent import Agent
        
    Ct=float(Ct)
    Cmax=float(Cmax)
       
    undpop=int(P0*N)
    againstpop=int(round((N-int(P0*N))/2))
    propop=N-undpop-againstpop
    
    
            
            
    
    undecided=[]
    prodecided=[]
    againstdecided=[]
    undecidedpersuasions=[]
    for i in range(undpop):
        a=(np.random.beta(alpha,alpha)-0.5)*1.8+case
        while a>1.0 or a<-1.0:
            a=(np.random.beta(alpha,alpha)-0.5)*1.8+case
            #print 'mmm'
        undecided.append(Agent(0,a,Ct))
        undecidedpersuasions.append(a)
    for i in range(propop):
        prodecided.append(Agent(1,random.uniform(Ct,Cmax),Ct))
    for i in range(againstpop):
        againstdecided.append(Agent(-1,random.uniform(-Cmax,-Ct),Ct))
    
    popul=undecided+prodecided+againstdecided
    return popul,undecidedpersuasions             

def undistributedpopulation(P0,N=10000,Ct=1.0,Cmax=3.0,Ppl=0):

    import random
    from Agent import Agent

    if P0>=1:
        raise Exception('P0 cannot be bigger than the population')
    if Ppl>=1:
        raise Exception('Ppl cannot be bigger than the population')
    if Ct>Cmax:
        raise Exception('The threshold cannot surpass the maximum persuasion.')
        
    Ct=float(Ct)
    Cmax=float(Cmax)
       
    undpop=int(P0*N)
    againstpop=int(round((N-int(P0*N))/2))
    propop=N-undpop-againstpop
            
            
    
    undecided=[]
    prodecided=[]
    againstdecided=[]
    undecidedpersuasions=[]
    for i in range(undpop):
        undecided.append(Agent(0,random.uniform(-Ct,Ct),Ct))
        undecidedpersuasions.append(random.uniform(-Ct,Ct))
    for i in range(propop):
        prodecided.append(Agent(1,random.uniform(Ct,Cmax),Ct))
    for i in range(againstpop):
        againstdecided.append(Agent(-1,random.uniform(-Cmax,-Ct),Ct))
    
    popul=undecided+prodecided+againstdecided
                 
    if len(popul)>N:
        popul=undecided+prodecided+againstdecided[:-1]
        random.shuffle(popul)
        return popul
    else:
        random.shuffle(popul)
        return popul,undecidedpersuasions
        
        
def distributedpopulation4(P0,N=10000,Ct=1.0,Cmax=3.0,alpha=5,case=4/5.0):
    import numpy as np
    import random
    from Agent import Agent
        
    Ct=float(Ct)
    Cmax=float(Cmax)
       
    undpop=int(P0*N)
    againstpop=int(round((N-int(P0*N))/2))
    propop=N-undpop-againstpop
    
    
            
            
    
    undecided=[]
    prodecided=[]
    againstdecided=[]
    undecidedpersuasions=[]
    for i in range(undpop):
        a=1.95*(np.random.beta(alpha*4,alpha)-round(case,1))
        while a>1.0 or a<-1.0:
            a=1.95*(np.random.beta(alpha*4,alpha)-round(case,1))
            #print 'mmm'
        undecided.append(Agent(0,a,Ct))
        undecidedpersuasions.append(a)
    for i in range(propop):
        prodecided.append(Agent(1,random.uniform(Ct,Cmax),Ct))
    for i in range(againstpop):
        againstdecided.append(Agent(-1,random.uniform(-Cmax,-Ct),Ct))
    
    popul=undecided+prodecided+againstdecided
    return popul,undecidedpersuasions  