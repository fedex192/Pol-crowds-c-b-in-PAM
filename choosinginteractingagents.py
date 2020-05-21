# -*- coding: utf-8 -*-
def choosinginteractingagents(popu, homo):  
    '''This function is used to choose which agents in population popu will interact. The probability is affected by the intensity of
    the homophily, homo. If it is 0, it is equivalent to randomly choose two agents from the population.'''
    import random,numpy 
    
    #First, we randomly choose one agent. The while ensures that even if python rounds up so that i equals N, its final vanue will be <N. 
    flag=0 
    N=len(popu)   
    i=random.randint(0,N)    
    while i==N:
        i=random.randint(0,N)
    
        
    #Now, we calculate the denominator of the homophily calculation. Having fixed i beforehand, it is the same for all terms.            
    sumsim=0    
    for k in range(N):
        if k!=i:
            sumsim+=(popu[i].newgetsimilarity(popu[k]))**homo
   
    #the flag checks that everything works. It's unnecessary. The rest of the loop simply calculates the similarity and probability of interaction
    #between agent i and every other agent in the population.
    probabilities=[]
    for agent in range(N):
        if sumsim!=0:
            if agent!=i:
                sim=popu[i].newgetsimilarity(popu[agent])
                probabilities.append(float((sim**homo))/float(sumsim))
            else:
                probabilities.append(0.0)
        else:
            flag=1
    #If everything worked correctly, we proceed to drawing the second agent, using the previously calculated probabilities:
    if flag==0:        
        a=list(numpy.random.multinomial(1,probabilities))
        j=a.index(1)
        while j==i:
            a=list(numpy.random.multinomial(1,probabilities))
            j=a.index(1)
    else:
        j=0  
    
    #we return both chosen agents
    return [i,j,flag]