import os
#os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
#os.chdir('C:\\Users\\Fede\\Desktop\\Simulation_Functions\\') 
os.chdir('D:\\Doctorado\\Simulation_Functions\\') 

def newexplorargsim(homo=0,allargsini=4,allargsfin=101,numens=1000,opsys='w',cb='yes',numofrelevargs=5):
    from newrunargsim import newrunargsim
    from saving import newsavinggeneric
    for allargs in range(allargsini,allargsfin,6):
        #for N in range(4,101):
        print allargs
        for N in range(10,101,5):
            print N
            counts0=0
            countspl=0
            countsmin=0
            countsbip=0
            otherstuff=0
            #finalresult=[]
            #result=[]
            ensamblestates=[]
            osc=0
            for copy in range(numens):
                a=newrunargsim(allargs,allargs/2,N,numofrelevargs,5000,cb,'no',homo)
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
                ensamblestates.append((a[0][-1],a[1][-1],a[2][-1])) 
                osc+=a[-1]
                #result.append(a)
            #finalresult.append((counts0,countspl,countsmin,countsbip,otherstuff))#,result))
            
            #savingargumentsimulation((counts0,countspl,countsmin,countsbip,otherstuff,osc,ensamblestates),allargs,N,numens,opsys)#finalresult,allargs,N,numens,opsys)
            newsavinggeneric((counts0,countspl,countsmin,countsbip,otherstuff,osc,ensamblestates),specifications='Nars='+str(allargs)+'_N='+str(N)+'_numens='+str(numens)+'_concb',path='C:\\Users\\Fede\\Desktop\\Datos_Argumentos\\Nueva_ArgSim_'+str(homo)+'\\')

 
                                                    
def newexplorargsimforprofiling(homo=0,allargsini=4,allargsfin=101,numens=1000,opsys='w',cb='yes',numofrelevargs=5):
    from newrunargsim import newrunargsimforprofiling
    from saving import newsavinggeneric
    for allargs in range(allargsini,allargsfin,6):
        #for N in range(4,101):
        print allargs
        for N in range(20,21,5):
            print N
            counts0=0
            countspl=0
            countsmin=0
            countsbip=0
            otherstuff=0
            #finalresult=[]
            #result=[]
            ensamblestates=[]
            osc=0
            for copy in range(numens):
                #print(copy)
                a=newrunargsimforprofiling(allargs,allargs/2,N,numofrelevargs,5000,cb,'no',homo)
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
                ensamblestates.append((a[0][-1],a[1][-1],a[2][-1])) 
                osc+=a[-1]
                #result.append(a)
    return (counts0,countspl,countsmin,countsbip,otherstuff,osc,ensamblestates)
           

def newexplorargsimwithconvergence(homo=0,allargs=60,Nini=10,Nfin=101,cb='no',numofrelevargs=6,numens=1000,opsys='w'):
     
    from newrunargsim import newrunargsimforprofiling                                                                                                                                                                                                                                                                                                 
    import time    
    
    for N in range(Nini,Nfin,1):
        #if numofrelevargs not in range(10,50,10):
            print(N)
            t = time.time()
            counts0=0
            countspl=0
            countsmin=0
            countsbip=0
            otherstuff=0
            countsosc=0
            ensamblestates=[]
            stepcounts=[]
            i=0
            while i<1000:
                #print(i)
                a=newrunargsimforprofiling(allargs,allargs/2,N,numofrelevargs,10000,cb,'',homo,1.0,3.0,'Bid')
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
                        ensamblestates.append((a[0][-1],a[1][-1],a[2][-1])) 
                        #osc+=a[-1]    
                    stepcounts.append(a[-1])
                    i+=1
                    
            elapsed = time.time() - t  
            print(elapsed)
            # print(np.max(stepcounts))
            # print(np.mean(stepcounts))
            # print(np.median(stepcounts))
            # print(np.std(stepcounts))
            # print(countsosc)
            from saving import savinggeneric
            savinggeneric(((counts0,countspl,countsmin,countsbip,countsosc,otherstuff),stepcounts,elapsed),'N'+str(N)+'Nars'+str(allargs)+'H'+str(homo)+'cb'+cb+'M'+str(numofrelevargs),path='D:\\Doctorado\\Simulation_Functions\\BarridoM\\')
            #'C:\\Users\\Fede\\Desktop\\Simulation_Functions\\BarridoConvergente\\')
            
            
            
def newexplorargsimwithconvergenceforprofiling2(homo=0,allargs=60,Nini=10,Nfin=101,cb='no',numofrelevargs=6,numens=1000,opsys='w'):
    #import time    
    #t = time.time()
    from newrunargsim import newrunargsimforprofiling                                                                                                                                                                                                                                                                                                 
    
    import numpy as np
    
    for N in np.arange(Nini,Nfin,1):
        if N not in np.arange(1000,1001,10):
            print(N)
            
            counts0=0
            countspl=0
            countsmin=0
            countsbip=0
            otherstuff=0
            countsosc=0
            ensamblestates=[]
            stepcounts=[]
            i=0
            while i<1000:
                #print(i)
                a=newrunargsimforprofiling(allargs,allargs/2,N,numofrelevargs,10000,cb,'',homo,1.0,3.0,'Bid')
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
                        ensamblestates.append((a[0][-1],a[1][-1],a[2][-1])) 
                        #osc+=a[-1]    
                    stepcounts.append(a[-1])
                    i+=1
                    
            #elapsed = time.time() - t  
            #return elapsed
            
            #print(np.max(stepcounts))
            #print(np.mean(stepcounts))
            #print(np.median(stepcounts))
            #print(np.std(stepcounts))
            #print(countsosc)
            from saving import savinggeneric
            savinggeneric(((counts0,countspl,countsmin,countsbip,countsosc,otherstuff),stepcounts),'Probandocosas',path='C:\\Users\\Fede\\Desktop\\Simulation_Functions\\BarridoConvergente\\')
        

def newexplorargsimwithconvergencereviewer(numofrelevargs=6,discrepini=0.2,discrepfini=2.01,cb='no',homo=0,numens=1000,opsys='w'):
    import numpy as np
    from newrunargsim import newrunargsimforprofiling                                                                                                                                                                                                                                                                                                 
    import time    
    
    N=50;  
    
    for discrep in np.arange(discrepini,discrepfini,0.04):            
        NA=round(discrep*N);
        if numofrelevargs<NA:
            #if numofrelevargs not in range(10,50,10):
            print(NA)
            t = time.time()
            counts0=0
            countspl=0
            countsmin=0
            countsbip=0
            otherstuff=0
            countsosc=0
            ensamblestates=[]
            stepcounts=[]
            i=0
            while i<1000:
                #print(i)
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
                        ensamblestates.append((a[0][-1],a[1][-1],a[2][-1])) 
                        #osc+=a[-1]    
                    stepcounts.append(a[-1])
                    i+=1
                    
            elapsed = time.time() - t  
            print(elapsed)
            # print(np.max(stepcounts))
            # print(np.mean(stepcounts))
            # print(np.median(stepcounts))
            # print(np.std(stepcounts))
            # print(countsosc)
            from saving import savinggeneric
            savinggeneric(((counts0,countspl,countsmin,countsbip,countsosc,otherstuff),stepcounts,elapsed),'N'+str(N)+'Nars'+str(NA)+'discrep'+str(discrep)+'cb'+cb+'M'+str(numofrelevargs),path='D:\\Doctorado\\Simulation_Functions\\BarridoReviewer\\')
            #'C:\\Users\\Fede\\Desktop\\Simulation_Functions\\BarridoConvergente\\')
        else:
            from saving import savinggeneric
            savinggeneric(((np.nan,np.nan,np.nan,np.nan,np.nan,np.nan),np.nan,np.nan),'N'+str(N)+'Nars'+str(NA)+'discrep'+str(discrep)+'cb'+cb+'M'+str(numofrelevargs),path='D:\\Doctorado\\Simulation_Functions\\BarridoReviewer\\')

#Para hacer los de evoluciones de argumentos, correr esto, y guardarlo con savinggeneric:
#evolutions=plottingarguments(tipo=5,cb='no',Ars=60,N=10,rel=6,l=0,bins=1,chosen='consenso2')
#from saving import savinggeneric
#savinggeneric(evolutions,'consenso1evolcbno10rel6bines1ens100')
#savinggeneric(evolutions,'consenso2evolcbno10rel6bines1ens100')
#savinggeneric(indeciso,'consenso1evolcbno10rel6bines1ens100')

def newexplorargsimwithconvergencereviewer2(numofrelevargs=6,cb='no',homo=0,numens=1000,opsys='w'):
    import numpy as np
    from newrunargsim import newrunargsimforprofiling                                                                                                                                                                                                                                                                                                 
    import time    

    for N in np.arange(99,100,1):
        print(N)
        for NA in range(10,101,2):
            print(NA)            
            if numofrelevargs<NA:
                if not (N in range(10,101,5) and NA in range(10,101,10)):
                #if numofrelevargs not in range(10,50,10):                
                    t = time.time()
                    counts0=0
                    countspl=0
                    countsmin=0
                    countsbip=0
                    otherstuff=0
                    countsosc=0
                    ensamblestates=[]
                    stepcounts=[]
                    i=0
                    while i<100:
                        #print(i)
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
                                ensamblestates.append((a[0][-1],a[1][-1],a[2][-1])) 
                                #osc+=a[-1]    
                            stepcounts.append(a[-1])
                            i+=1
                            
                    elapsed = time.time() - t  
                    print(elapsed)
                    # print(np.max(stepcounts))
                    # print(np.mean(stepcounts))
                    # print(np.median(stepcounts))
                    # print(np.std(stepcounts))
                    # print(countsosc)
                    from saving import savinggeneric
                    savinggeneric(((counts0,countspl,countsmin,countsbip,countsosc,otherstuff),stepcounts,elapsed),'N'+str(N)+'Nars'+str(NA)+'cb'+cb+'M'+str(numofrelevargs),path='D:\\Doctorado\\Simulation_Functions\\BarridoReviewer\\')
                    #'C:\\Users\\Fede\\Desktop\\Simulation_Functions\\BarridoConvergente\\')
            else:
                from saving import savinggeneric
                savinggeneric(((np.nan,np.nan,np.nan,np.nan,np.nan,np.nan),np.nan,np.nan),'N'+str(N)+'Nars'+str(NA)+'cb'+cb+'M'+str(numofrelevargs),path='D:\\Doctorado\\Simulation_Functions\\BarridoReviewer2\\')
