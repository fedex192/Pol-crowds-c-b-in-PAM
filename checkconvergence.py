# -*- coding: utf-8 -*-
def checkconvergence(popu,cb='no'):
    '''This function is used to check if the system has already converged or not (meaning it has reached one of the possible final states,
    and this state won't change anymore). It serves as an important part of newrunargsimforprofiling, our main simulation function, since it
    allows us to use a while loop, and use the necessary steps to converge, no more and no less. Its input is a population of agents popu, and
    the presence of confirmation bias (cb='yes') or its abscence (cb='no'). Since the final states are determined by looking only at the opinion
    of the agents, this is the main determinant of convergence: if opinions can't change, the system has converged (even if it would need some more
    steps to reach posture convergence. NOTE: postures are called persuasions in all the codes.'''
    import numpy as np
    
    #First, we get the persuasions of all the agents in the population
    persuasions=[]
    for i in range(len(popu)):
        persuasions.append(float(popu[i].getpersuasion()))
    
    #now we reduce the previous vector so that there are no repeated values.
    a=np.unique(persuasions)

    #Now come the conditions that check for convergence:
    if len(a)==1:
        convergence=True #if persuasion of all the agents is the same, the system has converged.
    elif len(a)==2:
        if float(abs(a[1]))==float(3) and float(abs(a[0]))==float(3): 
            convergence=True #if there are two values of persuasion, and they are 3 and -3, the system has converged (bipolarization. This final state is only found when there is homophily)
        elif np.sign(a[1])==np.sign(a[0]) and abs(a[1])>1 and abs(a[0])>1:
            convergence=True #if the sign of both values of persuasion is the same, and they are both higher than one (absolute value), all agents have O=1, or all agents have O=-1, and there is no way these opinions could change, due tu the rules of interaction. 
        else:
            convergence=False #for two values of persuasion, those are the only ways there could be convergence, unless there is confirmation bias.
        if cb=='yes': #if there is confirmation bias:
            if np.sign(a[1])!=np.sign(a[0]) and abs(a[1])>1 and abs(a[0])>1: 
                convergence=True #if the sign is opposite, but both persuasions are greater than one, then some agents (at least 1) have one opinion, and the rest have the other opinion. If CB is present, then opinions can only be reinforced from this point forward, and thus, the final state has been found (some more steps could be needed for complete convergence of persuasion)
    else:
        #there are more than 2 unique values of persuasion. Then:          
        if len(np.unique(np.sign(a)))==1 and len(np.unique(abs(np.array(a))>1))==1:
            convergence=True #if all the values of persuasion have the same sign, and are all greater than one (in absolute value), then all agents have the same opinion. This means the system has converged.
        else:
            convergence=False #this time, this is the only condition that ensures convergence of opinions if CB is absent.
            
        if cb=='yes': #if there is confirmation bias:
            if len(np.unique(np.sign(a)))==2 and sum((abs(np.array(a))>1))==len(a): #Si hay CB, y están los dos signos, pero son todos orientados, ya convergieron.
                convergence=True #if both signs are present, but all the agents have persuasion greater than 1 (in absolute value), then all have either O=1 or O=-1. With CB, this means that their opinions can only be reinforced from here on out, so the system has converged (in opinion).
                        
    return convergence #true if the system met any of the previous conditions, false if not.