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


def plottingarguments(tipo=5,cb='no',Ars=60,N=10,rel=5,l=0,bins=1,chosen='indeciso'):    
    '''This function was used for saving variables for making different kinds of plots involving arguments. The first four types were 
    omitted, since they were not used for the paper. The fifth type can be used for making the argument evolutions presented in Figure 3.
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
              
                        
def plottingmanyevolutionsbins1(chosen='indeciso',cb='no',N=10,Ars=60,rel=6):
        '''Having run the previous function, we can now make the proper plots of evolutions of arguments. This was optimized for bins of
        size 1; making it for larger bins requires some tweaking. We will not be making a more general function, but we added comments in
        the lines of code that should be changed for making it.
        "chosen" is the type of final state, as described in the function above.
        "cb" is also the same as before
        "N" is the number of agents.
        "Ars" is N_A, the number of existing arguments.
        "rel" is M, the memory size.'''
        
        #import useful libraries
        import numpy as np
        import pylab as py
        from loading import loadinggeneric #this function is used for loading saved variables.
        
        if N==100: #the third row of Figure 3 involved this N, which sets us in the region of moderate consensus.
            evolutions=loadinggeneric('PARAPLOTEARindecisoevolcbno100rel6bines1ens100') #you shoul put the proper name of the saved file.
        else:
            if rel==5: #we originally tested this value of M
                evolutions=loadinggeneric(chosen+'evolcb'+cb,'D:\\Doctorado\\Simulation_Functions\\')
            else: #we only used M=5 or M=6, so this is M=6.
                evolutions=loadinggeneric(chosen+'evolcb'+cb+'10rel6bines1ens100','D:\\Doctorado\\Simulation_Functions\\')
            
        #For correctly plotting the evolutions, we need to find the one that took the most time to converge, and extend the rest
        #so that all of them end there (this is done by repeating the last value of each evolution until the desired length is obtanined).
        newevols=list([list([0 for alpha in range(62)]) for i in range(max([len(evolutions[i]) for i in range(len(evolutions))]))])
        #Number 62 must be changed to extend this for larger bin size (e.g. for bins of size 5, it should be 14).
        a=max([len(evolutions[i]) for i in range(len(evolutions))])
        for i in range(len(evolutions)):
            if len(evolutions[i])!=a:
                evolutions[i]+=[evolutions[i][-1] for j in range(a-len(evolutions[i]))]
        
        #This code is for normalization, so that the cases of N=10 and N=100 can be readily compared.
        for j in range(a):
            for k in range(61): #this number should be changed for extending to other bin sizes (e.g. for bins of size 5, it should be 13).
                for i in range(len(evolutions)):
                    newevols[j][k]+=int(list(evolutions[i][j])[k])
                newevols[j][k]/=float(N)
            
        B=np.transpose(newevols) #transpose to see the time steps on the horizontal axis.
        
        #We now perform the plot.
        fig=py.figure()  
        if N==10:
            py.imshow(B,cmap='gray_r',aspect='auto',vmax=50) #If you use different N, different saturation of the scale is useful to appreciate
            #differences. This number is arbitrary.
        else:
            py.imshow(B,cmap='gray_r',aspect='auto',vmax=100)
        
        #Axis labels    
        py.ylabel(u'Arguments',size=18)
        py.xlabel(u'Time Steps',size=18)
        
        #ticks and axis limits
        py.ylim([-0.5,60+0.5])
        py.xticks(size=16)
        length=len(np.arange(-Ars,Ars+1,5))
        length=np.linspace(-0.5,60+0.5,Ars/10+1)
        py.yticks(length,size=16)
        ax=py.gca()
        ax.yaxis.set_ticklabels(np.arange(-Ars/2,Ars/2+1,10))
        py.xlim([0,100])
        py.xticks(range(0,101,20))
        ax.xaxis.set_ticklabels([0,2,4,6,8,10])
        if N==100:
            py.xlim([0,1000])          
            py.xticks(range(0,1001,200))
            ax.xaxis.set_ticklabels([0,2,4,6,8,10])     
                            
        #colorbar        
        C=py.colorbar()    
        for m in C.ax.yaxis.get_ticklabels():
            m.set_size(16)
        
        #Resize for good fit on paper:
        fig.set_size_inches(12,5)     
        #Save the figure. The directory should be changed for use on another computer.     
        py.savefig('D:\\Doctorado\\Paper Argumentos\\Review\\'+chosen+'evolnuevaPROBANDO'+str(N)+'CB='+cb+'.svg', bbox_inches='tight') 
                                            
##Examples of use:

# plottingmanyevolutionsbins1(chosen='indeciso',cb='no',N=100,Ars=60,bins=1,rel=6)
# plottingmanyevolutionsbins1(chosen='consenso1',cb='no',N=10,Ars=60,bins=1,rel=6)
# plottingmanyevolutionsbins1(chosen='consenso2',cb='no',N=10,Ars=60,bins=1,rel=6)
# import pylab as py
# py.close('all')