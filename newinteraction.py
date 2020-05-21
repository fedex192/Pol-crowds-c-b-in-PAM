# -*- coding: utf-8 -*-
def newargumentativeinteraction(popu, listofarguments, Cmax=3.0, intertype='Bid', cb='no',randomness='bidirectional',homo=0):
        '''This function executes one bidirectional pairwise interaction. popu is a population of agents; listofarguments is the
        list created before popu; cmax is the maximum value of persuasion; intertype is obsolete, it was used to choose between
        bidirectional and unidirectional interaction, default is bidirectional (and it was used for all simulations in the paper);
        cb determines the presence (cb='yes') or absence (cb='no') of confirmation bias; randomnes is obsolete, we deleted various
        cases we tested, and kept the one used for our simulations; it must be 'bidirectional' to work; finally, homo is the homophily 
        parameter, and determines the strenght of homophily (0 means homophily is not present).'''
        
        import random
        from choosinginteractingagents import choosinginteractingagents
        
        N=len(popu)
        
        #This function is used to choose which agents will interact; in the case of homo=0, it is equivalent to randomly choosing 2 agents from
        #the population.
        [i,j,flag]=choosinginteractingagents(popu, homo) #flag can be used for checking it works.
                
        agent1=popu[i]
        agent2=popu[j]
        
        totalargs=len(agent1.getrelevancevector()) #the relevance vector of both agents have the same lenght.
        
        if intertype=='Bid':#all other options were eliminated. It must be "Bid" for it to do something.
            
            #First Case: both agents have O=1
            if int(agent1.getopinion())==1 and int(agent2.getopinion())==1:
                #We only look at their positive arguments. We must check the strongest ones for each agent, and check that the other agent
                #does not already have it. If it does, we keep going over all the arguments the first agent has.
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
                #Add the new arguments (if any of the lists is empty, nothing will change for the receiving agent.
                
                
            #Second Case: both agents have O=-1
            elif int(agent1.getopinion())==-1 and int(agent2.getopinion())==-1:
                #Same as before, but this time, we look at the arguments with negative sign.
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
                
            #Third Case: opposing opinions (one agent has O=1, the other one has O=-1 (note that the conditionals in python work so that if 
            #the first and second cases are not true, it checks this condition, but does not enter it if it already entered one of the above.  
            elif agent1.getopinion()!=0 and agent2.getopinion()!=0:
                #the first two conditions do not change if confirmation bias is present, but this one does. That's why we need to account for
                #both conditions:
                
                #Without confirmation bias:
                if cb=='no':
                    #We look for the strongest positive argument for the agent with opinion 1, and the strongest negative argument for the
                    #agent with opinion -1. The procedure is then analogous to the previous two cases.
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
                        
                        agent1.addargument(agent2chosen) #Agent 1 receives the argument from agent 2, which is negative.
                        agent2.addargument(agent1chosen) #Agent 2 receives the argument from agent 1, which is positive.
                    
                    #This is the same as before, but for the case in which the first agent has O=-1, and the second one O=1.
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
                
                #With Confirmation Bias:                       
                if cb=='yes':
                    
                    #If any of the agents has only got arguments of the same sign as its opinion (e.g. the agent with O=1 only has positive arguments),
                    #then it won't give any argument to the other agent. But if it also has arguments of the opposite opinion (e.g., it also has negative
                    #arguments), then the other agent may receive one of them (assuming it has more weight than one of the arguments this second agent
                    #already has). 
                    
                    #This is a meaningless initialization:
                    agent1chosen=-1
                    agent2chosen=-1
                    
                    #We do the same process as before (for the cb='no' case):
                    
                    
                    #If agent 1 has O=1, and agent 2 has O=-1:
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
                        
                        #If agent 1 had an argument/s of the opposing opinion, it will pass it on to agent 2. Else, it will do nothing.
                        if agent1chosen!=-1:
                            agent2.addargument(agent1chosen) 
                        #The same thing happens if agent 2: if it had an argument/s of the opposing opinion, it will pass it on to agent 1. Else, it will do nothing.
                        if agent2chosen!=-1:
                            agent1.addargument(agent2chosen)
                            
                            
                    #the same process, but for the case in which agent 1 has O=-1, and agent 2 has O=1.                     
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

            #Fourth Case: both agents have O=0. Each will give the other a randomly selected argument. Of course, we check if that argument 
            #was already owned by the second agent, in which case we select another random argument, and so on. We repeat for the second agent.        
            elif int(agent1.getopinion())==0 and int(agent2.getopinion())==0:
                
                relvector1=agent1.getrelevancevector()
                relvector2=agent2.getrelevancevector()
                indexes1=[]
                indexes2=[]
                #To simplify the process, we start by listing all the arguments one agent has, but the other agent does not. 
                for argument in range(len(relvector1)):
                    
                    if relvector1[argument]==1 and relvector2[argument]==0:
                        indexes1.append(argument)
                    if relvector2[argument]==1 and relvector1[argument]==0:
                        indexes2.append(argument)
                
                #With both lists, we select a random argument. If both lists are not empty, both agents will receive an argument.        
                if indexes1!=[] and indexes2!=[]:         
                         
                    agent1chosen=random.choice(indexes1)
                    agent2chosen=random.choice(indexes2)  
                            
                    agent1.addargument(agent2chosen) #Al agente 1 le doy el argumento del 2, que es positivo.               
                    agent2.addargument(agent1chosen)
                
                # if one of the lists is empty, only one agent will receive an argument.
                elif  indexes1!=[] and indexes2==[]:
                    
                    agent1chosen=random.choice(indexes1)
                    agent2.addargument(agent1chosen)                           
                elif indexes1==[] and indexes2!=[]:
                    
                    agent2chosen=random.choice(indexes2)                         
                    agent1.addargument(agent2chosen)
                else:
                    pass #case in which both lists were empty: nothing happens.
            
            #Fifth and last case: one agent has opinion O!=0, and the other has opinion O=0. We originally tested various options for this
            #interaction, including unidirectional ones. We kept here only the one we used in the paper.
            else: 
                if randomness=='bidirectional':
                    
                    #For simplification, we find which agent is which; we call the oriented agent "dominant", and the moderate agent "nondominant".
                    
                    if int(agent1.getopinion())==1 or int(agent1.getopinion())==-1:
                        dominantagent=agent1
                        nondominantagent=agent2
                    else:
                        dominantagent=agent2
                        nondominantagent=agent1
                    
                    #We now consider separately the cases in which the oriented agent has O=1, or O=-1
                    
                    if dominantagent.getopinion()==1:
                        
                        #We extract the strongest positive argument from the oriented agent (not already owned by the moderate agent):
                        for arg in range(totalargs/2):
                            if dominantagent.getrelevancevector()[(totalargs/2-1)-arg]==1:
                                dominantagentchosen=(totalargs/2-1)-arg
                                if nondominantagent.getrelevancevector()[dominantagentchosen]!=1:
                                    break
                        #this was the same code used in previous cases.
                                                
                        nondominantagent.addargument(dominantagentchosen) #add that argument to the moderate agent.
                        
                        #Now, we choose a random argument from the moderate agent to add to the oriented agent. This is done in the same way
                        #as the previous case:
                        
                        dominantrelvector=dominantagent.getrelevancevector()
                        nondominantrelvector=nondominantagent.getrelevancevector()
                        indexes1=[]
                        
                        for argument in range(len(nondominantrelvector)):
                    
                            if dominantrelvector[argument]==0 and nondominantrelvector[argument]==1:
                                indexes1.append(argument)
                            
                        if indexes1!=[]:         
                         
                            nondominantagentchosen=random.choice(indexes1)
                            dominantagent.addargument(nondominantagentchosen)                        
                    
                    #We now consider the case in which the oriented agent has O=-1. The code is almost the same as before.    
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
         
            
            #Now that all possible cases of interaction have been adressed, and the corresponding arguments exchanged, we make use of 
            #the changepersuasion method of the Argumentativeagent class. This will ensure that persuasion is updated after argument exchange.                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                
            a=agent1.changepersuasion(listofarguments,Cmax)           
            b=agent2.changepersuasion(listofarguments,Cmax)

#Final remark: some checks carried out to ensure that this code worked correctly were omitted, to make the code easier to understand.