# -*- coding: utf-8 -*-
 
def argumentativepopulation(listofarguments,N=10,numofrelevargs=5,Ct=1.0, Cmax=3.0,old=''):
    '''This function is used to initialize a population of agents. listofarguments must have even length, i.e. same quantity of positive and negative arguments.
    The number of relevant arguments (numofrelevargs) is another way to call Memory (M). We kept this old notation in some functions (it was related to the paper of
    Mäs and Flaché). old variable is unused and irrelevant. NOTE: posture is called persuasion in this code.'''
    
    import random
    from Agent import Argumentativeagent
    popu=[] #this will contain all the agents.
    
    for agent in range(N):
        #we first create lists of all existing arguments, either positive or negative. This will be randomly ordered (shuffle).
        pros=range(len(listofarguments)/2)
        cons=range(len(listofarguments)/2, len(listofarguments))
        random.shuffle(pros)
        random.shuffle(cons)
        relevancevector=[0 for i in range(len(listofarguments))] #we initialize a "relevancevector", which keeps track of which arguments an agent has (value 1), and which it does not (value 0). 
        
        #The commented line can be used to choose an initial random number of arguments; we started using this, and after noticing it was easier to explain,
        #and that results were the same, we chose to set it to the maximum number of arguments in memory, which is the uncommented line. 
         
        #initialargs=random.randrange(0,numofrelevargs+1)
        initialargs=numofrelevargs
        
        #This while (and future whiles of the same form) is here to ensure that there are never more arguments that allowed. Initial testing showed that
        #Python had a very low probability of setting this one unit too large, and this ensures it does not happen.
        
        #while initialargs==numofrelevargs+1:
            #initialargs=random.randrange(0,numofrelevargs+1)
        
        #I choose a random initial number of positive arguments (therefore, choosing a random number of negative arguments)
        posargs=random.randrange(0,initialargs+1)
        while posargs==initialargs+1:
            posargs=random.randrange(0,initialargs+1)
         
        #We now choose the specific positive and negative arguments to be used:
        allargs=len(relevancevector)
        tobeusedcons=[]
        if posargs!=0:
            tobeusedpros=pros[-posargs:] #positive arguments
        else:
            tobeusedpros=[]
        negargs=initialargs-posargs
        
        if i!=0:
                tobeusedcons=cons[-negargs:] #negative arguments
               
                  
        proused=[]
        consused=[]
        
        #We put 1 values in the slots of the relevance vector to denote that they are owned by the agent. 
        for i in range(len(tobeusedpros)):
            relevancevector[tobeusedpros[-1]]=1
            proused.append(tobeusedpros.pop())
        #Asigno los restantes argumentos negativos para el agente.
        for i in range(len(tobeusedcons)):            
            relevancevector[tobeusedcons[-1]]=1
            consused.append(tobeusedcons.pop())
            
        #To initially set the persuasion and opinion of agents, we use the same code used in Agent.py, in function changepersuasion.
        #This is actually more complicated than it needs to be. Refer to function Agent.py to see this code explained.
        #Basically, we did it in a way which allowed for certain tests and different rules of interaction, but ended up not using those.
            
        positiveindexes=sorted(proused)
        negativeindexes=sorted(consused)
                
        #Calculating initial persuasion:
        newpersuasion=0
        
        for i in range(initialargs):
                if len(positiveindexes)!=0 and len(negativeindexes)!=0:
                    if positiveindexes[-1]>=negativeindexes[-1]-(allargs/2.0):
                        newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                        positiveindexes.pop()
                    elif positiveindexes[-1]<negativeindexes[-1]-(allargs/2.0):           
                        newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                        negativeindexes.pop()
                elif len(positiveindexes)==0 and len(negativeindexes)!=0:
                    newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                    negativeindexes.pop()
                elif len(negativeindexes)==0 and len(positiveindexes)!=0:
                    newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                    positiveindexes.pop()
                else:
                    pass
      
        #Now, we set the opinion of the agent:          
        if Ct<=newpersuasion:
            opinion=1
        elif -(Ct)>=newpersuasion:
            opinion=-1
        else: 
            opinion=0    
        
        #Lastly, it can happen that calculated persuasion is actually higher than the maximum value. In this case, we set it as the maximum.
        if newpersuasion>Cmax:
            newpersuasion=Cmax
        elif newpersuasion<-Cmax:
            newpersuasion=-Cmax
        
        #We now create the agent with all the previous information, and append it to the population list. The first number is the type (it must be 2), and the third variable is the unused recency vector.
        popu.append(Argumentativeagent(2, relevancevector, 0, newpersuasion, numofrelevargs, opinion, Ct))
    
    return popu   