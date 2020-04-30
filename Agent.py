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
        
    def change(self,delta,k,case,ismax,Cmax=3.0):
        '''Changes the persuasion according to the specified interaction, given by case.
        If case=1, then it assumes equal opinions; if case=2, it assumes opposing 
        opinions; if case=3 or 4, it assumes interaction between decided and undecided agents; in the
        first case, the agent's opinion is 1 or -1; in the second case, the agent's opinion is 0.
        If ismax=True, then it assumes this Agent has the higher persuasion value; if ismax=False,
        then it's the other way around.
        Delta gives the strength of the interaction; k gives the assymetry associated with not having an opinion.'''
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
   
    def change2(self,delta,k,case,ismax,Cmax=3.0):
        '''Changes the persuasion according to the specified interaction, given by case.
        If case=1, then it assumes equal opinions; if case=2, it assumes opposing 
        opinions; if case=3 or 4, it assumes interaction between decided and undecided agents; in the
        first case, the agent's opinion is 1 or -1; in the second case, the agent's opinion is 0.
        If ismax=True, then it assumes this Agent has the higher persuasion value; if ismax=False,
        then it's the other way around.
        Delta gives the strength of the interaction; k gives the assymetry associated with not having an opinion.'''
        if case==1:
            #La idea sería: if self.getopinion()==1 and self.getpersuasion()<=Cmax-delta:
            #                           entonces ambos tienen opinión +1, y me acerco a Cmax --> 
            #                           self.persuasion=self.getpersuasion+delta
            #               elif self.getopinion()==1 and self.getpersuasion()>=Cmax-delta:
            #                           self.persuasion=Cmax
            #               elif self.getopinion()==-1, las mismas dos condiciones pero cambiando por -Cmax+delta, y y así.
            #               elif self.getopinion()==0: 
            #                   if self.getpersuasion>=delta: 
            #                       self.persuasion=self.getpersuasion-delta
            #                   elif self.getpersuasion<=-delta:
            #                       self.persuasion=self.getpersuasion+delta
            #                   else:
            #                       self.persuasion=0 (o podría meter la cláusula de hacer self.getpersuasion-delta/2 y así.
            #
            
            
            if ismax:
                self.persuasion=self.getpersuasion()-delta
            else: 
                self.persuasion=self.getpersuasion()+delta
        elif case==2:
            #repetir lo de antes, pero ahora pidiendo que sea al revés del loop anterior.
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
            
class Argumentativeagent(Agent):
    """
    Representation of an argumentative person; an agent in the model. It is capable to receive and change arguments.
    Before assignment, check that opinion and persuasion fullfil requirements.
    """
    def __init__(self, tipo, relevancevector, recencyvector, persuasion, totalargs, opinion=0, Ct=1.0):
        """
        Initialize an Argumentativeagent instance, saves all parameters as attributes
        of the instance.        
        relevancevector: list of ones and zeros.
        opinion: Integer, possible values: 1, -1, 0.        
        persuasion: a double between -Cmax and Cmax.
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
        #list(np.array(relevancevector)*totalargs)
    
    def getrelevancevector(self):
        return self.relevancevector
    
    def getrecencyvector(self):
        return self.recencyvector
    
#    def maximpact(self):
#        return self.maximpact
    
    def changepersuasion(self,listofarguments,Cmax=3.0):

        
        if self.tipo==1:
            
            newpersuasion=0
            count=0
            for i in range(len(self.relevancevector)):
                if self.relevancevector[i]==1:
                    newpersuasion+=listofarguments[i].getvalence()*listofarguments[i].getimpact()
                    count+=1*listofarguments[i].getimpact()
            self.persuasion=newpersuasion/float(count)
            self.opinion=self.persuasion
        
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
            #Primero me quedo con todos los argumentos positivos (sus índices).
            #Luego los negativos. Luego, busco los self.totalargs argumentos de cualquier valencia más fuertes.
            for arg in range(allargs/2):
                if self.getrelevancevector()[(allargs/2-1)-arg]==1:
                    positiveindexes.append((allargs/2-1)-arg)
            for arg in range(allargs/2):
                if self.getrelevancevector()[(allargs-1)-arg]==1:
                    negativeindexes.append((allargs-1)-arg)
            #Guardé los índices. No los impactos.

            positiveindexes=sorted(positiveindexes)
            negativeindexes=sorted(negativeindexes)
            
            for i in range(self.totalargs):                            
                if len(positiveindexes)!=0 and len(negativeindexes)!=0:                                                                       
                        #Comparo índices, que van de 0 a 29. #Luego de poner que sólo se recuerdan 5, ya no importa el orden en el que los sumo. Agregué >= acá para incluir el caso de igualdad, después de sacar la aniquilación.
                        if positiveindexes[-1]>=negativeindexes[-1]-(allargs/2): #En el caso de 60 args, el 59 es como el 29 en índices. O sea, -30.
                            newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                            positiveindexes.pop()
                        elif positiveindexes[-1]<negativeindexes[-1]-(allargs/2):           
                            newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                            negativeindexes.pop()
                        else:                            
                            print 'what?'
                            return positiveindexes,negativeindexes,self.totalargs
                            #return 'what?'
                elif len(positiveindexes)==0 and len(negativeindexes)!=0:
                        newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                        negativeindexes.pop()
                #Si sólo tengo argumentos positivos, de una los agrego.
                elif len(negativeindexes)==0 and len(positiveindexes)!=0:
                        newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                        positiveindexes.pop()
                else:
                    break

            
            
            self.persuasion=newpersuasion        
                    
            
            #Ahora, ajustamos la opinión.
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
                self.relevancevector[newindex]=1 #primero cambio la relevancia de este argumento
                self.recencyvector[newindex]=self.totalargs+1 #Ahora, preparo para que la recency de este argumento sea totalargs.
                for recency in range(len(self.recencyvector)):
                    if self.recencyvector[recency]>0:
                        self.recencyvector[recency]-=1 #con esto, le saco recency a todos los demás que no sean 0
                for recency in range(len(self.recencyvector)): #ahora, me fijo cuáles dejaron de ser relevantes y los cambio.
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
            #En el caso de que el argumento agregado sea uno que ya estaba, entonces hay que aumentarle a ese la
            #recency, y restarle -1 sólo a los que originalmente tenían más recency que ese. De esa forma se preserva
            #el número de argumentos.
        elif self.tipo==3:
            
                allpos=(len(self.relevancevector)/2)
                if newindex>allpos-1: #por ejemplo, 29.
                    if self.relevancevector[newindex-allpos]==1: #si tengo el opuesto, no lo agrego y borro el otro.
                        self.relevancevector[newindex-allpos]=0
                    else:
                        self.relevancevector[newindex]=1 #si no tengo el opuesto, agrego este.
                elif newindex<allpos:
                    if self.relevancevector[newindex+allpos]==1: #si tengo el opuesto, no lo agrego y borro el otro.
                        self.relevancevector[newindex+allpos]=0
                    else:
                        self.relevancevector[newindex]=1 #si no tengo el opuesto, agrego este.
                else:
                    print 'what2?'
                    #return 'what2?'
                #El siguiente código sirve para que nunca tenga más de 5 argumentos.
                
                
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
                #El siguiente código sirve para que nunca tenga más de 5 argumentos.
                            
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
#                            if newindex==minpos:
#                                if newindex>allpos-1:
#                                    self.relevancevector[newindex-allpos]=0
#                                else:
#                                    self.relevancevector[newindex+allpos]=0   
                            else:
                                import random
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
                #El siguiente código sirve para que nunca tenga más de 5 argumentos.
                            
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
#                            if newindex==minpos:
#                                if newindex>allpos-1:
#                                    self.relevancevector[newindex-allpos]=0
#                                else:
#                                    self.relevancevector[newindex+allpos]=0   
                            else:
                                import random
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
                            


    def oldaddargument(self,newindex):
        if self.tipo==1:
            if self.relevancevector[newindex]==0 and self.recencyvector[newindex]==0:
                self.relevancevector[newindex]=1 #primero cambio la relevancia de este argumento
                self.recencyvector[newindex]=self.totalargs+1 #Ahora, preparo para que la recency de este argumento sea totalargs.
                for recency in range(len(self.recencyvector)):
                    if self.recencyvector[recency]>0:
                        self.recencyvector[recency]-=1 #con esto, le saco recency a todos los demás que no sean 0
                for recency in range(len(self.recencyvector)): #ahora, me fijo cuáles dejaron de ser relevantes y los cambio.
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
            #En el caso de que el argumento agregado sea uno que ya estaba, entonces hay que aumentarle a ese la
            #recency, y restarle -1 sólo a los que originalmente tenían más recency que ese. De esa forma se preserva
            #el número de argumentos.
        elif self.tipo==2:
            
                allpos=(len(self.relevancevector)/2)
                if newindex>allpos-1: #por ejemplo, 29.
                    if self.relevancevector[newindex-allpos]==1: #si tengo el opuesto, no lo agrego y borro el otro.
                        self.relevancevector[newindex-allpos]=0
                    else:
                        self.relevancevector[newindex]=1 #si no tengo el opuesto, agrego este.
                elif newindex<allpos:
                    if self.relevancevector[newindex+allpos]==1: #si tengo el opuesto, no lo agrego y borro el otro.
                        self.relevancevector[newindex+allpos]=0
                    else:
                        self.relevancevector[newindex]=1 #si no tengo el opuesto, agrego este.
                else:
                    print 'what2?'
                    #return 'what2?'       
                       
                                                                     
    def getsimilarity(self,Agent2):
        return 0.5*float((2-abs(self.getopinion()-Agent2.getopinion())))
        
    def newgetsimilarity(self,Agent2):
        return (1.0/6.0)*float((6.0-abs(self.getpersuasion()-Agent2.getpersuasion())))                
                
        

    