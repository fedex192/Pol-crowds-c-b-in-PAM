# -*- coding: utf-8 -*-
cpdef list choosinginteractingagents(list popu, int homo):  
    cdef:
         list probabilities, a
         int N, flag, k, agent, j
         double sumsim, sim    
    import numpy as np
    flag=0 
    N=len(popu)   
    i=np.random.randint(0,N)    
    while i==N:
        i=np.random.randint(0,N)
        
    sumsim=0    
    for k in range(N):
        if k!=i:
            sumsim+=(popu[i].newgetsimilarity(popu[k]))**homo
    #sumsim es la misma para todas las probas porque i está fijo. Lo que cambia es sim entre i y cada otro agente.
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
    if flag==0:        
        a=list(np.random.multinomial(1,probabilities))
        j=a.index(1)
        while j==i:
            a=list(np.random.multinomial(1,probabilities))
            j=a.index(1)
    else:
        j=0
    #obtengo el agente elegido.
    
    
    
    return [i,j,flag]