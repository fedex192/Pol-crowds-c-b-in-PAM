# -*- coding: utf-8 -*-

'''This script runs the main simulations for the paper. NOTE: posture is called persuasion in all this code.'''

#You start by setting the directory where all other functions are present.

import os
#os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
#os.chdir('C:\\Users\\Fede\\Desktop\\Simulation_Functions\\') 
os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
#Put your own directory here.


def newrunargsimforprofiling(allargs=60,rangeofimpacts=30,N=10,numofrelevargs=6,steps=10000,cb='yes',plotting='',homo=0,Ct=1.0, Cmax=3.0,intertype='Bid'):
    '''This function is the main simulation. 
    "allargs" is N_A in the paper. 
    "rangeofimpacts" must be N_A/2. 
    "N" is the number of agents.
    "numofrelevargs" is the memory size M. 
    "steps" is the maximum number of steps to use for the simulation; sometimes, oscillations can occur, which prevent total convergence of 
    persuasions (this is due to the rule of agents acquiring the new argument in case of a tie, see Agent.py), and thus this parameter prevents 
    the simulation from going on forever. The decision of when to quit and call it an oscilation is arbitrary, but exploratory tests can easily
    show that 10000 is one order of magnitud larger than the mean number of steps necessary for convergence in all simulations carried out in the
    paper (and is usually many orders of magnitud larger). 
    "cb" determines if confirmation bias is present (cb='yes') or not (cb='no').
    "plotting" is used for debugging and checking results, and plots some of the results (set it to plotting='yes'). 
    "homo" is the homophily parameter (0 means no homophily). 
    "Ct" is the threshold between opinions (we use Ct as threshold between O=1 and O=0, and -Ct as threshold between O=0 and O=-1). 
    "Cmax" is the maximum absolute value of persuasion. 
    "intertype" was used to change the kind of interaction, from unidirectional to bidirectional; it was unused for the paper, since all 
    interactions were bidirectional. 
    This function returns the final number of agents of each opinion, and a flag which is helpful for detecting oscillations.'''

    #we start by importing all necessary function. The number 2 means they were cythonized first.  
    from population2 import argumentativepopulation
    from createlistofarguments2 import createlistofarguments
    from newinteraction2 import newargumentativeinteraction
    from getundecidedcounts2 import getundecidedcounts
    from getagentspersuasion2 import getagentspersuasion
    from checkconvergence2 import checkconvergence

    #we create the list of all arguments.    
    listofarguments=createlistofarguments(allargs,1,rangeofimpacts)
    #we create the population of agents     
    popu=argumentativepopulation(listofarguments,N,numofrelevargs,Ct,Cmax)
    
    
    countsund=[]
    countspro=[]
    countsagainst=[]
    #save the initial number of agents of each opinion.    
    a=getundecidedcounts(popu)
    countsund.append(a[0])
    countspro.append(a[1])
    countsagainst.append(a[2])
    
    #vector of persuasions, in case it is necessary    
    persuasions=[[] for i in range(len(popu))]
    
    stepcount=0 #for counting the number of steps taken.

    flag=0 #for detecting oscillations      
    
    #main loop 
    while not checkconvergence(popu,cb):
        stepcount+=1        
        
        #we save the persuations at the beginning of each step. 
        subpersuasions=getagentspersuasion(popu)  
        for j in range(len(popu)):
            persuasions[j]+=subpersuasions[j]  
            
        #now we make one pairwise interaction:                      
        b=newargumentativeinteraction(popu, listofarguments, Cmax, intertype, cb,'bidirectional',homo)
        
        #save the number of agents of each opinion after interaction
        a=getundecidedcounts(popu)
        countsund.append(a[0])
        countspro.append(a[1])
        countsagainst.append(a[2])
        
        #break in case of oscillations:
        if stepcount>10000:
            flag=1
            break
            
    #save the persuasions of the last step                 
    subpersuasions=getagentspersuasion(popu)  
    for j in range(len(popu)):
        persuasions[j]+=subpersuasions[j]        
                      
    #if one wishes to see some plots:                      
    if plotting=='yes':    
        arguments=[[] for i in range(len(popu))]
        for j in range(len(popu)):
            for i in range(len(popu[j].relevancevector)):
                if popu[j].relevancevector[i]==1:
                    #print i
                    arguments[j].append(i)
        ##this can be used for plotting histograms of arguments.
        #if a[0]!=0 and a[0]!=10: #if you want plots of only specific final states (like moderate consensus), uncomment this line, and indent the next.
        #makingargumenthistograms(arguments,allargs) 
        from plottingopinions import plottingopinions        
        plottingopinions(a) #this plots the evolution of opinions, and can be used to determine if one wishes to save this run, or not.     
        #plottingpersuasions(persuasions) #this can be used for plotting persuasion evolutions.
        #return 0 #one may wish to end the function after plotting, without returning all the variables

    return countsund, countspro, countsagainst,flag,stepcount#,persuasions#,arguments ##one may uncomment the last two variables if one wishes to use them.



def newrunargsim(allargs=60,rangeofimpacts=30,N=10,numofrelevargs=6,steps=6000,cb='yes',plotting='',homo=0,Ct=1.0, Cmax=3.0,intertype='Bid'):
    '''This function is the same as the one preceding it, with one exception: this function uses a for loop. It is useful for small tests, and 
    to easily make some of the descriptive plots used in the paper. However, the previous one was used for all the main simulations of the paper.'''
    
    #we start by importing all necessary functions.
    from population import argumentativepopulation
    from createlistofarguments import createlistofarguments
    from newinteraction import newargumentativeinteraction
    from getundecidedcounts import getundecidedcounts
    from getagentspersuasion import getagentspersuasion

    #we create the list of all arguments.
    listofarguments=createlistofarguments(allargs,1,rangeofimpacts)
    #we create the population of agents
    popu=argumentativepopulation(listofarguments,N,numofrelevargs,Ct,Cmax)
    
    
    countsund=[]
    countspro=[]
    countsagainst=[]
    #save the initial number of agents of each opinion.
    a=getundecidedcounts(popu)
    countsund.append(a[0])
    countspro.append(a[1])
    countsagainst.append(a[2])
    
    #vector of persuasions, in case it is necessary
    persuasions=[[] for i in range(len(popu))]
    
    
    #stepcount=0 #for counting the number of steps taken.
    
    #breakcount can be used for breaking the simulation if the number of steps goes too far, which can depend on the number of agents, and if 
    #persuasions do not change for a certain number of steps. Currently unused.
    # if N<50:
    #     breakcount=6000
    # elif N>=50 and N<80:
    #     breakcount=6000
    # else:
    #     breakcount=6000
    
    #main loop        
    for i in range(steps):
        #we save the persuations at the beginning of each step.
        subpersuasions=getagentspersuasion(popu)
        for j in range(len(popu)):
            persuasions[j]+=subpersuasions[j]    
            
        #now we make one pairwise interaction:      
        b=newargumentativeinteraction(popu, listofarguments, Cmax, intertype, cb,'bidirectional',homo)
        
        #save the number of agents of each opinion after interaction
        a=getundecidedcounts(popu)
        countsund.append(a[0])
        countspro.append(a[1])
        countsagainst.append(a[2])
        
        ##this code can be used to stop the simulation early if no changes in persuasion occur for a certain number of steps.
        # tempcount=0
        # if i!=0:
        #     for persuasion in range(len(persuasions)):
        #         if persuasions[persuasion][-1]==persuasions[persuasion][-2]:
        #             tempcount+=1
        #     if tempcount==N:
        #         stepcount+=1
        #     else:
        #         stepcount=0
        # if stepcount==breakcount:
        #     break
        
    #If too many steps were taken, it probably was an oscillation. This does not affect any results of the paper, and was mostly
    #unused.
    if i>9000:
        flag=1
    else:
        flag=0    
    
    #save the persuasions of the last step
    subpersuasions=getagentspersuasion(popu)  
    for j in range(len(popu)):
        persuasions[j]+=subpersuasions[j]        
    
    #if one wishes to see some plots.                                             
    if plotting=='yes':    
        arguments=[[] for i in range(len(popu))]
        for j in range(len(popu)):
            for i in range(len(popu[j].relevancevector)):
                if popu[j].relevancevector[i]==1:
                    #print i
                    arguments[j].append(i)
        ##this can be used for plotting histograms of arguments.
        #if a[0]!=0 and a[0]!=10: #if you want plots of only specific final states (like moderate consensus), uncomment this line, and indent the next.
        #from makingargumenthistograms import makingargumenthistograms
        #makingargumenthistograms(arguments,allargs)
        from plottingopinions import plottingopinions
        plottingopinions(a) #this plots the evolution of opinions, and can be used to determine if one wishes to save this run, or not.     
        #from plottingpersuasions import plottingpersuasions
        #plottingpersuasions(persuasions) #this can be used for plotting persuasion evolutions.
        #return 0 #one may wish to end the function after plotting, without returning all the variables

    return countsund, countspro, countsagainst,flag#,persuasions#, arguments ##one may uncomment the last two variables if one wishes to use them.
                

#This function is exactly the same as newrunargsim, but it also returns the final arguments (this can be memory-consuming, and is the reason
#why it was used as a separate function). We will not add comments to it, since this was already done for newrunargsim. Some lines may be
#uncommented, since this was not used for main simulations, but for plotting arguments evolutions.
def checkingargumentsevolution(allargs=60,rangeofimpacts=30,N=10,numofrelevargs=5,steps=10000,cb='yes',Ct=1.0, Cmax=3.0,intertype='Bid'):
    from population import argumentativepopulation
    from createlistofarguments import createlistofarguments
    from interaction import argumentativeinteraction
    from getundecidedcounts import getundecidedcounts
    from getagentspersuasion import getagentspersuasion
#    import pylab as py
    listofarguments=createlistofarguments(allargs,1,rangeofimpacts)
    popu=argumentativepopulation(listofarguments,N,numofrelevargs,Ct,Cmax)
    countsund=[]
    countspro=[]
    countsagainst=[]
    a=getundecidedcounts(popu)
    countsund.append(a[0])
    countspro.append(a[1])
    countsagainst.append(a[2])
    persuasions=[[] for i in range(len(popu))]
    stepcount=0
    arguments=[]
    if N<50:
        breakcount=500
    elif N>=50 and N<80:
        breakcount=700
    else:
        breakcount=1000
    
    subarguments=[[] for i in range(len(popu))]
    for j in range(len(popu)):
        for i in range(len(popu[j].relevancevector)):
            if popu[j].relevancevector[i]==1:
                    #print i
                subarguments[j].append(i)
    arguments.append(subarguments)    
                
    for i in range(steps):
        subpersuasions=getagentspersuasion(popu)  
        for j in range(len(popu)):
            persuasions[j]+=subpersuasions[j]          
        #b=argumentativeinteraction(popu, listofarguments, Cmax, intertype, cb,'bidirectional')
        b=argumentativeinteraction(popu, listofarguments, Cmax, intertype, cb,'bidirectional')
        if b!=None:
            print b
        a=getundecidedcounts(popu)
        countsund.append(a[0])
        countspro.append(a[1])
        countsagainst.append(a[2])
        tempcount=0
        if i!=0:
            for persuasion in range(len(persuasions)):
                if persuasions[persuasion][-1]==persuasions[persuasion][-2]:
                    tempcount+=1
            if tempcount==N:
                stepcount+=1
            else:
                stepcount=0
        if stepcount==breakcount:
            break
            
        subarguments=[[] for k in range(len(popu))]
        for k in range(len(popu)):
            for l in range(len(popu[k].relevancevector)):
                if popu[k].relevancevector[l]==1:
                    #print i
                    subarguments[k].append(l)
        arguments.append(subarguments)
        
    subpersuasions=getagentspersuasion(popu)  
    for j in range(len(popu)):
        persuasions[j]+=subpersuasions[j]        
                        

    return countsund, countspro, countsagainst, arguments, persuasions
