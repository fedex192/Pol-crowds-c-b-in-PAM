# -*- coding: utf-8 -*-
def newloadingargumentvariables(allargs,N,homo,cb='no',numens=1000):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('D:\\Doctorado\\Simulation_Functions\\BarridoLimitado\\Nueva_ArgSim_'+str(homo)+'\\') 
    #os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSims\\'+folder+str(numens))
    if cb=='no':
        f = open('varNars='+str(allargs)+'_N='+str(N)+'_numens='+str(numens)+'_sincb.pckl', 'rb')
    elif cb=='yes':
        f = open('varNars='+str(allargs)+'_N='+str(N)+'_numens='+str(numens)+'_concb.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var

def newloadingargumentvariablesconvergente(allargs,N,homo,cb='no',numens=1000,numofrelevargs=6):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('D:\\Doctorado\\Simulation_Functions\\BarridoConvergente\\') 
    #os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSims\\'+folder+str(numens))
    f = open('N'+str(N)+'Nars'+str(allargs)+'H'+str(homo)+'cb'+cb+'M'+str(numofrelevargs)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var



def newcollectargsimdata(homo=0,cb='no'):
    #numens=50 para la de 100, 20 para la de 1000.
    import os
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    #counts0=[[] for i in range(6,101,2)]
    #countsdec=[[] for i in range(6,101,2)]
    #countsbip=[[] for i in range(6,101,2)]
    #countsother=[[] for i in range(6,101,2)]
    #countspl=[[] for i in range(6,101,2)]
    #countsmin=[[] for i in range(6,101,2)]
    #allcopies=[[] for i in range(6,101,2)]
    
    counts0=[[] for i in range(4,101,6)]
    countsdec=[[] for i in range(4,101,6)]
    countsbip=[[] for i in range(4,101,6)]
    countsother=[[] for i in range(4,101,6)]
    countspl=[[] for i in range(4,101,6)]
    countsmin=[[] for i in range(4,101,6)]
    allcopies=[[] for i in range(4,101,6)]

    i=0
#    for allargs in range(6,101,2):
#        for N in range(4,101):
    for allargs in range(4,101,6):
        for N in range(10,101,5):
            A=newloadingargumentvariables(allargs,N,homo,cb,1000)
            counts0[i].append(A[0])
            countspl[i].append(A[1])
            countsmin[i].append(A[2])
            countsbip[i].append(A[3])
            countsother[i].append(A[4])
            countsdec[i].append(A[1]+A[2])
            allcopies[i].append(A[5])
        i+=1
            
    return counts0,countsdec,countsbip,countsother,countspl,countsmin,allcopies


def collectargsimdata2(numens=1000,folder='P0.5'):
    #numens=50 para la de 100, 20 para la de 1000.
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingargumentvariables2
    counts0=[[] for i in range(6,101,2)]
    countsdec=[[] for i in range(6,101,2)]
    countsbip=[[] for i in range(6,101,2)]
    countsother=[[] for i in range(6,101,2)]
    countspl=[[] for i in range(6,101,2)]
    countsmin=[[] for i in range(6,101,2)]
    allcopies=[[] for i in range(6,101,2)]
    countsosc=[[] for i in range(6,101,2)]
    i=0
    for allargs in range(6,101,2):
        for N in range(4,101):
            A=loadingargumentvariables2(allargs,N,numens,folder)
            counts0[i].append(A[0])
            countspl[i].append(A[1])
            countsmin[i].append(A[2])
            countsbip[i].append(A[3])
            countsother[i].append(A[4])
            countsdec[i].append(A[1]+A[2])
            countsosc[i].append(A[5])
            allcopies[i].append(A[6])
        i+=1
            
    return counts0,countsdec,countsbip,countsother,countsosc,countspl,countsmin,allcopies
    

def newcollectargsimdataconvergente(homo=0,cb='no'):
    #numens=50 para la de 100, 20 para la de 1000.
    import os
    import numpy as np
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    #counts0=[[] for i in range(6,101,2)]
    #countsdec=[[] for i in range(6,101,2)]
    #countsbip=[[] for i in range(6,101,2)]
    #countsother=[[] for i in range(6,101,2)]
    #countspl=[[] for i in range(6,101,2)]
    #countsmin=[[] for i in range(6,101,2)]
    #allcopies=[[] for i in range(6,101,2)]
    
    counts0=[[] for i in range(10,101,10)]
    countsdec=[[] for i in range(10,101,10)]
    countsbip=[[] for i in range(10,101,10)]
    countsother=[[] for i in range(10,101,10)]
    countspl=[[] for i in range(10,101,10)]
    countsmin=[[] for i in range(10,101,10)]
    countsosc=[[] for i in range(10,101,10)]
    stepcountsmean=[[] for i in range(10,101,10)]
    stepcountsmedian=[[] for i in range(10,101,10)]
    tiempos=[[] for i in range(10,101,10)]    
#    allcopies=[[] for i in range(10,101,10)]

    i=0
#    for allargs in range(6,101,2):
#        for N in range(4,101):
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
            stepcountsmean[i].append(np.mean(A[1]))
            stepcountsmedian[i].append(np.median(A[1]))
            tiempos[i].append(A[2])           
            #allcopies[i].append(A[5])            
        i+=1
       
    return counts0,countsdec,countsbip,countsother,countspl,countsmin,countsosc,stepcountsmean,stepcountsmedian,tiempos
    
    
    
def newcollectargsimdatareviewer(homo=0,cb='no'):
    #numens=50 para la de 100, 20 para la de 1000.
    import os
    import numpy as np
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    #counts0=[[] for i in range(6,101,2)]
    #countsdec=[[] for i in range(6,101,2)]
    #countsbip=[[] for i in range(6,101,2)]
    #countsother=[[] for i in range(6,101,2)]
    #countspl=[[] for i in range(6,101,2)]
    #countsmin=[[] for i in range(6,101,2)]
    #allcopies=[[] for i in range(6,101,2)]
    
    counts0=[[] for i in range(6,51,2)]
    countsdec=[[] for i in range(6,51,2)]
    countsbip=[[] for i in range(6,51,2)]
    countsother=[[] for i in range(6,51,2)]
    countspl=[[] for i in range(6,51,2)]
    countsmin=[[] for i in range(6,51,2)]
    countsosc=[[] for i in range(6,51,2)]
    stepcountsmean=[[] for i in range(6,51,2)]
    stepcountsmedian=[[] for i in range(6,51,2)]
    tiempos=[[] for i in range(6,51,2)]    
#    allcopies=[[] for i in range(10,101,10)]

    i=0
#    for allargs in range(6,101,2):
#        for N in range(4,101):
    for M in range(6,51,2):
        for discrep in np.arange(0.2,2.01,0.04):
            A=newloadingargumentvariablesreviewer(round(discrep*50),discrep,homo,cb,1000,M)
            if A[0]==np.nan:
                counts0[i].append(np.nan)
                countspl[i].append(np.nan)
                countsmin[i].append(np.nan)
                countsbip[i].append(np.nan)
                countsother[i].append(np.nan)
                countsdec[i].append(np.nan)
                countsosc[i].append(np.nan)
                # stepcountsmean[i].append(np.mean(A[1]))
                # stepcountsmedian[i].append(np.median(A[1]))
                tiempos[i].append(np.nan)           
                #allcopies[i].append(A[5]) 
            else:           
                counts0[i].append(A[0][0])
                countspl[i].append(A[0][1])
                countsmin[i].append(A[0][2])
                countsbip[i].append(A[0][3])
                countsother[i].append(A[0][5])
                countsdec[i].append(A[0][1]+A[0][2])
                countsosc[i].append(A[0][4])
                # stepcountsmean[i].append(np.mean(A[1]))
                # stepcountsmedian[i].append(np.median(A[1]))
                tiempos[i].append(A[2])           
                #allcopies[i].append(A[5])                    
        i+=1
       
    return counts0,countsdec,countsbip,countsother,countspl,countsmin,countsosc,stepcountsmean,stepcountsmedian,tiempos
    
    
def newloadingargumentvariablesreviewer(allargs,discrep,homo,cb='no',numens=1000,numofrelevargs=6):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('D:\\Doctorado\\Simulation_Functions\\BarridoReviewer\\') 
    #os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSims\\'+folder+str(numens))
    f = open('N50NArs'+str(float(allargs))+'discrep'+str(discrep)+'cb'+cb+'M'+str(numofrelevargs)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def newloadingargumentvariablesreviewer2(NA,N,M,homo=0,cb='no',numens=1000):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('D:\\Doctorado\\Simulation_Functions\\BarridoReviewer\\') 
    #os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSims\\'+folder+str(numens))
    f = open('N'+str(N)+'NArs'+str(NA)+'cb'+cb+'M'+str(M)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def newcollectargsimdatareviewer2grueso(homo=0,cb='no'):
    #numens=50 para la de 100, 20 para la de 1000.
    import os
    import numpy as np
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    #counts0=[[] for i in range(6,101,2)]
    #countsdec=[[] for i in range(6,101,2)]
    #countsbip=[[] for i in range(6,101,2)]
    #countsother=[[] for i in range(6,101,2)]
    #countspl=[[] for i in range(6,101,2)]
    #countsmin=[[] for i in range(6,101,2)]
    #allcopies=[[] for i in range(6,101,2)]
    
    counts0=[[[] for j in range(10,101,5)] for i in range(6,51,2)]
    countsdec=[[[] for j in range(10,101,5)] for i in range(6,51,2)]
    countsbip=[[[] for j in range(10,101,5)] for i in range(6,51,2)]
    countsother=[[[] for j in range(10,101,5)] for i in range(6,51,2)]
    countspl=[[[] for j in range(10,101,5)] for i in range(6,51,2)]
    countsmin=[[[] for j in range(10,101,5)] for i in range(6,51,2)]
    countsosc=[[[] for j in range(10,101,5)] for i in range(6,51,2)]
    stepcountsmean=[[[] for j in range(10,101,5)] for i in range(6,51,2)]
    stepcountsmedian=[[[] for j in range(10,101,5)] for i in range(6,51,2)]
    tiempos=[[[] for j in range(10,101,5)] for i in range(6,51,2)]    
#    allcopies=[[] for i in range(10,101,10)]

    i=0
#    for allargs in range(6,101,2):
#        for N in range(4,101):
    for M in range(6,51,2):
        j=0
        for N in range(10,101,5):
            for NA in range(10,101,10):
                if N!=50:
                    A=newloadingargumentvariablesreviewer2(NA,N,M,homo,cb,1000)
                else:
                    discrep=NA/50.0
                    A=newloadingargumentvariablesreviewer(round(discrep*50),discrep,homo,cb,1000,M)                    
                if A[0]==np.nan:
                    counts0[i][j].append(np.nan)
                    countspl[i][j].append(np.nan)
                    countsmin[i][j].append(np.nan)
                    countsbip[i][j].append(np.nan)
                    countsother[i][j].append(np.nan)
                    countsdec[i][j].append(np.nan)
                    countsosc[i][j].append(np.nan)
                    # stepcountsmean[i].append(np.mean(A[1]))
                    # stepcountsmedian[i].append(np.median(A[1]))
                    tiempos[i][j].append(np.nan)           
                    #allcopies[i].append(A[5]) 
                else:           
                    counts0[i][j].append(A[0][0])
                    countspl[i][j].append(A[0][1])
                    countsmin[i][j].append(A[0][2])
                    countsbip[i][j].append(A[0][3])
                    countsother[i][j].append(A[0][5])
                    countsdec[i][j].append(A[0][1]+A[0][2])
                    countsosc[i][j].append(A[0][4])
                    # stepcountsmean[i].append(np.mean(A[1]))
                    # stepcountsmedian[i].append(np.median(A[1]))
                    tiempos[i][j].append(A[2])           
                    #allcopies[i].append(A[5])  
            j+=1                  
        i+=1
        
    return counts0,countsdec,countsbip,countsother,countspl,countsmin,countsosc,stepcountsmean,stepcountsmedian,tiempos    
    
def transformdatareviewer2():
    
    import numpy as np
    # import pylab as py
    # import copy
    from loading import loadinggeneric
    # import matplotlib.pyplot as plt
    # import matplotlib as mpl    

    # numens=1000
    # homo=0
    # from saving import savinggeneric    
    # from newcollectdata import newcollectargsimdatareviewer2grueso
    # A=newcollectargsimdatareviewer2grueso(homo,'no')
    A=loadinggeneric('BarridoGruesoReviewer')
    counters=[[] for i in range(6,51,2)]
    
    counts0=[[] for i in range(6,51,2)]
    countsdec=[[] for i in range(6,51,2)]
    countsbip=[[] for i in range(6,51,2)]
    countsother=[[] for i in range(6,51,2)]
    countspl=[[] for i in range(6,51,2)]
    countsmin=[[] for i in range(6,51,2)]
    countsosc=[[] for i in range(6,51,2)]
    # stepcountsmean=[[] for i in range(6,51,2)]
    # stepcountsmedian=[[] for i in range(6,51,2)]
    # tiempos=[[] for i in range(6,51,2)]           
    
    
    
    i=0
    for M in range(6,51,2):
        j=0
        alldeltas=[]
        for N in range(10,101,5):
            k=0
            for NA in range(10,101,10):
                newdiscrep=round(NA/float(N),2)
                if newdiscrep in alldeltas:
                    index=alldeltas.index(newdiscrep)
                    counters[i][index]+=1
                    counts0[i][index]+=A[0][i][j][k]
                    countsdec[i][index]+=A[1][i][j][k]
                    countsbip[i][index]+=A[2][i][j][k]
                    countsother[i][index]+=A[3][i][j][k]
                    countspl[i][index]+=A[4][i][j][k]
                    countsmin[i][index]+=A[5][i][j][k]
                    countsosc[i][index]+=A[6][i][j][k]
                    # stepcountsmean[i][index]+=A[7][i][j][k]
                    # stepcountsmedian[i][index]+=A[8][i][j][k]
                    # tiempos[i][index]+=A[9][i][j][k]
                else:
                    alldeltas.append(newdiscrep)
                    counters[i].append(1)
                    counts0[i].append(A[0][i][j][k])
                    countsdec[i].append(A[1][i][j][k])
                    countsbip[i].append(A[2][i][j][k])
                    countsother[i].append(A[3][i][j][k])
                    countspl[i].append(A[4][i][j][k])
                    countsmin[i].append(A[5][i][j][k])
                    countsosc[i].append(A[6][i][j][k])
                    # stepcountsmean[i].append(A[7][i][j][k])
                    # stepcountsmedian[i].append(A[8][i][j][k])
                    # tiempos[i].append(A[9][i][j][k])
             
                k+=1           
            j+=1   
            
        sortedindexes=np.argsort(alldeltas)
        
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
             
        i+=1
                    
    newcounts0=list(np.array(counts0)/np.array(np.array(counters)*float(100)))
    newcountsdec=list(np.array(countsdec)/np.array(np.array(counters)*float(100)))
    newcountsbip=list(np.array(countsbip)/np.array(np.array(counters)*float(100)))
    newcountsother=list(np.array(countsother)/np.array(np.array(counters)*float(100)))
    newcountspl=list(np.array(countspl)/np.array(np.array(counters)*float(100)))
    newcountsmin=list(np.array(countsmin)/np.array(np.array(counters)*float(100)))
    newcountsosc=list(np.array(countsosc)/np.array(np.array(counters)*float(100)))
    # newstepcountsmean=list(np.array(stepcountsmean)/np.array(np.array(counters)*float(100)))
    # newstepcountsmedian=list(np.array(stepcountsmedian)/np.array(np.array(counters)*float(100)))
    # newtiempos=list(np.array(tiempos)/np.array(np.array(counters)*float(100)))                
    
    return newcounts0,newcountsdec,newcountsbip,newcountsother,newcountspl,newcountsmin,newcountsosc,alldeltas#,newstepcountsmean,newstepcountsmedian,newtiempos