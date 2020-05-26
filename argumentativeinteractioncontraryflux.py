# -*- coding: utf-8 -*-
def argumentativeinteractioncontraryflux(popu, listofarguments, Cmax=3.0, intertype='Bid', cb='no',randomness='no'):
        '''This function is to be used exclusively with runargsimwithPCBcontraryflux found in ContraryFluxSimulation.py. It is
        a slightly modified version of argumentativeinteraction found in newinteraction.py. We will not be adding comments to this version,
        since changes are very few. Instead, we list the changes here:
        1) This was not designed to be used with homophily, so selection of both interacting agents is random.
        2) a new variable is created, called fluxflag, and set to 0. If the interaction is between two oriented agents of
        opposite opinion when confirmation bias is not present (the main case where there is contrary flux), fluxflag is set to 1.
        3) if fluxflag is 1, this function returns the number 1, and the arguments exchanged between the agents (either of which
        could be empty, if one agent did not transfer an argument to the other). If fluxflag is 0, this functions returns 0. 
        The reason we did not take into account the other possible case of interaction which could lead to contrary flux (when an 
        oriented agent interacts with a moderate agent and receives an argument opposite to its opinion) is because it affected both cases
        of presence and abscence of confirmation bias in the same way, and was an uncommon interaction (mainly found in the transitional first
        few interactions in the system). Once a bipolarization state is produced, that interaction is not present, and its stability is not 
        related to it. This made its inclusion irrelevant (however, we tried it, and including it does not change results).
        4) There is residual code used for testing that everything works, and other types of interactions other than bidirectional, which
        were originally studied, but not used for the paper. These were deleted in the clean argumentativeinteraction function of newinteraction.py.
        
        NOTE: posture is called persuasion in all this code.'''
            
            
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
            
            if int(agent1.getopinion())==1 and int(agent2.getopinion())==1:
            
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
                         
            elif int(agent1.getopinion())==-1 and int(agent2.getopinion())==-1:
            
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
                        
                        agent1.addargument(agent2chosen)
                        agent2.addargument(agent1chosen)
                        
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
                                              
                        agent1.addargument(agent2chosen)             
                        agent2.addargument(agent1chosen)     
                               
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
                            agent1.addargument(agent2chosen)     
                                                  
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
                            agent2.addargument(agent1chosen)
                        if agent2chosen!=-1:
                            agent1.addargument(agent2chosen)    

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
                            
                    agent1.addargument(agent2chosen)               
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
                if randomness=='full': 
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
                
                elif randomness=='yes': 
                    if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                        dominantagent=agent1
                        nondominantagent=agent2
                    else:
                        dominantagent=agent2
                        nondominantagent=agent1
                    
                    if dominantagent.getopinion()==1:

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