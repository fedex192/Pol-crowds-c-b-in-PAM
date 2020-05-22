# -*- coding: utf-8 -*-

def restructuringargumentvalues(b,k):
    '''This is an auxiliary function, to restructure the list that comes from the checkingargumentsevolution function, for use with the 
    plottingarguments function. It will not be thoroughly commented. We only used it for the case of N_A=60, but it can be easily extended 
    by changing 30 for N_A/2, 29 by N_A/2-1, and adding an N_A input parameter. We avoided this in case we missed some call to this function, 
    resulting in errors.'''
    
    for i in range(len(b[k])):
        for j in range(len(b[k][i])):
            if b[k][i][j]<30:
                b[k][i][j]+=1
            elif b[k][i][j]>=30:
                b[k][i][j]-=29
                b[k][i][j]=-b[k][i][j]
    return b[k]


def plottingarguments(tipo=5,cb='yes',Ars=60,N=10,rel=5,l=0,bins=1,chosen='indeciso'):    
    '''This function was used for making different kinds of plots involving arguments. The first four types were omitted, since they were not
    used for the paper. The fifth type can be used for making the argument evolutions presented in Figure 3.
    "tipo" is the type, here it can only be 5, or else nothing will happen.
    "cb" is the presence (cb='yes') or abscence (cb='no') of confirmation bias.
    "Ars" is N_A, the number of arguments in the system.
    "N" is the number of agents.
    "rel" is M, the memory size.
    "l" is obsolete, it was used for the other types.
    "bins" can be used for determining how fine-grained the evolution of arguments will be. If bins=1, the evolution will show
    each existing argument; if bins>1, some arguments will be combined for the final plot (i.e the bins of the histogram of each time
    step will include more than one argument). 
    "chosen" is the type of final state one wishes to plot. If chosen='indeciso' (i.e. undecided), the final state is moderate (O=0). If
    chosen='consenso1', the final state is orientend with O=1. If chosen='consenso2', the final state is oriented with O=-1. If
    chosen='bip', the final state is bipolarization (note that it is not present if cb='no').
    What this function does is to run several evolutions (for the paper, we used 100), and make a histogram on each time step, of all the
    arguments present at that time step. If bins=1, this means it counts how many of each argument are present in all the copies, for each time
    step. N=100 with chosen=indeciso is easier to understand, since all arguments are present at first, and in the end, only the strongest ones
    remain (please, see Figure 3 of the paper).'''
    import pylab as py
    from newrunargsim import checkingargumentsevolution 
    
    if tipo==5: #the only one possible here.
        
        import numpy as np
        #initializations:
        count=0
        evolutions=[]
        
        while count<100: #choose how many copies you want to use in the ensamble.
            c=checkingargumentsevolution(Ars,Ars/2,N,rel,2000,cb) #main simulation function. 2000 steps were enough for the figures we made.
            b=c[-2]
            opinions=[]
            
            #determine the opinion of all agents:
            for i in range(N):
                if c[-1][i][-1]<-1:
                    opinions.append(-1)
                elif c[-1][i][-1]>1:
                    opinions.append(1)
                else:
                    opinions.append(0)
                    
            #use the previous variable to determine which final state was found  
            if opinions==[1 for i in range(N)]:
                chosentype='consenso1' #oriented positive consensus
            elif opinions==[-1 for i in range(N)]:
                chosentype='consenso2' #oriented negative consensus
            elif opinions==[0 for i in range(N)]:
                chosentype='indeciso' #moderate consensus
            elif 0 not in opinions:
                chosentype=u'bip' #bipolarization
            else:
                chosentype=u'otros' #just in case.

            #if this run ended in the way we chose, we add it:
            if chosen==chosentype:
                #initialize bins
                argumentbins=[]
                
                for k in range(len(b)): #loop over time steps.
                    b[k]=restructuringargumentvalues(b,k) #we change the structure for easy access.
                    systemargs=b[k][0]
                    for i in range(1,N):
                        systemargs+=b[k][i] #we save the arguments
                                        
                    a=np.histogram(systemargs,np.arange(-Ars/2,Ars/2+2,bins)) #we obtain the histogram of each time step.
                    argumentbins.append(list(a[0]))
                    
                evolutions.append(argumentbins) #we add the results to the evolutions vector, which will contain the evolutions for every
                #copy of the ensamble. This means that the first index of this vector will be the specific copy we ran, and the argument bins
                #for each time step of that copy will be inside.
                count+=1 #elevate count, the variable used by the while loop.
                
        return evolutions    