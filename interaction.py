# -*- coding: utf-8 -*-
def interaction(agent1, agent2, delta, k=2):
        """
        Computes changes in persuasion (and opinion if necessary) after interacting 
        with another person.
        Agent2 must be of class Agent.
        k determines de assymetrical interaction between an undecided (opinion=0) person,
        and a decided person. Default is 2.
        
        This function won't check for possible errors in the simulation, like interaction
        with oneself, so this must be prevented beforehand.
        """

        
            
        prepersuasion1=agent1.getpersuasion()
        prepersuasion2=agent2.getpersuasion()
        
        if agent1.getopinion()==agent2.getopinion():
            case=1
        elif agent1.getopinion()!=0 and agent2.getopinion()!=0:
            case=2
        else:
            case=3
            
        ismax=(prepersuasion1>prepersuasion2)
        if case==1 and abs(prepersuasion1-prepersuasion2)<delta:
            delta=abs(prepersuasion1-prepersuasion2)/2.0
        
        agent1.change(delta,k,case,ismax)
        agent2.change(delta,k,case,not ismax)
        
def masinteraction(popu,listofarguments,h=9):
    #Notar que esta vez se actualiza la opinión de un sólo agente por interacción de un par.
    #i: index of the agent; use random to choose him.
    #a: "coin toss". If default is -1, because the first time you call it, you still haven't tossed anything.
    import numpy as np
    import random
    N=len(popu)   
    i=random.randint(0,N)    
    while i==N:
        i=random.randint(0,N)
        
    sumsim=0    
    for k in range(N):
        if k!=i:
            sumsim+=(popu[i].getsimilarity(popu[k]))**h
    #sumsim es la misma para todas las probas porque i está fijo. Lo que cambia es sim entre i y cada otro agente.
    probabilities=[]
    for agent in range(N):
        if agent!=i:
            sim=popu[i].getsimilarity(popu[agent])
            probabilities.append(float((sim**h))/float(sumsim))
            
    
    a=np.random.multinomial(1,probabilities) #obtengo el agente elegido.
    
    for element in range(len(a)):
        if a[element]==1:
            
            if element>=i:
                relvector=popu[element+1].getrelevancevector()
            else:
                relvector=popu[element].getrelevancevector()
            
            chosen=random.randrange(0,sum(relvector))#al hacer la suma, obtengo el número de args relevantes.
            while chosen==sum(relvector):
                chosen=random.randrange(0,sum(relvector))
                
            for argument in range(len(relvector)):
                if relvector[argument]==1:
                    if chosen==0:
                        trueargument=argument
                        break
                    else:
                        chosen-=1
        #De esta forma, itero sobre los argumentos; si el argumento en el que estoy no es relevante, no hago nada;
        #si sí es relevante, me fijo si es el elegido; sino, sé que el elegido está a un argumento relevante menos
        #de distancia que antes, porque avancé sobre un argumento relevante. Le saco uno, y sigo.
            popu[i].addargument(trueargument)
            popu[i].changepersuasion(listofarguments)
            break
            #print 'good'

def oldargumentativeinteraction(popu, listofarguments, Cmax=3.0, intertype='Bid', cb='no'):
        import numpy as np
        import random
        N=len(popu)   
        i=random.randint(0,N)
        j=random.randint(0,N)    
        while i==N or j==N or i==j:
            i=random.randint(0,N)
            j=random.randint(0,N)  
        
        agent1=popu[i]
        agent2=popu[j]
        
        totalargs=len(agent1.getrelevancevector())
        
        if intertype=='Bid':
            #Caso Dos Positivos
            if int(agent1.getopinion())==1 and int(agent2.getopinion())==1:
            #Busco el argumento de más impacto para cada agente, y corroboro que el otro no lo tiene aún.
                agent1chosen=[]
                agent2chosen=[]
                for arg in range(totalargs/2):
                    if agent1.getrelevancevector()[(totalargs/2-1)-arg]==1:
                        agent1chosen=(totalargs/2-1)-arg
                        if agent2.getrelevancevector()[agent1chosen]!=1:
                            break
                for arg in range(totalargs/2):
                    if agent2.getrelevancevector()[(totalargs/2-1)-arg]==1:
                        agent2chosen=(totalargs/2-1)-arg
                        if agent1.getrelevancevector()[agent2chosen]!=1:
                            break
                agent1.addargument(agent2chosen)
                agent2.addargument(agent1chosen)
            #Caso Dos Negativos               
            elif int(agent1.getopinion())==-1 and int(agent2.getopinion())==-1:
            #Busco el argumento de más impacto para cada agente, y corroboro que el otro no lo tiene aún.
                for arg in range(totalargs/2):
                    if agent1.getrelevancevector()[(totalargs-1)-arg]==1:
                        agent1chosen=(totalargs-1)-arg
                        if agent2.getrelevancevector()[agent1chosen]!=1:
                            break
                for arg in range(totalargs/2):
                    if agent2.getrelevancevector()[(totalargs-1)-arg]==1:
                        agent2chosen=(totalargs-1)-arg
                        if agent1.getrelevancevector()[agent2chosen]!=1:
                            break
                
                agent1.addargument(agent2chosen)
                agent2.addargument(agent1chosen)  
                
            #Caso Uno Positivo y Uno Negativo.    
            elif agent1.getopinion()!=0 and agent2.getopinion()!=0:
                if cb=='no':
                    if agent1.getopinion()==1:
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                agent1chosen=(totalargs/2-1)-arg
                                if agent2.getrelevancevector()[agent1chosen]!=1:
                                    break
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs-1)-arg]==1:
                                agent2chosen=(totalargs-1)-arg
                                if agent1.getrelevancevector()[agent2chosen]!=1:
                                    break    
                        
                        agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es negativo.     
                        agent2.addargument(agent1chosen)   #Al agente 2 le doy el argumento del 1, que es positivo.  
                        
                    else:                    
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs-1)-arg]==1:
                                agent1chosen=(totalargs-1)-arg
                                if agent2.getrelevancevector()[agent1chosen]!=1:
                                    break                    
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                agent2chosen=(totalargs/2-1)-arg
                                if agent1.getrelevancevector()[agent2chosen]!=1:
                                    break  
                                              
                        agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                        agent2.addargument(agent1chosen) #Al agente 2 le doy el argumento del 1, que es negativo.      
                                       
                if cb=='yes':
                    
                    agent1chosen=-1
                    agent2chosen=-1
                    
                    if agent1.getopinion()==1:
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs-1)-arg]==1:
                                if agent2.getrelevancevector()[(totalargs-1)-arg]!=1:
                                    agent1chosen=(totalargs-1)-arg
                                    break
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                if agent1.getrelevancevector()[(totalargs/2-1)-arg]!=1:
                                    agent2chosen=(totalargs/2-1)-arg
                                    break    
                        
                        if agent1chosen!=-1:
                            agent2.addargument(agent1chosen) 
                        if agent2chosen!=-1:
                            agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es negativo.     
                          #Al agente 2 le doy el argumento del 1, que es positivo.                          
                    else:                    
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs-1)-arg]==1:
                                if agent1.getrelevancevector()[(totalargs-1)-arg]!=1:
                                    agent2chosen=(totalargs-1)-arg
                                    break
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                if agent2.getrelevancevector()[(totalargs/2-1)-arg]!=1:
                                    agent1chosen=(totalargs/2-1)-arg
                                    break    
                        
                        if agent1chosen!=-1:
                            agent2.addargument(agent1chosen) #Al agente 1 le doy el argumento del 2, que es positivo.
                        if agent2chosen!=-1:
                            agent1.addargument(agent2chosen) #Al agente 2 le doy el argumento del 1, que es negativo.     

                    
            elif int(agent1.getopinion())==0 and int(agent2.getopinion())==0:
                
                relvector1=agent1.getrelevancevector()
                relvector2=agent2.getrelevancevector()
                indexes1=[]
                indexes2=[]
                for argument in range(len(relvector1)):
                    
                    if relvector1[argument]==1 and relvector2[argument]==0:
                        indexes1.append(argument)
                    if relvector2[argument]==1 and relvector1[argument]==0:
                        indexes2.append(argument)
                        
                if indexes1!=[] and indexes2!=[]:         
                         
                    agent1chosen=random.choice(indexes1)
                    agent2chosen=random.choice(indexes2)  
                            
                    agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                    agent2.addargument(agent1chosen)
                      
                elif  indexes1!=[] and indexes2==[]:
                    
                    agent1chosen=random.choice(indexes1)
                    agent2.addargument(agent1chosen)    
                        
                elif indexes1==[] and indexes2!=[]:
                    
                    agent2chosen=random.choice(indexes2)                         
                    agent1.addargument(agent2chosen)
                else:
                    pass
            
            else:
                if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                    dominantagent=agent1
                    nondominantagent=agent2
                else:
                    dominantagent=agent2
                    nondominantagent=agent1
                
                if dominantagent.getopinion()==1:
                    
                    for arg in range(totalargs/2):
                        if dominantagent.getrelevancevector()[(totalargs/2-1)-arg]==1:
                            dominantagentchosen=(totalargs/2-1)-arg
                            if nondominantagent.getrelevancevector()[dominantagentchosen]!=1:
                                break
                                
                    nondominantagent.addargument(dominantagentchosen)
                    
                elif dominantagent.getopinion()==-1:
                
                    for arg in range(totalargs/2):
                        if dominantagent.getrelevancevector()[(totalargs-1)-arg]==1:
                            dominantagentchosen=(totalargs-1)-arg
                            if nondominantagent.getrelevancevector()[dominantagentchosen]!=1:
                                break   
                     
                    nondominantagent.addargument(dominantagentchosen)       
             
            a=agent1.changepersuasion(listofarguments,Cmax)           
            b=agent2.changepersuasion(listofarguments,Cmax)
            if a!=None:
                print a
            if b!=None:
                print b
            # - Poner en la población que distintos agentes pueden tener distinto número de argumentos iniciales.



def argumentativeinteraction(popu, listofarguments, Cmax=3.0, intertype='Bid', cb='no',randomness='no'):
        #randomness puede ser 'full', 'yes', o 'no'.
        import random
        N=len(popu)   
        i=random.randint(0,N)
        j=random.randint(0,N)    
        while i==N or j==N or i==j:
            i=random.randint(0,N)
            j=random.randint(0,N)  
        
        agent1=popu[i]
        agent2=popu[j]
        
        totalargs=len(agent1.getrelevancevector())
        
        if intertype=='Bid':
            #Caso Dos Positivos
            if int(agent1.getopinion())==1 and int(agent2.getopinion())==1:
            #Busco el argumento de más impacto para cada agente, y corroboro que el otro no lo tiene aún.
                agent1chosen=[]
                agent2chosen=[]
                for arg in range(totalargs/2):
                    if agent1.getrelevancevector()[(totalargs/2-1)-arg]==1:
                        agent1chosen=(totalargs/2-1)-arg
                        if agent2.getrelevancevector()[agent1chosen]!=1:
                            break
                for arg in range(totalargs/2):
                    if agent2.getrelevancevector()[(totalargs/2-1)-arg]==1:
                        agent2chosen=(totalargs/2-1)-arg
                        if agent1.getrelevancevector()[agent2chosen]!=1:
                            break
                agent1.addargument(agent2chosen)
                agent2.addargument(agent1chosen)
            #Caso Dos Negativos               
            elif int(agent1.getopinion())==-1 and int(agent2.getopinion())==-1:
            #Busco el argumento de más impacto para cada agente, y corroboro que el otro no lo tiene aún.
                for arg in range(totalargs/2):
                    if agent1.getrelevancevector()[(totalargs-1)-arg]==1:
                        agent1chosen=(totalargs-1)-arg
                        if agent2.getrelevancevector()[agent1chosen]!=1:
                            break
                for arg in range(totalargs/2):
                    if agent2.getrelevancevector()[(totalargs-1)-arg]==1:
                        agent2chosen=(totalargs-1)-arg
                        if agent1.getrelevancevector()[agent2chosen]!=1:
                            break
                
                agent1.addargument(agent2chosen)
                agent2.addargument(agent1chosen)  
                
            #Caso Uno Positivo y Uno Negativo.    
            elif agent1.getopinion()!=0 and agent2.getopinion()!=0:
                if cb=='no':
                    if agent1.getopinion()==1:
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                agent1chosen=(totalargs/2-1)-arg
                                if agent2.getrelevancevector()[agent1chosen]!=1:
                                    break
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs-1)-arg]==1:
                                agent2chosen=(totalargs-1)-arg
                                if agent1.getrelevancevector()[agent2chosen]!=1:
                                    break    
                        
                        agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es negativo.     
                        agent2.addargument(agent1chosen)   #Al agente 2 le doy el argumento del 1, que es positivo.  
                        
                    else:                    
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs-1)-arg]==1:
                                agent1chosen=(totalargs-1)-arg
                                if agent2.getrelevancevector()[agent1chosen]!=1:
                                    break                    
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                agent2chosen=(totalargs/2-1)-arg
                                if agent1.getrelevancevector()[agent2chosen]!=1:
                                    break  
                                              
                        agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                        agent2.addargument(agent1chosen) #Al agente 2 le doy el argumento del 1, que es negativo.      
                                       
                if cb=='yes':
                    
                    agent1chosen=-1
                    agent2chosen=-1
                    
                    if agent1.getopinion()==1:
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs-1)-arg]==1:
                                if agent2.getrelevancevector()[(totalargs-1)-arg]!=1:
                                    agent1chosen=(totalargs-1)-arg
                                    break
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                if agent1.getrelevancevector()[(totalargs/2-1)-arg]!=1:
                                    agent2chosen=(totalargs/2-1)-arg
                                    break    
                        
                        if agent1chosen!=-1:
                            agent2.addargument(agent1chosen) 
                        if agent2chosen!=-1:
                            agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es negativo.     
                          #Al agente 2 le doy el argumento del 1, que es positivo.                          
                    else:                    
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs-1)-arg]==1:
                                if agent1.getrelevancevector()[(totalargs-1)-arg]!=1:
                                    agent2chosen=(totalargs-1)-arg
                                    break
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                if agent2.getrelevancevector()[(totalargs/2-1)-arg]!=1:
                                    agent1chosen=(totalargs/2-1)-arg
                                    break    
                        
                        if agent1chosen!=-1:
                            agent2.addargument(agent1chosen) #Al agente 1 le doy el argumento del 2, que es positivo.
                        if agent2chosen!=-1:
                            agent1.addargument(agent2chosen) #Al agente 2 le doy el argumento del 1, que es negativo.     

                    
            elif int(agent1.getopinion())==0 and int(agent2.getopinion())==0:
                
                relvector1=agent1.getrelevancevector()
                relvector2=agent2.getrelevancevector()
                indexes1=[]
                indexes2=[]
                for argument in range(len(relvector1)):
                    
                    if relvector1[argument]==1 and relvector2[argument]==0:
                        indexes1.append(argument)
                    if relvector2[argument]==1 and relvector1[argument]==0:
                        indexes2.append(argument)
                        
                if indexes1!=[] and indexes2!=[]:         
                         
                    agent1chosen=random.choice(indexes1)
                    agent2chosen=random.choice(indexes2)  
                            
                    agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                    agent2.addargument(agent1chosen)
                      
                elif  indexes1!=[] and indexes2==[]:
                    
                    agent1chosen=random.choice(indexes1)
                    agent2.addargument(agent1chosen)    
                        
                elif indexes1==[] and indexes2!=[]:
                    
                    agent2chosen=random.choice(indexes2)                         
                    agent1.addargument(agent2chosen)
                else:
                    pass
            
            else:
                if randomness=='full': #caso en el que el decidido le da un argumento aleatorio al indeciso.
                    if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                        dominantagent=agent1
                        nondominantagent=agent2
                    else:
                        dominantagent=agent2
                        nondominantagent=agent1
                    
                    relvector1=dominantagent.getrelevancevector()
                    relvector2=nondominantagent.getrelevancevector()
                    indexes=[]
                    
                    if dominantagent.getopinion()==1:
                        
                        for argument in range(totalargs/2):
    
                            if relvector1[argument]==1 and relvector2[argument]==0:
                                indexes.append(argument)
                        
                        if indexes!=[]:        
                            dominantagentchosen=random.choice(indexes)            
                            nondominantagent.addargument(dominantagentchosen)
                        
                    elif dominantagent.getopinion()==-1:
                    
                        for argument in range(totalargs/2,totalargs):
    
                            if relvector1[argument]==1 and relvector2[argument]==0:
                                indexes.append(argument)           
                        
                        if indexes!=[]:                    
                            dominantagentchosen=random.choice(indexes)                      
                            nondominantagent.addargument(dominantagentchosen)  
                
                elif randomness=='yes': #Caso en el que el decidido le da un argumento aleatorio entre los que sean más fuerte que el más débil del indeciso (de la misma valencia)
                    if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                        dominantagent=agent1
                        nondominantagent=agent2
                    else:
                        dominantagent=agent2
                        nondominantagent=agent1
                    
                    if dominantagent.getopinion()==1:
                        #me fijo cuál es el más débil del indeciso, de valencia 1, y hago un random sobre los 
                        #que tiene el decidido, con mayor impacto que ese (también de valencia 1).
                        dominantindexes=[]
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[arg]==1:
                                dominantindexes.append(arg)
                       
                        nondominantminindex=[]
                        for arg in range(totalargs/2):
                            if nondominantagent.getrelevancevector()[arg]==1:
                                nondominantminindex=arg  
                                break                      
                        
                        selectedindexes=[]
                        if nondominantminindex!=[]:
                            for index in dominantindexes:
                                if index>nondominantminindex:
                                    selectedindexes.append(index)

                            if selectedindexes!=[]:
                                dominantagentchosen=random.choice(selectedindexes)
                                
                        else:
                            dominantagentchosen=random.choice(dominantindexes)
                        
                        #con esto, seleccioné un argumento aleatorio de los del decidido que tengan más impacto que el de menor impacto del indeciso.
                        
                                

                                    
                        nondominantagent.addargument(dominantagentchosen)
                        
                    elif dominantagent.getopinion()==-1:
                    
                        dominantindexes=[]
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[totalargs/2+arg]==1:
                                dominantindexes.append(totalargs/2+arg)
                       
                        nondominantminindex=[]
                        for arg in range(totalargs/2):
                            if nondominantagent.getrelevancevector()[totalargs/2+arg]==1:
                                nondominantminindex=totalargs/2+arg  
                                break                      
                        
                        selectedindexes=[]
                        if nondominantminindex!=[]:
                            for index in dominantindexes:
                                if index>nondominantminindex:
                                    selectedindexes.append(index)

                            if selectedindexes!=[]:
                                dominantagentchosen=random.choice(selectedindexes)
                                
                        else:
                            dominantagentchosen=random.choice(dominantindexes)

                       
                        nondominantagent.addargument(dominantagentchosen)       
    
                elif randomness=='bidirectional':
                    
                    if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                        dominantagent=agent1
                        nondominantagent=agent2
                    else:
                        dominantagent=agent2
                        nondominantagent=agent1
                    
                    if dominantagent.getopinion()==1:
                        
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                dominantagentchosen=(totalargs/2-1)-arg
                                if nondominantagent.getrelevancevector()[dominantagentchosen]!=1:
                                    break
                                    
                        nondominantagent.addargument(dominantagentchosen)
                        
                        dominantrelvector=dominantagent.getrelevancevector()
                        nondominantrelvector=nondominantagent.getrelevancevector()
                        indexes1=[]
                        
                        for argument in range(len(nondominantrelvector)):
                    
                            if dominantrelvector[argument]==0 and nondominantrelvector[argument]==1:
                                indexes1.append(argument)
                            
                        if indexes1!=[]:         
                         
                            nondominantagentchosen=random.choice(indexes1)
                            dominantagent.addargument(nondominantagentchosen)                        
                        
                    elif dominantagent.getopinion()==-1:
                    
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[(totalargs-1)-arg]==1:
                                dominantagentchosen=(totalargs-1)-arg
                                if nondominantagent.getrelevancevector()[dominantagentchosen]!=1:
                                    break   
                        
                        nondominantagent.addargument(dominantagentchosen)   
                        
                        dominantrelvector=dominantagent.getrelevancevector()
                        nondominantrelvector=nondominantagent.getrelevancevector()
                        indexes1=[]
                        
                        for argument in range(len(nondominantrelvector)):
                    
                            if dominantrelvector[argument]==0 and nondominantrelvector[argument]==1:
                                indexes1.append(argument)
                            
                        if indexes1!=[]:         
                         
                            nondominantagentchosen=random.choice(indexes1)
                            dominantagent.addargument(nondominantagentchosen)        
                        
                    else:       
                        print 'totally wrong'
                    
                
                else: #caso en el que el decidido le da el más fuerte suyo que el indeciso no tenga.

                    if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                        dominantagent=agent1
                        nondominantagent=agent2
                    else:
                        dominantagent=agent2
                        nondominantagent=agent1
                    
                    if dominantagent.getopinion()==1:
                        
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                dominantagentchosen=(totalargs/2-1)-arg
                                if nondominantagent.getrelevancevector()[dominantagentchosen]!=1:
                                    break
                                    
                        nondominantagent.addargument(dominantagentchosen)
                        
                    elif dominantagent.getopinion()==-1:
                    
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[(totalargs-1)-arg]==1:
                                dominantagentchosen=(totalargs-1)-arg
                                if nondominantagent.getrelevancevector()[dominantagentchosen]!=1:
                                    break   
                        
                        nondominantagent.addargument(dominantagentchosen)          
                        
                    else:       
                        print 'totally wrong'
                                                            
                                                                                                                        
                
            a=agent1.changepersuasion(listofarguments,Cmax)           
            b=agent2.changepersuasion(listofarguments,Cmax)
            if a!=None:
                print a
            if b!=None:
                print b
            # - Poner en la población que distintos agentes pueden tener distinto número de argumentos iniciales.



def argumentativeinteractioncontraryflux(popu, listofarguments, Cmax=3.0, intertype='Bid', cb='no',randomness='no'):
        #randomness puede ser 'full', 'yes', o 'no'.
        import random
        N=len(popu)   
        i=random.randint(0,N)
        j=random.randint(0,N)    
        while i==N or j==N or i==j:
            i=random.randint(0,N)
            j=random.randint(0,N)  
        
        agent1=popu[i]
        agent2=popu[j]
        
        totalargs=len(agent1.getrelevancevector())
        fluxflag=0
        
        if intertype=='Bid':
            #Caso Dos Positivos
            if int(agent1.getopinion())==1 and int(agent2.getopinion())==1:
            #Busco el argumento de más impacto para cada agente, y corroboro que el otro no lo tiene aún.
                agent1chosen=[]
                agent2chosen=[]
                for arg in range(totalargs/2):
                    if agent1.getrelevancevector()[(totalargs/2-1)-arg]==1:
                        agent1chosen=(totalargs/2-1)-arg
                        if agent2.getrelevancevector()[agent1chosen]!=1:
                            break
                for arg in range(totalargs/2):
                    if agent2.getrelevancevector()[(totalargs/2-1)-arg]==1:
                        agent2chosen=(totalargs/2-1)-arg
                        if agent1.getrelevancevector()[agent2chosen]!=1:
                            break
                agent1.addargument(agent2chosen)
                agent2.addargument(agent1chosen)
            #Caso Dos Negativos               
            elif int(agent1.getopinion())==-1 and int(agent2.getopinion())==-1:
            #Busco el argumento de más impacto para cada agente, y corroboro que el otro no lo tiene aún.
                for arg in range(totalargs/2):
                    if agent1.getrelevancevector()[(totalargs-1)-arg]==1:
                        agent1chosen=(totalargs-1)-arg
                        if agent2.getrelevancevector()[agent1chosen]!=1:
                            break
                for arg in range(totalargs/2):
                    if agent2.getrelevancevector()[(totalargs-1)-arg]==1:
                        agent2chosen=(totalargs-1)-arg
                        if agent1.getrelevancevector()[agent2chosen]!=1:
                            break
                
                agent1.addargument(agent2chosen)
                agent2.addargument(agent1chosen)  
                
            #Caso Uno Positivo y Uno Negativo.    
            elif agent1.getopinion()!=0 and agent2.getopinion()!=0:
                if cb=='no':
                    fluxflag=1
                    if agent1.getopinion()==1:
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                agent1chosen=(totalargs/2-1)-arg
                                if agent2.getrelevancevector()[agent1chosen]!=1:
                                    break
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs-1)-arg]==1:
                                agent2chosen=(totalargs-1)-arg
                                if agent1.getrelevancevector()[agent2chosen]!=1:
                                    break    
                        
                        agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es negativo.     
                        agent2.addargument(agent1chosen)   #Al agente 2 le doy el argumento del 1, que es positivo.  
                        
                    else:                    
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs-1)-arg]==1:
                                agent1chosen=(totalargs-1)-arg
                                if agent2.getrelevancevector()[agent1chosen]!=1:
                                    break                    
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                agent2chosen=(totalargs/2-1)-arg
                                if agent1.getrelevancevector()[agent2chosen]!=1:
                                    break  
                                              
                        agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                        agent2.addargument(agent1chosen) #Al agente 2 le doy el argumento del 1, que es negativo.      
                               
                if cb=='yes':
                    agent1chosen=-1
                    agent2chosen=-1
                    
                    if agent1.getopinion()==1:
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs-1)-arg]==1:
                                if agent2.getrelevancevector()[(totalargs-1)-arg]!=1:
                                    agent1chosen=(totalargs-1)-arg
                                    break
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                if agent1.getrelevancevector()[(totalargs/2-1)-arg]!=1:
                                    agent2chosen=(totalargs/2-1)-arg
                                    break    
                        
                        if agent1chosen!=-1:
                            agent2.addargument(agent1chosen) 
                        if agent2chosen!=-1:
                            agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es negativo.     
                          #Al agente 2 le doy el argumento del 1, que es positivo.                          
                    else:                    
                        for arg in range(totalargs/2):
                            if agent2.getrelevancevector()[(totalargs-1)-arg]==1:
                                if agent1.getrelevancevector()[(totalargs-1)-arg]!=1:
                                    agent2chosen=(totalargs-1)-arg
                                    break
                        for arg in range(totalargs/2):
                            if agent1.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                if agent2.getrelevancevector()[(totalargs/2-1)-arg]!=1:
                                    agent1chosen=(totalargs/2-1)-arg
                                    break    
                        
                        if agent1chosen!=-1:
                            agent2.addargument(agent1chosen) #Al agente 1 le doy el argumento del 2, que es positivo.
                        if agent2chosen!=-1:
                            agent1.addargument(agent2chosen) #Al agente 2 le doy el argumento del 1, que es negativo.     

            elif int(agent1.getopinion())==0 and int(agent2.getopinion())==0:
                
                relvector1=agent1.getrelevancevector()
                relvector2=agent2.getrelevancevector()
                indexes1=[]
                indexes2=[]
                for argument in range(len(relvector1)):
                    
                    if relvector1[argument]==1 and relvector2[argument]==0:
                        indexes1.append(argument)
                    if relvector2[argument]==1 and relvector1[argument]==0:
                        indexes2.append(argument)
                        
                if indexes1!=[] and indexes2!=[]:         
                         
                    agent1chosen=random.choice(indexes1)
                    agent2chosen=random.choice(indexes2)  
                            
                    agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                    agent2.addargument(agent1chosen)
                      
                elif  indexes1!=[] and indexes2==[]:
                    
                    agent1chosen=random.choice(indexes1)
                    agent2.addargument(agent1chosen)    
                        
                elif indexes1==[] and indexes2!=[]:
                    
                    agent2chosen=random.choice(indexes2)                         
                    agent1.addargument(agent2chosen)
                else:
                    pass
            
            else:
                if randomness=='full': #caso en el que el decidido le da un argumento aleatorio al indeciso.
                    if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                        dominantagent=agent1
                        nondominantagent=agent2
                    else:
                        dominantagent=agent2
                        nondominantagent=agent1
                    
                    relvector1=dominantagent.getrelevancevector()
                    relvector2=nondominantagent.getrelevancevector()
                    indexes=[]
                    
                    if dominantagent.getopinion()==1:
                        
                        for argument in range(totalargs/2):
    
                            if relvector1[argument]==1 and relvector2[argument]==0:
                                indexes.append(argument)
                        
                        if indexes!=[]:        
                            dominantagentchosen=random.choice(indexes)            
                            nondominantagent.addargument(dominantagentchosen)
                        
                    elif dominantagent.getopinion()==-1:
                    
                        for argument in range(totalargs/2,totalargs):
    
                            if relvector1[argument]==1 and relvector2[argument]==0:
                                indexes.append(argument)           
                        
                        if indexes!=[]:                    
                            dominantagentchosen=random.choice(indexes)                      
                            nondominantagent.addargument(dominantagentchosen)  
                
                elif randomness=='yes': #Caso en el que el decidido le da un argumento aleatorio entre los que sean más fuerte que el más débil del indeciso (de la misma valencia)
                    if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                        dominantagent=agent1
                        nondominantagent=agent2
                    else:
                        dominantagent=agent2
                        nondominantagent=agent1
                    
                    if dominantagent.getopinion()==1:
                        #me fijo cuál es el más débil del indeciso, de valencia 1, y hago un random sobre los 
                        #que tiene el decidido, con mayor impacto que ese (también de valencia 1).
                        dominantindexes=[]
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[arg]==1:
                                dominantindexes.append(arg)
                       
                        nondominantminindex=[]
                        for arg in range(totalargs/2):
                            if nondominantagent.getrelevancevector()[arg]==1:
                                nondominantminindex=arg  
                                break                      
                        
                        selectedindexes=[]
                        if nondominantminindex!=[]:
                            for index in dominantindexes:
                                if index>nondominantminindex:
                                    selectedindexes.append(index)

                            if selectedindexes!=[]:
                                dominantagentchosen=random.choice(selectedindexes)
                                
                        else:
                            dominantagentchosen=random.choice(dominantindexes)
                        
                        #con esto, seleccioné un argumento aleatorio de los del decidido que tengan más impacto que el de menor impacto del indeciso.
                        
                                

                                    
                        nondominantagent.addargument(dominantagentchosen)
                        
                    elif dominantagent.getopinion()==-1:
                    
                        dominantindexes=[]
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[totalargs/2+arg]==1:
                                dominantindexes.append(totalargs/2+arg)
                       
                        nondominantminindex=[]
                        for arg in range(totalargs/2):
                            if nondominantagent.getrelevancevector()[totalargs/2+arg]==1:
                                nondominantminindex=totalargs/2+arg  
                                break                      
                        
                        selectedindexes=[]
                        if nondominantminindex!=[]:
                            for index in dominantindexes:
                                if index>nondominantminindex:
                                    selectedindexes.append(index)

                            if selectedindexes!=[]:
                                dominantagentchosen=random.choice(selectedindexes)
                                
                        else:
                            dominantagentchosen=random.choice(dominantindexes)

                       
                        nondominantagent.addargument(dominantagentchosen)       
    
                elif randomness=='bidirectional':
                    
                    if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                        dominantagent=agent1
                        nondominantagent=agent2
                    else:
                        dominantagent=agent2
                        nondominantagent=agent1
                    
                    if dominantagent.getopinion()==1:
                        
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                dominantagentchosen=(totalargs/2-1)-arg
                                if nondominantagent.getrelevancevector()[dominantagentchosen]!=1:
                                    break
                                    
                        nondominantagent.addargument(dominantagentchosen)
                        
                        dominantrelvector=dominantagent.getrelevancevector()
                        nondominantrelvector=nondominantagent.getrelevancevector()
                        indexes1=[]
                        
                        for argument in range(len(nondominantrelvector)):
                    
                            if dominantrelvector[argument]==0 and nondominantrelvector[argument]==1:
                                indexes1.append(argument)
                            
                        if indexes1!=[]:         
                         
                            nondominantagentchosen=random.choice(indexes1)
                            dominantagent.addargument(nondominantagentchosen)                        
                        
                    elif dominantagent.getopinion()==-1:
                    
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[(totalargs-1)-arg]==1:
                                dominantagentchosen=(totalargs-1)-arg
                                if nondominantagent.getrelevancevector()[dominantagentchosen]!=1:
                                    break   
                        
                        nondominantagent.addargument(dominantagentchosen)   
                        
                        dominantrelvector=dominantagent.getrelevancevector()
                        nondominantrelvector=nondominantagent.getrelevancevector()
                        indexes1=[]
                        
                        for argument in range(len(nondominantrelvector)):
                    
                            if dominantrelvector[argument]==0 and nondominantrelvector[argument]==1:
                                indexes1.append(argument)
                            
                        if indexes1!=[]:         
                         
                            nondominantagentchosen=random.choice(indexes1)
                            dominantagent.addargument(nondominantagentchosen)        
                        
                    else:       
                        print 'totally wrong'
                    
                
                else: #caso en el que el decidido le da el más fuerte suyo que el indeciso no tenga.

                    if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                        dominantagent=agent1
                        nondominantagent=agent2
                    else:
                        dominantagent=agent2
                        nondominantagent=agent1
                    
                    if dominantagent.getopinion()==1:
                        
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                dominantagentchosen=(totalargs/2-1)-arg
                                if nondominantagent.getrelevancevector()[dominantagentchosen]!=1:
                                    break
                                    
                        nondominantagent.addargument(dominantagentchosen)
                        
                    elif dominantagent.getopinion()==-1:
                    
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[(totalargs-1)-arg]==1:
                                dominantagentchosen=(totalargs-1)-arg
                                if nondominantagent.getrelevancevector()[dominantagentchosen]!=1:
                                    break   
                        
                        nondominantagent.addargument(dominantagentchosen)          
                        
                    else:       
                        print 'totally wrong'
                                                            
                                                                                                                        
                
            a=agent1.changepersuasion(listofarguments,Cmax)           
            b=agent2.changepersuasion(listofarguments,Cmax)
            if a!=None:
                print a
            if b!=None:
                print b
                
            if fluxflag==0:
                return 0
            else:
                return 1,agent1chosen,agent2chosen    
            # - Poner en la población que distintos agentes pueden tener distinto número de argumentos iniciales.










def randomargumentativeinteraction(popu, listofarguments, Cmax=3.0, intertype='Bid', cb='no'):
        import numpy as np
        import random
        N=len(popu)   
        i=random.randint(0,N)
        j=random.randint(0,N)    
        while i==N or j==N or i==j:
            i=random.randint(0,N)
            j=random.randint(0,N)  
        
        agent1=popu[i]
        agent2=popu[j]
        
        totalargs=len(agent1.getrelevancevector())
        
        if intertype=='Bid':
            #Caso Dos Positivos
            if int(agent1.getopinion())==1 and int(agent2.getopinion())==1:
            #Busco el argumento de más impacto para cada agente, y corroboro que el otro no lo tiene aún.
                
                relvector1=agent1.getrelevancevector()
                relvector2=agent2.getrelevancevector()
                indexes1=[]
                indexes2=[]
                for argument in range(totalargs/2):
                    
                    if relvector1[argument]==1 and relvector2[argument]==0:
                        indexes1.append(argument)
                    if relvector2[argument]==1 and relvector1[argument]==0:
                        indexes2.append(argument)
                        
                if indexes1!=[] and indexes2!=[]:         
                         
                    agent1chosen=random.choice(indexes1)
                    agent2chosen=random.choice(indexes2)  
                            
                    agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                    agent2.addargument(agent1chosen)
                      
                elif  indexes1!=[] and indexes2==[]:
                    
                    agent1chosen=random.choice(indexes1)
                    agent2.addargument(agent1chosen)    
                        
                elif indexes1==[] and indexes2!=[]:
                    
                    agent2chosen=random.choice(indexes2)                         
                    agent1.addargument(agent2chosen)
                else:
                    pass                
            #Caso Dos Negativos               
            elif int(agent1.getopinion())==-1 and int(agent2.getopinion())==-1:
            #Busco el argumento de más impacto para cada agente, y corroboro que el otro no lo tiene aún.
                relvector1=agent1.getrelevancevector()
                relvector2=agent2.getrelevancevector()
                indexes1=[]
                indexes2=[]
                for argument in range(totalargs/2,totalargs):
                    
                    if relvector1[argument]==1 and relvector2[argument]==0:
                        indexes1.append(argument)
                    if relvector2[argument]==1 and relvector1[argument]==0:
                        indexes2.append(argument)
                        
                if indexes1!=[] and indexes2!=[]:         
                         
                    agent1chosen=random.choice(indexes1)
                    agent2chosen=random.choice(indexes2)  
                            
                    agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                    agent2.addargument(agent1chosen)
                      
                elif  indexes1!=[] and indexes2==[]:
                    
                    agent1chosen=random.choice(indexes1)
                    agent2.addargument(agent1chosen)    
                        
                elif indexes1==[] and indexes2!=[]:
                    
                    agent2chosen=random.choice(indexes2)                         
                    agent1.addargument(agent2chosen)
                else:
                    pass                
                
            #Caso Uno Positivo y Uno Negativo.    
            elif agent1.getopinion()!=0 and agent2.getopinion()!=0:                                        
                if cb=='yes':
                    
                    relvector1=agent1.getrelevancevector()
                    relvector2=agent2.getrelevancevector()
                    indexes1=[]
                    indexes2=[]
                    if agent1.getopinion()==1:
                        
                        for argument in range(totalargs/2,totalargs): #Del que es positivo saco un negativo
                    
                            if relvector1[argument]==1 and relvector2[argument]==0:
                                indexes1.append(argument)
                                
                        for argument in range(totalargs/2): #Del que es negativo saco un positivo.
                            if relvector2[argument]==1 and relvector1[argument]==0:
                                indexes2.append(argument)
                            
                        if indexes1!=[] and indexes2!=[]:         
                                
                            agent1chosen=random.choice(indexes1)
                            agent2chosen=random.choice(indexes2)  
                                    
                            agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                            agent2.addargument(agent1chosen)
                            
                        elif  indexes1!=[] and indexes2==[]:
                            
                            agent1chosen=random.choice(indexes1)
                            agent2.addargument(agent1chosen)    
                            
                        elif indexes1==[] and indexes2!=[]:
                            
                            agent2chosen=random.choice(indexes2)                         
                            agent1.addargument(agent2chosen)
                        else:
                            pass                
                        
                         
                    else:                    
                        
                        for argument in range(totalargs/2): #Del que es positivo saco un negativo
                    
                            if relvector1[argument]==1 and relvector2[argument]==0:
                                indexes1.append(argument)
                                
                        for argument in range(totalargs/2,totalargs): #Del que es negativo saco un positivo.
                            if relvector2[argument]==1 and relvector1[argument]==0:
                                indexes2.append(argument)
                            
                        if indexes1!=[] and indexes2!=[]:         
                                
                            agent1chosen=random.choice(indexes1)
                            agent2chosen=random.choice(indexes2)  
                                    
                            agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                            agent2.addargument(agent1chosen)
                            
                        elif  indexes1!=[] and indexes2==[]:
                            
                            agent1chosen=random.choice(indexes1)
                            agent2.addargument(agent1chosen)    
                            
                        elif indexes1==[] and indexes2!=[]:
                            
                            agent2chosen=random.choice(indexes2)                         
                            agent1.addargument(agent2chosen)
                        else:
                            pass        
                                       
            elif int(agent1.getopinion())==0 and int(agent2.getopinion())==0:
                
                relvector1=agent1.getrelevancevector()
                relvector2=agent2.getrelevancevector()
                indexes1=[]
                indexes2=[]
                for argument in range(len(relvector1)):
                    
                    if relvector1[argument]==1 and relvector2[argument]==0:
                        indexes1.append(argument)
                    if relvector2[argument]==1 and relvector1[argument]==0:
                        indexes2.append(argument)
                        
                if indexes1!=[] and indexes2!=[]:         
                         
                    agent1chosen=random.choice(indexes1)
                    agent2chosen=random.choice(indexes2)  
                            
                    agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                    agent2.addargument(agent1chosen)
                      
                elif  indexes1!=[] and indexes2==[]:
                    
                    agent1chosen=random.choice(indexes1)
                    agent2.addargument(agent1chosen)    
                        
                elif indexes1==[] and indexes2!=[]:
                    
                    agent2chosen=random.choice(indexes2)                         
                    agent1.addargument(agent2chosen)
                else:
                    pass
            
            else:
                if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                    dominantagent=agent1
                    nondominantagent=agent2
                else:
                    dominantagent=agent2
                    nondominantagent=agent1
                
                relvector1=dominantagent.getrelevancevector()
                relvector2=nondominantagent.getrelevancevector()
                indexes=[]
                
                if dominantagent.getopinion()==1:
                    
                    for argument in range(totalargs/2):

                        if relvector1[argument]==1 and relvector2[argument]==0:
                            indexes.append(argument)
                    
                    if indexes!=[]:        
                        dominantagentchosen=random.choice(indexes)            
                        nondominantagent.addargument(dominantagentchosen)
                    
                elif dominantagent.getopinion()==-1:
                
                    for argument in range(totalargs/2,totalargs):

                        if relvector1[argument]==1 and relvector2[argument]==0:
                            indexes.append(argument)           
                    
                    if indexes!=[]:                    
                        dominantagentchosen=random.choice(indexes)                      
                        nondominantagent.addargument(dominantagentchosen)       
             
            a=agent1.changepersuasion(listofarguments,Cmax)           
            b=agent2.changepersuasion(listofarguments,Cmax)
            if a!=None:
                print a
            if b!=None:
                print b
            # - Poner en la población que distintos agentes pueden tener distinto número de argumentos iniciales.



def masinteractionbeta(popu,listofarguments,i,h=9,a=-1):
    #Notar que esta vez se actualiza la opinión de un sólo agente por interacción de un par.
    #i: index of the agent; use random to choose him.
    #a: "coin toss". If default is -1, because the first time you call it, you still haven't tossed anything.
    import numpy as np
    import random
    N=len(popu)
#    j=np.random.randrange(0, N)
#    while j==i:
#       j=np.random.randrange(0, N)
#    if a==-1:
#        a=np.random.random() #coin toss
    
    probabilities=[]
    for agent in range(N):
        if agent!=i:
            sim=popu[i].getsimilarity(popu[agent])
            sumsim=0
            for k in range(N):
                if k!=i:
                    sumsim+=(popu[i].getsimilarity(popu[k]))**h
            probabilities.append(float((sim**h))/float(sumsim))
            
    
    a=np.random.multinomial(1,probabilities) #obtengo el agente elegido.
    for element in range(len(a)):
        if element==1:
#    if a<(float((sim**h))/float(sumsim))*99:
#        if (float((sim**h))/float(sumsim))*99>1:
#            print (float((sim**h))/float(sumsim))*99
            #elijo un argumento para intercambiar
            relvector=popu[element].getrelevancevector()
            chosen=random.randrange(0,sum(relvector)) #al hacer la suma, obtengo el número de args relevantes.
            for argument in range(len(relvector)):
                if relvector[argument]==1:
                    if chosen==0:
                        trueargument=argument
                        break
                    else:
                        chosen-=1
        #De esta forma, itero sobre los argumentos; si argumento en el que estoy no es relevante, no hago nada;
        #si sí es relevante, me fijo si es el elegido; sino, sé que el elegido está a un argumento relevante menos
        #de distancia que antes, porque avancé sobre un argumento relevante. Le saco uno, y sigo.
            popu[i].addargument(trueargument)
            popu[i].changepersuasion(listofarguments)
            print 'good'
    #else:   
       # masinteraction(popu,listofarguments,i,h,a) #I've already made the coin toss; I pass it down.
       