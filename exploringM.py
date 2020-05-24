'''This functions were used for exploring the dependence on paramater M, here called rel'''

#You start by setting the directory where all other functions are present.

import os
#os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
#os.chdir('C:\\Users\\Fede\\Desktop\\Simulation_Functions\\') 
os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
#Put your own directory here.


#The first function explores the space parameter for fixed N_A (here called allargs), and free M and N.
def explorargsimforrelandN(relini=6,relfin=57,allargs=60,numens=1000,cb='no',opsys='w'):
    '''Exploration of N vs. M. 
    "relini" is the first value of M to be used.
    "relfin" is the last value of M to be used +1.
    "allargs" is N_A, the fixed total number of arguments.
    "numens" is the number of copies of the ensamble
    "cb" is the presence of confirmation bias (cb='yes'), or its abscence (cb='no')
    "opsys" is obsolete, was used for changing operating systems when we ran some of this simulations on linux as well as Windows.
    It does not return anything, but it saves the results.'''
    
    #First, we import one function to save the variables. This is a specific saving method for this exploration.
    from saving import savingargumentsimulation2
    
    #In this function, we call M as rel, and N_A as allargs.
    
    for rel in range(relini,relfin,2): #choose the steps to be used. Since memory should be even or uneven, the smallest one should be 2. 
        print rel #for keeping track.
        for N in range(10,111,5):
            
            #initializations:
            counts0=0
            countspl=0
            countsmin=0
            countsbip=0
            otherstuff=0 #in case something else happens (used for initial testing)
            ensamblestates=[]
            osc=0 #oscillations
            
            from newrunargsim import newrunargsim #newrunargsimfor profiling is also an option.
            
            for copy in range(numens):
                a=newrunargsim(allargs,allargs/2,N,rel,10000,cb,'no') 
                
                #now we check which final state we found, and increase its count.                
                if a[1][-1]==N:
                    countspl+=1
                elif a[2][-1]==N:
                    countsmin+=1
                elif a[0][-1]==N:
                    counts0+=1
                elif a[0][-1]==0 and a[1][-1]!=N and a[2][-1]!=N:
                    countsbip+=1 
                else:
                    otherstuff+=1
                ensamblestates.append((a[0][-1],a[1][-1],a[2][-1])) #here we append what the final states were. This is useful to
                #check, for example, what type of bipolarization was obtained (e.g. 60% O=1 and 40% O=-1).
                osc+=a[-1] #in case oscillations occurred.
            savingargumentsimulation2((counts0,countspl,countsmin,countsbip,otherstuff,osc,ensamblestates),rel,N,numens,opsys)

def explorargsimforrelandArs(relini=6,relfin=57,N=60,numens=1000,cb='no',opsys='w'):
    '''Exploration of N_A vs. M. 
    "relini" is the first value of M to be used.
    "relfin" is the last value of M to be used +1.
    "N" is the fixed number of agents.
    "numens" is the number of copies of the ensamble
    "cb" is the presence of confirmation bias (cb='yes'), or its abscence (cb='no')
    "opsys" is obsolete, was used for changing operating systems when we ran some of this simulations on linux as well as Windows.
    It does not return anything, but it saves the results.'''
    
    #First, we import one function to save the variables. This is a specific saving method for this exploration.    
    from saving import savingargumentsimulation3
    
    #In this function, we call M as rel, and N_A as allargs.

    
    for rel in range(relini,relfin,5): #choose the steps to be used. Since memory should be even or uneven, the smallest one should be 2. 
        print rel #for keeping track.
        for Ars in range(10,113,6):
            
            #initializations:
            counts0=0
            countspl=0
            countsmin=0
            countsbip=0
            otherstuff=0 #in case something else happens (used for initial testing)
            ensamblestates=[]
            osc=0 #oscillations
            
            from newrunargsim import newrunargsim #newrunargsimfor profiling is also an option.            
            
            for copy in range(numens):
                a=newrunargsim(Ars,Ars/2,N,rel,10000,cb,'no')
                
                #now we check which final state we found, and increase its count.                                
                if a[1][-1]==N:
                    countspl+=1
                elif a[2][-1]==N:
                    countsmin+=1
                elif a[0][-1]==N:
                    counts0+=1
                elif a[0][-1]==0 and a[1][-1]!=N and a[2][-1]!=N:
                    countsbip+=1 
                else:
                    otherstuff+=1
                ensamblestates.append((a[0][-1],a[1][-1],a[2][-1])) #here we append what the final states were. This is useful to
                #check, for example, what type of bipolarization was obtained (e.g. 60% O=1 and 40% O=-1) 
                osc+=a[-1] #in case oscillations occurred.

            savingargumentsimulation3((counts0,countspl,countsmin,countsbip,otherstuff,osc,ensamblestates),rel,Ars,numens,opsys)
