# -*- coding: utf-8 -*-
def newargumentativeinteraction(popu, listofarguments, Cmax=3.0, intertype='Bid', cb='no',randomness='no',homo=0):
        #randomness puede ser 'full', 'yes', o 'no'.
        import random
        from choosinginteractingagents import choosinginteractingagents
        
        N=len(popu)   
        # i=random.randint(0,N)
        # j=random.randint(0,N)    
        # while i==N or j==N or i==j:
        #     i=random.randint(0,N)
        #     j=random.randint(0,N)  
        [i,j,flag]=choosinginteractingagents(popu, homo)
        
        if flag==1:
            return 10101010
        
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