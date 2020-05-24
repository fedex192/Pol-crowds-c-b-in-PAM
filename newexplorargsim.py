'''These functions are used for exploring the free parameters of the model, N and N_A (M was explored in two separate files)'''

#We start by choosing the directory:
import os
#os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
#os.chdir('C:\\Users\\Fede\\Desktop\\Simulation_Functions\\') 
os.chdir('D:\\Doctorado\\Simulation_Functions\\') 

def newexplorargsimforprofiling(homo=0,allargsini=6,allargsfin=101,numens=1000,opsys='w',cb='yes',numofrelevargs=5):
    '''This function was used for exploring the parameters N and N_A. As seen in other functions, here we call N_A as allargs.
    "homo" is the homophily parameter.
    "allargsini" is the smallest number of arguments considered for the exploration.
    "allargsfin" is the largest number of arguments considered for the exploration.
    "numens" is the number of copies in the ensamble.
    "opsys" is obsolete, it was originally used for selecting different saving options.
    "cb" is the presence (cb='yes') or abscence (cb='no') of confirmation bias.
    "numofrelevargs" is M, the memory size (originally named as number of relevant arguments).
    This function does not return anything, but saves the results.'''
    
    from newrunargsim import newrunargsimforprofiling #the main simulation function
    from saving import savinggeneric #generic saving method
    for allargs in range(allargsini,allargsfin,2): #the number of arguments must be even, so the step should be even too.
        print allargs #for keeping track
        for N in range(10,101,1):
            #print N #in case more subtle tracking is required
            
            #initializations
            counts0=0
            countspl=0
            countsmin=0
            countsbip=0
            otherstuff=0
            ensamblestates=[]
            osc=0 #in case of oscillations
            for copy in range(numens):
                #We run the simulation:
                a=newrunargsimforprofiling(allargs,allargs/2,N,numofrelevargs,5000,cb,'no',homo)
                #check how many of each final state occurred
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
                #save subtler results for deeper analysis (like checking if bipolarization was 50-50 or not).
                ensamblestates.append((a[0][-1],a[1][-1],a[2][-1])) 
                #save the number of oscillations encountered
                osc+=a[-1]            
                
            #We save the results. The path must be changed for using it in another computer.
            savinggeneric((counts0,countspl,countsmin,countsbip,otherstuff,osc,ensamblestates),specifications='Nars='+str(allargs)+'_N='+str(N)+'_numens='+str(numens)+'_concb',path='C:\\Users\\Fede\\Desktop\\Datos_Argumentos\\Nueva_ArgSim_'+str(homo)+'\\')
       

def newexplorargsimwithconvergence(homo=0,allargs=60,Nini=10,Nfin=101,cb='no',numofrelevargs=6,numens=1000,opsys='w'):
    '''This function does the same as the preceding one, but it ignores oscillating states, and instead keeps running
    simulations until "numens" non-oscillating copies have been obtained. Using either function gives the same results. This
    function also allows for testing the time it takes to perform the simulations. Only the new lines are commented. New inputs:
        "Nini" is the initial value of N to explore.
        "Nfin" is the final value of N to explore.
        '''
     
    from newrunargsim import newrunargsimforprofiling                                                                                                                                                                                                                                                                                                 
    import time #for keeping track of time
    
    for N in range(Nini,Nfin,1): #This time we only explore N inside the function. N_A must be epxlored with a loop that goes over this function.
            print(N) 
            t = time.time() #initial time
            counts0=0
            countspl=0
            countsmin=0
            countsbip=0
            otherstuff=0
            countsosc=0
            ensamblestates=[]
            stepcounts=[] #initialize stepcount
            i=0
            while i<numens: #while instead of for.
                a=newrunargsimforprofiling(allargs,allargs/2,N,numofrelevargs,10000,cb,'',homo,1.0,3.0,'Bid')
                if a[3]==1: #if it is an oscillation, we keep track of it, but do nothing else.
                    countsosc+=1   
                else: #if it is not, procede as the previous function:
                    if a[1][-1]==N and a[3]!=1:
                        countspl+=1
                    elif a[2][-1]==N and a[3]!=1:
                        countsmin+=1
                    elif a[0][-1]==N and a[3]!=1:
                        counts0+=1
                    elif a[0][-1]==0 and a[1][-1]!=N and a[2][-1]!=N and a[3]!=1:
                        countsbip+=1    
                    else:
                        otherstuff+=1
                        ensamblestates.append((a[0][-1],a[1][-1],a[2][-1])) 
                    stepcounts.append(a[-1]) #We also save how many steps where used.
                    i+=1
                    
            elapsed = time.time() - t  #see how much time has passed.
            print(elapsed) #print it, for keeping track of it on the console.
            
            from saving import savinggeneric
            savinggeneric(((counts0,countspl,countsmin,countsbip,countsosc,otherstuff),stepcounts,elapsed),'N'+str(N)+'Nars'+str(allargs)+'H'+str(homo)+'cb'+cb+'M'+str(numofrelevargs),path='D:\\Doctorado\\Simulation_Functions\\BarridoM\\')