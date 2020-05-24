'''This functions were used for exploring the relationship between N_A/N vs. M. We originally named N_A/N as "discrepancy", and later
renamed it as "Delta", hence the name of the file. The first function was used to study a special case, where the quotient N_A/N was
only used with N=50 (fixed). It can be though of as an exploration of M vs. N_A for fixed N=50, but using this particular N allows us
to explore the most important values of N_A/N vs. M (from N_A/N = 0.1 to 2). The second function was used to explore this quotient varying
both N and N_A, and is much more general.'''

def newexplorargsimwithconvergencereview(numofrelevargs=6,discrepini=0.2,discrepfini=2.01,cb='no',homo=0,numens=1000,opsys='w'):
    '''As mentioned, this was used to study the special case of N_A/N vs M with N=50.
    "numofrelevargs" is M, the memory size (originally name as such).
    "discrepini" is the first value of N_A/N to be explored.
    "discrepfini" is the last value of N_A/N to be explored.
    "cb" is the presence (cb='yes') or abscence (cb='no') of confirmation bias.
    "homo" is the homophily parameter (homo=0 means no homophily).
    "numens" is the number of copies of the ensamble.
    "opsys" is obsolete, it was used to change saving options.
    '''
    import numpy as np
    from newrunargsim import newrunargsimforprofiling #main simulation function                                                                                                                                                                                                                                                                                                 
    import time #to keep track of time
    
    N=50; #fixed number of agents
    
    for discrep in np.arange(discrepini,discrepfini,0.04): #0.04 is the minimum step size if N=50. It means that N_A increases in steps of 2.
        NA=round(discrep*N); #find N_A
        if numofrelevargs<NA: #if this is false, then it makes no physical sense, since agents remember more arguments than the existing ones.
            #if numofrelevargs not in range(10,50,10):
            print(NA) #keep track of progress
            t = time.time() #check initial time
            #initializations:
            counts0=0
            countspl=0
            countsmin=0
            countsbip=0
            otherstuff=0
            countsosc=0
            stepcounts=[]
            i=0
            while i<numens: #save only those copies without oscillations, until reaching numens.
                #print(i)
                a=newrunargsimforprofiling(NA,NA/2,N,numofrelevargs,10000,cb,'',homo,1.0,3.0,'Bid')
                if a[3]==1:
                    countsosc+=1 #if it is an oscillating state, only add one to the count, do nothing else
                else: #if not, procede as usual
                    #add 1 to the count of the state found
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
                    stepcounts.append(a[-1]) #keep track of the number of steps
                    i+=1
                    
            elapsed = time.time() - t  #save elapsed time
            print(elapsed) #print it so it can be seen on the console
            
            #now we save the results. Change directory if used in another computer
            from saving import savinggeneric
            savinggeneric(((counts0,countspl,countsmin,countsbip,countsosc,otherstuff),stepcounts,elapsed),'N'+str(N)+'Nars'+str(NA)+'discrep'+str(discrep)+'cb'+cb+'M'+str(numofrelevargs),path='D:\\Doctorado\\Simulation_Functions\\BarridoReviewer\\')
        else: #if we are in those cases without physical sense, we save nans. This simplifies analyisis of results.
            
            from saving import savinggeneric
            savinggeneric(((np.nan,np.nan,np.nan,np.nan,np.nan,np.nan),np.nan,np.nan),'N'+str(N)+'Nars'+str(NA)+'discrep'+str(discrep)+'cb'+cb+'M'+str(numofrelevargs),path='D:\\Doctorado\\Simulation_Functions\\BarridoReviewer\\')

def newexplorargsimwithconvergencereview2(numofrelevargs=6,cb='no',homo=0,numens=1000,opsys='w'):
    '''This function generalizes the one preceding it. We will not repeat the comments already present in the preceding one, but add new
    comments for new pieces of code. We do not need discrepini and discrepfini anymore.'''
    
    import numpy as np
    from newrunargsim import newrunargsimforprofiling                                                                                                                                                                                                                                                                                                 
    import time    

    for N in np.arange(10,100,1): #loop over N
        print(N) #keep track of N
        for NA in range(10,101,2): #loop over N_A
            print(NA) #keep track of N_A
            if numofrelevargs<NA:
                    t = time.time()
                    counts0=0
                    countspl=0
                    countsmin=0
                    countsbip=0
                    otherstuff=0
                    countsosc=0
                    stepcounts=[]
                    i=0
                    while i<100: #this exploration is VERY time consuming. We used only 100 copies (the results are the same).
                        a=newrunargsimforprofiling(NA,NA/2,N,numofrelevargs,10000,cb,'',homo,1.0,3.0,'Bid')
                        if a[3]==1:
                            countsosc+=1   
                        else:
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
                            stepcounts.append(a[-1])
                            i+=1
                            
                    elapsed = time.time() - t  
                    print(elapsed)
                    
                    from saving import savinggeneric
                    savinggeneric(((counts0,countspl,countsmin,countsbip,countsosc,otherstuff),stepcounts,elapsed),'N'+str(N)+'Nars'+str(NA)+'cb'+cb+'M'+str(numofrelevargs),path='D:\\Doctorado\\Simulation_Functions\\BarridoReviewer\\')
            else:
                from saving import savinggeneric
                savinggeneric(((np.nan,np.nan,np.nan,np.nan,np.nan,np.nan),np.nan,np.nan),'N'+str(N)+'Nars'+str(NA)+'cb'+cb+'M'+str(numofrelevargs),path='D:\\Doctorado\\Simulation_Functions\\BarridoReviewer2\\')
