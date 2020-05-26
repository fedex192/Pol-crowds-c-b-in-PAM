# -*- coding: utf-8 -*-
'''This file contains many functions used for recovering the saved data from the parameter explorations, and joining it in simple
structures, so it can be used for analysis and plotting. They can be time-consuming.'''

#The next two functions are used to load and restructure the results saved by newexplorargsimforprofiling of file newexplorargsim.py.
#We actually used them to load old results from an original exploration without homophily. The results are the same, but the names of
#the saved files were different, and it was easier to use these. These were used only with function analyzingargsimphasediagramMayPops
#of file newargumentsphasediagram.py. We leave them here just for reference, since collectargsimdata is mentioned in that file.

def loadingargumentvariables(allargs,N,numens=1000,cb='no'):
    '''This functions loads results from explorations found in newrunargsim.py.
    "allargs" is N_A, the number of existing arguments.
    "N" is the number of agents.
    "numens" is the number of copies of the ensamble
    "cb" is the presence (cb='yes') or abscence (cb='no') of confirmation bias.
    This returns the saved variable.'''
    
    import pickle, os #import useful libraries.
    
    A=os.getcwd() #get current directory
    
    if cb=='no': #change directory according to the case. These directories should be changed in another computer.
        os.chdir('D:\\Doctorado\\Simulation_Functions\\Barrido Anterior\\FullExplorationRel6-'+str(numens)+'\\')
    else:
        os.chdir('D:\\Doctorado\\Simulation_Functions\\Barrido Anterior\\FullExplorationRel6ConCB-'+str(numens)+'\\')
    
    #open saved variable
    f = open('allargs'+str(allargs)+', N='+str(N)+', Ens='+str(numens)+'.pckl', 'rb')
    var = pickle.load(f) #save it to var
    f.close() #close saved variable
    os.chdir(A) #go back to the original directory.
    return var

def collectargsimdata(numens=1000,cb='no'):
    '''This functions uses the previous one to load and restructure all the results from the exploration newexplorargsimforprofiling
    found in newexplorargsim.py. 
    "numens" is the number of copies of the ensamble
    "cb" is the presence (cb='yes') or abscence (cb='no') of confirmation bias.
    This returns the restructured results, ready for plotting.'''
    
    #initializations
    counts0=[[] for i in range(10,101,2)] #counts of moderate consensus states
    countsdec=[[] for i in range(10,101,2)] #counts of oriented consensus states
    countsbip=[[] for i in range(10,101,2)] #counts of bipolarization states
    countsother=[[] for i in range(10,101,2)] #counts of other states (obsolete, for debugging
    countspl=[[] for i in range(10,101,2)] #counts of oriented positive consensus states
    countsmin=[[] for i in range(10,101,2)] #counts of oriented negative consensus states
    allcopies=[[] for i in range(10,101,2)]  #save all the copies, useful for plots like the one in analyzingargsimphasediagramMayPops (in newargumentsphasediagram.py)

    i=0 #initialization for the indexes
    for allargs in range(10,101,2): #for every value of N_A
        for N in range(10,101): #for every value of N
            A=loadingargumentvariables(allargs,N,numens,cb) #loading function
            #append the final counts to the initialized lists.
            counts0[i].append(A[0])
            countspl[i].append(A[1])
            countsmin[i].append(A[2])
            countsbip[i].append(A[3])
            countsother[i].append(A[4])
            countsdec[i].append(A[1]+A[2])
            allcopies[i].append(A[5])
        i+=1
                 
    return counts0,countsdec,countsbip,countsother,countspl,countsmin,allcopies
 
   
#The next two functions are used to load and restructure the results saved by newexplorargsimwithconvergence of file newexplorargsim.py.
#Results are plotted in function analyzingargsimphasediagram of file newargumentsphasediagram.

def newloadingargumentvariablesconvergente(allargs,N,homo,cb='no',numens=1000,numofrelevargs=6):
    '''This functions loads results from explorations found in newrunargsim.py.
    "allargs" is N_A, the number of existing arguments.
    "N" is the number of agents.
    "homo" is the homophily parameter
    "cb" is the presence (cb='yes') or abscence (cb='no') of confirmation bias.
    "numens" is the number of copies of the ensamble
    "numofrelevargs" is M, the memory size.
    This returns the saved variable.
    The rest of the function is the same as loadingargumentvariables, and will not be commented.'''
        
    import pickle, os
    A=os.getcwd()
    os.chdir('D:\\Doctorado\\Simulation_Functions\\BarridoConvergente\\') 
    f = open('N'+str(N)+'Nars'+str(allargs)+'H'+str(homo)+'cb'+cb+'M'+str(numofrelevargs)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var          

def newcollectargsimdataconvergente(homo=0,cb='no'):
    '''This functions uses the previous one to load and restructure all the results from the exploration newexplorargsimwithconvergence
    found in newexplorargsim.py. 
    "homo" is the homophily parameter.
    "cb" is the presence (cb='yes') or abscence (cb='no') of confirmation bias.
    This returns the restructured results, ready for plotting.
    Since this function is very similar to collectargsimdata, we will not be commenting it, except for the new lines of code.'''
    
    import numpy as np
    
    counts0=[[] for i in range(10,101,10)]
    countsdec=[[] for i in range(10,101,10)]
    countsbip=[[] for i in range(10,101,10)]
    countsother=[[] for i in range(10,101,10)]
    countspl=[[] for i in range(10,101,10)]
    countsmin=[[] for i in range(10,101,10)]
    countsosc=[[] for i in range(10,101,10)]
    stepcountsmean=[[] for i in range(10,101,10)] #this initializes the mean number of steps
    stepcountsmedian=[[] for i in range(10,101,10)] #this initializes the median number of steps
    tiempos=[[] for i in range(10,101,10)] #this initializes the elapsed time for the simulations
#    allcopies=[[] for i in range(10,101,10)] #this was not used here

    i=0
    for allargs in range(10,101,10):
        for N in range(10,101,10):
            
            A=newloadingargumentvariablesconvergente(allargs,N,homo,cb,1000,6)
            
            counts0[i].append(A[0][0])
            countspl[i].append(A[0][1])
            countsmin[i].append(A[0][2])
            countsbip[i].append(A[0][3])
            countsother[i].append(A[0][5])
            countsdec[i].append(A[0][1]+A[0][2])
            countsosc[i].append(A[0][4])
            #new variables:
            stepcountsmean[i].append(np.mean(A[1]))
            stepcountsmedian[i].append(np.median(A[1]))
            tiempos[i].append(A[2])                              
        i+=1
       
    return counts0,countsdec,countsbip,countsother,countspl,countsmin,countsosc,stepcountsmean,stepcountsmedian,tiempos #we also return the new variables
    
    
    
#The next two functions are used to load and restructure the results saved by newexplorargsimwithconvergencereview of file exploringDelta.py.
#Please note, we do not provide the function to make the plots for this case, since it is just a particular case of the next two functions.
#However, this could be used to prepare the saved data for plotting, which could be easily done with analyzingargsimphasediagram in the 
#file newargumentsphasediagram.py

def newloadingargumentvariablesreviewer(allargs,discrep,homo,cb='no',numens=1000,numofrelevargs=6):
    '''This functions loads results from the exploration newexplorargsimwithconvergencereview found in exploringDelta.py.
    "allargs" is N_A, the number of existing arguments.
    "discrep" is the N_A/N.
    "homo" is the homophily parameter
    "cb" is the presence (cb='yes') or abscence (cb='no') of confirmation bias.
    "numens" is the number of copies of the ensamble
    "numofrelevargs" is M, the memory size.
    This returns the saved variable.
    The rest of the function is the same as loadingargumentvariables, and will not be commented.'''
            
    import pickle, os
    A=os.getcwd()
    os.chdir('D:\\Doctorado\\Simulation_Functions\\BarridoReviewer\\') 
    f = open('N50NArs'+str(float(allargs))+'discrep'+str(discrep)+'cb'+cb+'M'+str(numofrelevargs)+'.pckl', 'rb') #Note the name, fixed N=50
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var    
    
def newcollectargsimdatareviewer(homo=0,cb='no'):
    '''This functions uses the previous one to load and restructure all the results from the exploration newexplorargsimwithconvergencereview 
    found in exploringDelta.py.
    "homo" is the homophily parameter
    "cb" is the presence (cb='yes') or abscence (cb='no') of confirmation bias.
    This returns the restructured results, ready for plotting.
    Since this function is very similar to newcollectargsimdataconvergente, we will not be commenting it, except for the new lines of code.'''
    
    import os
    import numpy as np
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    
    counts0=[[] for i in range(6,51,2)]
    countsdec=[[] for i in range(6,51,2)]
    countsbip=[[] for i in range(6,51,2)]
    countsother=[[] for i in range(6,51,2)]
    countspl=[[] for i in range(6,51,2)]
    countsmin=[[] for i in range(6,51,2)]
    countsosc=[[] for i in range(6,51,2)]
    tiempos=[[] for i in range(6,51,2)]    

    i=0

    for M in range(6,51,2):
        for discrep in np.arange(0.2,2.01,0.04): #discrep is N_A/N, and for fixed N=50, this is the full range and minimum step size.
            A=newloadingargumentvariablesreviewer(round(discrep*50),discrep,homo,cb,1000,M)
            
            if A[0]==np.nan: #this is done so we only consider the region of physical significance, M<N_A
                counts0[i].append(np.nan)
                countspl[i].append(np.nan)
                countsmin[i].append(np.nan)
                countsbip[i].append(np.nan)
                countsother[i].append(np.nan)
                countsdec[i].append(np.nan)
                countsosc[i].append(np.nan)
                tiempos[i].append(np.nan)           
            else: #when we are in the region of physical significance, we procede as before:          
                counts0[i].append(A[0][0])
                countspl[i].append(A[0][1])
                countsmin[i].append(A[0][2])
                countsbip[i].append(A[0][3])
                countsother[i].append(A[0][5])
                countsdec[i].append(A[0][1]+A[0][2])
                countsosc[i].append(A[0][4])
                tiempos[i].append(A[2])           
        i+=1
       
    return counts0,countsdec,countsbip,countsother,countspl,countsmin,countsosc,tiempos


#The next three functions are used to load and restructure the results saved by newexplorargsimwithconvergencereview2 of file exploringDelta.py.    
#Results are plotted in function analyzingargsimphasediagramreview of file newargumentsphasediagram.  

def newloadingargumentvariablesreview2(NA,N,M,homo=0,cb='no',numens=1000):
    '''This functions loads results from the exploration newexplorargsimwithconvergencereview2 found in exploringDelta.py.
    "NA" is N_A, the number of existing arguments.
    "N" is the number of agents.
    "M" is the memory size.
    "homo" is the homophily parameter
    "cb" is the presence (cb='yes') or abscence (cb='no') of confirmation bias.
    "numens" is the number of copies of the ensamble
    This returns the saved variable.
    The rest of the function is the same as loadingargumentvariables, and will not be commented.'''
                
    import pickle, os
    A=os.getcwd()
    os.chdir('D:\\Doctorado\\Simulation_Functions\\BarridoReviewer\\') 
    f = open('N'+str(N)+'NArs'+str(NA)+'cb'+cb+'M'+str(M)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
    
def newcollectargsimdatareview2(homo=0,cb='no'):
    '''This functions uses the previous one to load and restructure all the results from the exploration newexplorargsimwithconvergencereview2
    found in exploringDelta.py.
    "homo" is the homophily parameter
    "cb" is the presence (cb='yes') or abscence (cb='no') of confirmation bias.
    This returns the restructured results, but not ready for plotting. THe last function, transformdatareview2, finishes the restructuring
    of the data (we separated both functions because this time, the restructuring process was much more complicated).
    Since this function is very similar to newcollectargsimdatareviewer, we will not be commenting it, except for the new lines of code.'''
    
    import os
    import numpy as np
    from saving import savinggeneric #we will save this, just in case.
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    
    #This time, the final lists are more complicated, as seen in this initializations
    counts0=[[[] for j in range(10,101,1)] for i in range(6,51,2)] #the most inner dimensions are of N, the outer ones are of M.
    countsdec=[[[] for j in range(10,101,1)] for i in range(6,51,2)]
    countsbip=[[[] for j in range(10,101,1)] for i in range(6,51,2)]
    countsother=[[[] for j in range(10,101,1)] for i in range(6,51,2)]
    countspl=[[[] for j in range(10,101,1)] for i in range(6,51,2)]
    countsmin=[[[] for j in range(10,101,1)] for i in range(6,51,2)]
    countsosc=[[[] for j in range(10,101,1)] for i in range(6,51,2)]
    tiempos=[[[] for j in range(10,101,1)] for i in range(6,51,2)]    

    i=0

    for M in range(6,51,2): #the range of Ms explored
        j=0
        print(M) #for keeping track, this is the function which takes the most to finish in this file.
        for N in range(10,101,1): #the range of Ns explored
            for NA in range(10,101,2): #the range of N_As explored
                
                A=newloadingargumentvariablesreview2(NA,N,M,homo,cb,1000)  
                              
                if A[0]==np.nan:
                    counts0[i][j].append(np.nan)
                    countspl[i][j].append(np.nan)
                    countsmin[i][j].append(np.nan)
                    countsbip[i][j].append(np.nan)
                    countsother[i][j].append(np.nan)
                    countsdec[i][j].append(np.nan)
                    countsosc[i][j].append(np.nan)
                    tiempos[i][j].append(np.nan)           
                else:           
                    counts0[i][j].append(A[0][0])
                    countspl[i][j].append(A[0][1])
                    countsmin[i][j].append(A[0][2])
                    countsbip[i][j].append(A[0][3])
                    countsother[i][j].append(A[0][5])
                    countsdec[i][j].append(A[0][1]+A[0][2])
                    countsosc[i][j].append(A[0][4])
                    tiempos[i][j].append(A[2])            
            j+=1                  
        i+=1
        
        savinggeneric((counts0,countsdec,countsbip,countsother,countspl,countsmin,countsosc,tiempos),'BarridoFinoReviewFinal')
        #we save the results, in case something happens and we have to start all over.
        
    return counts0,countsdec,countsbip,countsother,countspl,countsmin,countsosc,tiempos


def transformdatareview2():
    '''This function is to be used after the previous one, and finishes the restructuring of data. After this, results can be
    plotted with function analyzingargsimphasediagramreview in file newargumentsphasediagram.py. This function is quite complicated,
    you need to fully understand the process of studying every possible value of N_A/N in a given range of N_A and of N, to understand
    this full process. If you need guidance, please contact the corresponding author.'''
    
    #useful import
    import numpy as np
    from loading import loadinggeneric #we load results
    from saving import savinggeneric #we will save the results at the end
    
    #If the previous function was not already run, these lines can be uncommented and used to run it    
    # numens=1000
    # homo=0
    # from newcollectdata import newcollectargsimdatareview2
    # A=newcollectargsimdatareview2(homo,'no')
    
    #If the previous function was already run, this can be used to load the results.
    A=loadinggeneric('BarridoFinoReviewerFinal')

    #For properly analyzing the results, a lot of restructuring is needed.
    #This exploration involved finding every possible value of N_A/N for all N_A in range [10,100] (steps of 2) and for all N in range
    #[10,100]. We now need to find all those values of N_A/N and regroup them in an useful way for plotting.

    #initializations
    counters=[[] for i in range(6,51,2)] #this will count all values of N_A/N, also called "delta"
    
    #These initializations are the same as previous functions in this file       
    counts0=[[] for i in range(6,51,2)]
    countsdec=[[] for i in range(6,51,2)]
    countsbip=[[] for i in range(6,51,2)]
    countsother=[[] for i in range(6,51,2)]
    countspl=[[] for i in range(6,51,2)]
    countsmin=[[] for i in range(6,51,2)]
    countsosc=[[] for i in range(6,51,2)]         
    
        
    i=0
    for M in range(6,51,2):
        j=0
        alldeltas=[] #all possible values of N_A/N
        for N in range(10,101,1):
            k=0
            for NA in range(10,101,2):
                #The idea is as follows: for a fixed value of M, one particular value of N_A/N could come from different combinations of 
                #N_A and N. To find the true general behavior in all parameter space of N_A/N vs. M, we average the results of all 
                #possible combinations that give the same value of N_A/N (and this is done for each M, that is why the most outer loop is 
                #over values of M). To do this average, we create a list of N_A/Ns, and each time we find the same value as one already on
                #the list, we sum the new results to the ones already on the list. When the complete process is finished, we divide by the
                #total number of times we found each value of N_A/N, thus obtaining averages for each value of N_A/N. "counters" is the list
                #that keeps counts of how many times we encountered each value of N_A/N.
                
                newdelta=round(NA/float(N),6) #we can round these values, as we choose. When we bin the interval of values of N_A/N, this
                #will not matter (we do that in the plotting function analyzingargsimphasediagramreview).
                
                if newdelta in alldeltas: #If this newdelta was already present in our list of deltas, we update the values on the lists, summing the new ones and the old ones
                    index=alldeltas.index(newdelta)
                    counters[i][index]+=1
                    counts0[i][index]+=A[0][i][j][k]
                    countsdec[i][index]+=A[1][i][j][k]
                    countsbip[i][index]+=A[2][i][j][k]
                    countsother[i][index]+=A[3][i][j][k]
                    countspl[i][index]+=A[4][i][j][k]
                    countsmin[i][index]+=A[5][i][j][k]
                    countsosc[i][index]+=A[6][i][j][k]
                else: #if the delta is new, we create a new entry on the lists and save the new results there.
                    alldeltas.append(newdelta) 
                    counters[i].append(1)
                    counts0[i].append(A[0][i][j][k])
                    countsdec[i].append(A[1][i][j][k])
                    countsbip[i].append(A[2][i][j][k])
                    countsother[i].append(A[3][i][j][k])
                    countspl[i].append(A[4][i][j][k])
                    countsmin[i].append(A[5][i][j][k])
                    countsosc[i].append(A[6][i][j][k])
             
                k+=1           
            j+=1   
            
        sortedindexes=np.argsort(alldeltas) #we will sort the lists by increasing values of delta=N_A/N
        
        alldeltas=np.array(alldeltas)
        counters[i]=np.array(counters[i])
        counts0[i]=np.array(counts0[i])
        countsdec[i]=np.array(countsdec[i])
        countsbip[i]=np.array(countsbip[i])
        countsother[i]=np.array(countsother[i])
        countspl[i]=np.array(countspl[i])
        countsmin[i]=np.array(countsmin[i])
        countsosc[i]=np.array(countsosc[i])
        
        
        alldeltas=alldeltas[sortedindexes]
        counters[i]=counters[i][sortedindexes]
        counts0[i]=counts0[i][sortedindexes]
        countsdec[i]=countsdec[i][sortedindexes]
        countsbip[i]=countsbip[i][sortedindexes]
        countsother[i]=countsother[i][sortedindexes]
        countspl[i]=countspl[i][sortedindexes]
        countsmin[i]=countsmin[i][sortedindexes]
        countsosc[i]=countsosc[i][sortedindexes]       
             
        #Now all the lists are properly sorted 
             
        i+=1
    #Now we divide by counters to get the proper average values, and also by the number of copies in the ensamble.
    newcounts0=list(np.array(counts0)/np.array(np.array(counters)*float(100))) #The number 100 is the number of copies in the ensamble
    newcountsdec=list(np.array(countsdec)/np.array(np.array(counters)*float(100)))
    newcountsbip=list(np.array(countsbip)/np.array(np.array(counters)*float(100)))
    newcountsother=list(np.array(countsother)/np.array(np.array(counters)*float(100)))
    newcountspl=list(np.array(countspl)/np.array(np.array(counters)*float(100)))
    newcountsmin=list(np.array(countsmin)/np.array(np.array(counters)*float(100)))
    newcountsosc=list(np.array(countsosc)/np.array(np.array(counters)*float(100)))        
    
    #save the results
    savinggeneric((newcounts0,newcountsdec,newcountsbip,newcountsother,newcountspl,newcountsmin,newcountsosc,alldeltas),'BarridoFino')
    
    return newcounts0,newcountsdec,newcountsbip,newcountsother,newcountspl,newcountsmin,newcountsosc,alldeltas #also return them, if you want to use them now