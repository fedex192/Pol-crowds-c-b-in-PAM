# -*- coding: utf-8 -*-
class Agent(object):

    """
    Representation of a person; an agent in the model.
    Before assignment, check that opinion and persuasion fullfil requirements.
    """
    def __init__(self, opinion, persuasion,Ct=1.0):
        """
        Initialize an Agent instance, saves all parameters as attributes
        of the instance.        
        opinion: Integer, possible values: 1, -1, 0.        
        persuasion: a double between -Cmax and Cmax.
        Ct: a double between 0 and Cmax; it determines changes in opinion.
        """
        self.opinion=opinion
        self.persuasion=persuasion
        self.threshold=Ct

    def getopinion(self):
        """
        Returns opinion.
        """
        return self.opinion

    def getpersuasion(self):
        """
        Returns persuasion.
        """
        return self.persuasion

    def getthreshold(self):
        """
        Returns threshold.
        """
        return self.threshold
            
class Argumentativeagent(Agent):
    """
    Representation of an argumentative person; an agent in the model. It is capable of receiving and changing arguments.
    Before assignment, check that opinion and persuasion fullfil requirements. It builds upon the Agent class (the reason
    behind this distinction is related to preliminary simulations which used Agent instead of Argumentativeagent).
    """
    def __init__(self, tipo, relevancevector, recencyvector, persuasion, totalargs, opinion=0, Ct=1.0):
        """
        Initialize an Argumentativeagent instance, saves all parameters as attributes
        of the instance.        
        relevancevector: list of ones and zeros.
        recencyvector: unused, initialized as 0 in our simulations. It was originally used for replicating Mäs and Flaché.
        persuasion: a double between -Cmax and Cmax.        
        totalargs: maximum number of arguments an agent can have.        
        opinion: Integer, possible values: 1, -1, 0.        
        Ct: a double between 0 and Cmax; it determines changes in opinion.
        """
        self.tipo=tipo
        self.totalargs=totalargs
        if tipo==1:
            opinion=persuasion
            Ct=1.0       
        Agent.__init__(self,opinion, persuasion,Ct)
        self.relevancevector=relevancevector
        self.recencyvector=recencyvector
    
    def getrelevancevector(self):
        #Relevance vector contains slots for every possible argument in the system. The first half of those slots are used for representing positive arguments. 
        #The second half are the negative ones. The length therefore shows all the arguments that could exist, N_A. If an argument is present, it is represented as a 1 in its slot. 
        #If it is not present, it is represented as a 0. Binary representation of the presence of arguments.
        return self.relevancevector
    
    def changepersuasion(self,listofarguments,Cmax=3.0):
            #This functions calculates the persuasion given the arguments of the agent. It is to be called after initial argument assignment, and after a new argument is added. 
            #It is more complicated than it needs to be, because we originally had planned other rules and conditions which required that complexity. We did not modify it afterwards,
            #because it was not necessary. Specifically, we used to delete arguments in this function instead of the next one. Now this function only calculates persuasion, and nothing else.
                
            newpersuasion=0
            allargs=len(self.relevancevector)
            
            positiveindexes=[]
            negativeindexes=[]
            
            #Since each argument has an assigned index, and that index determines its weight, we first determine which arguments we have by properly reading that information
            #from the relevance vector. 
            #First, we find all positive arguments. Then, all negative arguments. We save them in the order: from stronger to weaker, because it is easier code-wise.
            for arg in range(allargs/2):
                if self.getrelevancevector()[(allargs/2-1)-arg]==1:
                    positiveindexes.append((allargs/2-1)-arg)
            for arg in range(allargs/2):
                if self.getrelevancevector()[(allargs-1)-arg]==1:
                    negativeindexes.append((allargs-1)-arg)

            #Now we reorder-them, from weakest to strongest.
            positiveindexes=sorted(positiveindexes)
            negativeindexes=sorted(negativeindexes)
            
            #This part is more complicated than it needs to be. If in doubt, contact the corresponding author for further explanations. 
            #In a nutshell, it was originally necessary to keep track of the weight and order of the arguments to be used for calculating persuasion, to find which one to delete.
            #Now, all this loop could be replaced by a much simpler one in which we get the weights of all arguments in relevance vector and procede to calculate persuasion.
            
            for i in range(self.totalargs):
                #If the agent has both positive and negative arguments:                            
                if len(positiveindexes)!=0 and len(negativeindexes)!=0:                                                                                            
                        if positiveindexes[-1]>=negativeindexes[-1]-(allargs/2):
                            newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                            positiveindexes.pop()
                        elif positiveindexes[-1]<negativeindexes[-1]-(allargs/2):           
                            newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                            negativeindexes.pop()
                #If the agent only has negative arguments:
                elif len(positiveindexes)==0 and len(negativeindexes)!=0:
                        newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                        negativeindexes.pop()
                #If the agent only has positive arguments:
                elif len(negativeindexes)==0 and len(positiveindexes)!=0:
                        newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                        positiveindexes.pop()
                else:
                    break

            
            #Now, we set the new persuasion of the agent:
            self.persuasion=newpersuasion        
                    
            
            #Changing persuasion may change opinion. So now we change opinion accordingly.
            if self.getthreshold()<self.getpersuasion():
                self.opinion=1
            elif -(self.getthreshold())>self.getpersuasion():
                self.opinion=-1
            else: 
                self.opinion=0    
            
            #Persuasion calculated as before could actually be higher than the maximum possible value. If this happens, we replace that value by the maximum with the corresponding sign.
            if self.getpersuasion()>Cmax:
                self.persuasion=Cmax
            elif self.getpersuasion()<-Cmax:
                self.persuasion=-Cmax
                
    def addargument(self,newindex):                           
        #Originally, there were other types. We deleted them and left the one we used for our simulations, for clarity.
        if self.tipo==2:
            
                #First, we add the new argument.
                self.relevancevector[newindex]=1
                allpos=(len(self.relevancevector)/2)
                #positive arguments are the first half slots in relevancevector, and negativearguments are the second half slots. 
                #To compare weights between arguments of different sign, we consider the index of the positive, and compare it to the index of the negative - allpos.
                

                #Now we check if there are more than the maximum number of arguments, and if so, delete one argument:
                            
                minpos=[]
                minneg=[]
                if sum(self.relevancevector)>self.totalargs:
                    #We check the positive argument with least weight (if it exists).
                    for i in range(allpos):
                        if self.relevancevector[i]==1:
                            minpos=i
                            break
                    #We check the negative argument with least weight (if it exists).
                    for i in range(allpos):
                        if self.relevancevector[i+allpos]==1:
                            minneg=i
                            break 
                            
                    #If there are both positive and negative arguments...        
                    if minpos!=[] and minneg!=[]:
                        #if the positive argument has least weight than the negative, we delete it.
                        if minpos<minneg:
                            self.relevancevector[minpos]=0
                        #if the negative argument has least weight than the positive, we delete it.                            
                        elif minpos>minneg:
                            self.relevancevector[minneg+allpos]=0
                        #if both have the same weight, and one of them is the one received, we delete the old one, and keep the new one.
                        else:
                            if newindex==minpos:
                                self.relevancevector[newindex+allpos]=0
                            elif newindex==minneg+allpos:
                                self.relevancevector[newindex-allpos]=0
                        #If we initialize agents with less than the maximum number of arguments, it could be possible that both arguments of the same weight were already in memory, 
                        #and that the new argument is neither of them. That means that the new argument is stronger. If that is the case, we randomly choose which of the arguments
                        #with the same weight we delete.
                            else:
                                import random
                                true=random.choice([minpos,minneg+allpos])
                                self.relevancevector[true]=0
                    #Instead, if the minimum was the negative one, we delete it.                
                    elif minpos==[] and minneg!=[]:
                        self.relevancevector[minneg+allpos]=0  
                    #if the minimum was the positive one, we delete it.       
                    elif minneg==[] and minpos!=[]:
                        self.relevancevector[minpos]=0            
                            
    def newgetsimilarity(self,Agent2):
        return (1.0/6.0)*float((6.0-abs(self.getpersuasion()-Agent2.getpersuasion())))                
                
        #The reason behind the name "new" is that we had previously included a getsimilarity function with the formula used in Mäs and Flaché, for testing.

    