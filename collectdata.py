# -*- coding: utf-8 -*-
def collectargsimdata(numens=1000,cb='no'):
    #numens=50 para la de 100, 20 para la de 1000.
    import os
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    from loading import loadingargumentvariables
    #counts0=[[] for i in range(6,101,2)]
    #countsdec=[[] for i in range(6,101,2)]
    #countsbip=[[] for i in range(6,101,2)]
    #countsother=[[] for i in range(6,101,2)]
    #countspl=[[] for i in range(6,101,2)]
    #countsmin=[[] for i in range(6,101,2)]
    #allcopies=[[] for i in range(6,101,2)]
    
    counts0=[[] for i in range(10,101,2)]
    countsdec=[[] for i in range(10,101,2)]
    countsbip=[[] for i in range(10,101,2)]
    countsother=[[] for i in range(10,101,2)]
    countspl=[[] for i in range(10,101,2)]
    countsmin=[[] for i in range(10,101,2)]
    allcopies=[[] for i in range(10,101,2)]

    i=0
#    for allargs in range(6,101,2):
#        for N in range(4,101):
    for allargs in range(10,101,2):
        for N in range(10,101):
            A=loadingargumentvariables(allargs,N,numens,cb)
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
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
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

def collectargsimdatarel(numens=1000,folder='FullExploration'):
    #numens=50 para la de 100, 20 para la de 1000.
    import os
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    from loading import loadingargumentvariablesrel
    counts0=[[] for i in range(5,56,5)]
    countsdec=[[] for i in range(5,56,5)]
    countsbip=[[] for i in range(5,56,5)]
    countsother=[[] for i in range(5,56,5)]
    countspl=[[] for i in range(5,56,5)]
    countsmin=[[] for i in range(5,56,5)]
    allcopies=[[] for i in range(5,56,5)]
    countsosc=[[] for i in range(5,56,5)]
    i=0
    for rel in range(5,56,5):
        for N in range(10,111,5):
            A=loadingargumentvariablesrel(rel,N,numens,folder)
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

def collectargsimdatarelars(numens=1000,folder='FullExploration'):
    #numens=50 para la de 100, 20 para la de 1000.
    import os
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    from loading import loadingargumentvariablesrelars
    counts0=[[] for i in range(5,56,5)]
    countsdec=[[] for i in range(5,56,5)]
    countsbip=[[] for i in range(5,56,5)]
    countsother=[[] for i in range(5,56,5)]
    countspl=[[] for i in range(5,56,5)]
    countsmin=[[] for i in range(5,56,5)]
    allcopies=[[] for i in range(5,56,5)]
    countsosc=[[] for i in range(5,56,5)]
    i=0
    for rel in range(5,56,5):
        for Ars in range(10,113,6):
            A=loadingargumentvariablesrelars(rel,Ars,numens,folder)
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



def collectdata(N,typ='normal'):
    import os
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    from loading import loading
    import numpy as np
    alldata=[]
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    if N==10:
        interval=range(1,100,10)
    elif N==11:
        interval=np.linspace(1,99,N)
    elif N==20:
        interval=range(1,100,5)
    elif N==50:
        interval=range(1,100,2)
    else:
        interval=range(1,100)
    if typ=='normal':
        kind='temp'
    else:
        kind='temp4'
    for P0 in interval:
        alldataund=[]
        alldatapl=[]
        alldatami=[]
        for delta in range(1,100):
            a=loading('fix'+str(round(0.01*delta,2))+'delta',round(0.01*round(P0),2),'trio',kind,N)
            alldataund.append(a[0])
            alldatapl.append(a[1])
            alldatami.append(a[2])
            #Cada uno de estos va a ser una lista con los valores para cada delta. Esos valores, a su vez,
            #constituyen listas de los valores para indecisos y demás, sin promediar en ensambles.
        #Ahora que tengo todos los deltas guardados, junto los tres tipos en un tuple, y los guardo como un P0.
        #De esta manera, quedan con la misma estructura que salía de collectdata1.
        alldata.append((alldataund,alldatapl,alldatami))
    return alldata

def collectdata1000(N):
    import os
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    from loading import loading
    alldata=[]
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    for P0 in range(1,100):
        alldataund=[]
        alldatapl=[]
        alldatami=[]
        for delta in range(1,100):
            alldataund.append(loading('fix'+str(0.01*delta)+'deltaandP0withP0',0.01*P0,'und','temp',N))
            alldatapl.append(loading('fix'+str(0.01*delta)+'deltaandP0withP0',0.01*P0,'pl','temp',N))
            alldatami.append(loading('fix'+str(0.01*delta)+'deltaandP0withP0',0.01*P0,'mi','temp',N))
            #Cada uno de estos va a ser una lista con los valores para cada delta. Esos valores, a su vez,
            #constituyen listas de los valores para indecisos y demás, sin promediar en ensambles.
        #Ahora que tengo todos los deltas guardados, junto los tres tipos en un tuple, y los guardo como un P0.
        #De esta manera, quedan con la misma estructura que salía de collectdata1.
        alldata.append((alldataund,alldatapl,alldatami))
    return alldata 

def collectdatasmall(N):
    import os
    import numpy as np
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    from loading import loading
    alldata=[]
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    if N==10 or N==1:
        interval=range(1,100,10)
    elif N==11:
        interval=np.linspace(1,99,N)
    elif N==20:
        interval=range(1,100,5)
    elif N==50:
        interval=range(1,100,2)
    else:
        interval=range(1,100)
    for P0 in interval:
        alldataund=[]
        alldatapl=[]
        alldatami=[]
        for delta in range(1,100):
            a=loading('fix'+str(0.01*delta)+'delta',round(0.01*P0,2),'trio','temp2',N)
            alldataund.append(a[0])
            alldatapl.append(a[1])
            alldatami.append(a[2])
            #Cada uno de estos va a ser una lista con los valores para cada delta. Esos valores, a su vez,
            #constituyen listas de los valores para indecisos y demás, sin promediar en ensambles.
        #Ahora que tengo todos los deltas guardados, junto los tres tipos en un tuple, y los guardo como un P0.
        #De esta manera, quedan con la misma estructura que salía de collectdata1.
        alldata.append((alldataund,alldatapl,alldatami))
    return alldata

def collectdatasmallwithppl(N):
    import os
    import numpy as np
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    from loading import loading
    alldata=[]
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    if N==10 or N==1 or N==2:
        interval=range(1,100,10)
    elif N==11:
        interval=np.linspace(1,99,N)
    elif N==20:
        interval=range(1,100,5)
    elif N==50:
        interval=range(1,100,2)
    else:
        interval=range(1,100)
    for P0 in interval:
        alldataund=[]
        alldatapl=[]
        alldatami=[]
        for delta in range(1,100):
            a=loading('fix'+str(0.01*delta)+'delta',round(0.01*P0,2),'trio','temp5',N)
            alldataund.append(a[0])
            alldatapl.append(a[1])
            alldatami.append(a[2])
            #Cada uno de estos va a ser una lista con los valores para cada delta. Esos valores, a su vez,
            #constituyen listas de los valores para indecisos y demás, sin promediar en ensambles.
        #Ahora que tengo todos los deltas guardados, junto los tres tipos en un tuple, y los guardo como un P0.
        #De esta manera, quedan con la misma estructura que salía de collectdata1.
        alldata.append((alldataund,alldatapl,alldatami))
    return alldata
    
        
                
def collectdatasmall10(N):
    import os
    import numpy as np
    os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
    from loading import loading
    alldata=[]
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    if N==10:
        interval=range(1,100,10)
    elif N==11:
        interval=np.linspace(1,99,N)
    for P0 in interval:
        alldataund=[]
        alldatapl=[]
        alldatami=[]
        for delta in range(1,100):
            a=loading('fix'+str(0.01*delta)+'delta',round(0.01*P0,2),'trio','ten',N)
            alldataund.append(a[0])
            alldatapl.append(a[1])
            alldatami.append(a[2])
            #Cada uno de estos va a ser una lista con los valores para cada delta. Esos valores, a su vez,
            #constituyen listas de los valores para indecisos y demás, sin promediar en ensambles.
        #Ahora que tengo todos los deltas guardados, junto los tres tipos en un tuple, y los guardo como un P0.
        #De esta manera, quedan con la misma estructura que salía de collectdata1.
        alldata.append((alldataund,alldatapl,alldatami))
    return alldata


def collectdata10000(N):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loading
    alldata=[]
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    for P0 in range(1,100):
        alldataund=[]
        alldatapl=[]
        alldatami=[]
        for delta in range(1,100):
            alldataund.append(loading('fix'+str(0.01*delta)+'deltaandP0withP0',0.01*P0,'und','full',N))
            alldatapl.append(loading('fix'+str(0.01*delta)+'deltaandP0withP0',0.01*P0,'pl','full',N))
            alldatami.append(loading('fix'+str(0.01*delta)+'deltaandP0withP0',0.01*P0,'mi','full',N))
            #Cada uno de estos va a ser una lista con los valores para cada delta. Esos valores, a su vez,
            #constituyen listas de los valores para indecisos y demás, sin promediar en ensambles.
        #Ahora que tengo todos los deltas guardados, junto los tres tipos en un tuple, y los guardo como un P0.
        #De esta manera, quedan con la misma estructura que salía de collectdata1.
        alldata.append((alldataund,alldatapl,alldatami))
    return alldata
    
    
def collectdataoneforalljustfinalstatesonecopy(N,copy='bis'):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingoneforall
    alldata=[]
    for P0 in range(1,100):
        deltadata=[]
        for delta in range(1,100):
            deltadata.append(loadingoneforall(round(0.01*P0,2),round(0.01*delta,2),N,'Int Grupal - Grupos Variables - N=',copy)[0][0][0][-1])
        alldata.append(deltadata)

    return alldata

def collectdatapairjustfinalstatesonecopy(N,tipo=''):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingpair
    alldata=[]
    for P0 in range(1,100):
        deltadata=[]
        for delta in range(1,100):
            deltadata.append(loadingpair(round(0.01*P0,2),round(0.01*delta,2),N,'Int Pares - Grupos Variables - N=',tipo)[0][0][-1])
        alldata.append(deltadata)

    return alldata
    
    
def collectdataoneforalljustfinalstates(N,numens):
    #numens=50 para la de 100, 20 para la de 1000.
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingoneforall
    from saving import savinggeneric
    alldata=[]
    for P0 in range(1,100):
        print P0
        deltadata=[]
        for delta in range(1,100):
            enscopy=[]
            for copy in range(numens):
                A=loadingoneforall(round(0.01*P0,2),round(0.01*delta,2),N)[0][copy][0][-1]
                B=(sum([A[i][0] for i in range(len(A))]),sum([A[i][1] for i in range(len(A))]),sum([A[i][2] for i in range(len(A))]))
                enscopy.append(B)
            deltadata.append(enscopy)
        alldata.append(deltadata)
        savinggeneric(deltadata,'P0='+str(P0))
    return alldata
#A=collectdataoneforalljustfinalstates(100,50)    
def collectdataoneforall100():
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions')
    from loading import loadinggeneric
    from saving import savinggeneric
    alldata=[]
    for P0 in range(1,100):
       alldata.append(loadinggeneric('P0='+str(P0),'C:\\Users\\Guillermo Lemarchand\\Desktop\\Avances de la Tesis\\Segunda Parte\\Grupos Variables\\One For All\\P0s\\')) 
    savinggeneric(alldata,'gruposvariablesgrupalpostaN100')

def collectdatapairjustfinalstatesbeta(N=100,numens=50):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingpair
    alldata=[]
    for P0 in range(1,100):
        deltadata=[]
        for delta in range(1,100):
            enscopy=[]
            for copy in range(numens):
                A=loadingpair(round(0.01*P0,2),round(0.01*delta,2),N)[0][copy][-1]
                T0=sum([A[0][i][-1] for i in range(len(A[0]))])
                Tpl=sum([A[1][i][-1] for i in range(len(A[1]))])
                Tmin=sum([A[2][i][-1] for i in range(len(A[2]))])                
                enscopy.append((T0,Tpl,Tmin))
            deltadata.append(enscopy)
        alldata.append(deltadata)

    return alldata
    
def collectdatapairjustfinalstates(N=100,numens=50):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingpair
    alldata=[]
    for P0 in range(1,100):
        deltadata=[]
        print P0
        for delta in range(1,100):
            enscopy=[]
            for copy in range(numens):            
                enscopy.append(loadingpair(round(0.01*P0,2),round(0.01*delta,2),N)[0][copy])
            deltadata.append(enscopy)
        alldata.append(deltadata)

    return alldata
    
def collectdataoneforalljustfinalstates1000(N=1000,numens=20):
    #numens=50 para la de 100, 20 para la de 1000.
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingoneforall
    alldata=[]
    for P0 in range(1,100):
        deltadata=[]
        print P0
        for delta in range(1,100):
            enscopy=[]
            for copy in range(numens):
                enscopy.append(loadingoneforall(round(0.01*P0,2),round(0.01*delta,2),N)[0][copy][0])
            deltadata.append(enscopy)
        alldata.append(deltadata)
    return alldata


def collectdatapairjustfinalstatesconvergence(N=100,numens=1000):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingpair
    alldatamaxes=[[] for i in range(99)]
    alldatameans=[[] for i in range(99)]
    for P0 in range(1,100):
        print P0
        for delta in range(1,100):
            a=loadingpair(round(0.01*P0,2),round(0.01*delta,2),N,'Int Pares - Grupos Variables - N=','Convergence')[0]
            alldatamaxes[P0-1].append(a[0])
            alldatameans[P0-1].append(a[1])

    return alldatamaxes,alldatameans
        
                
def collectdataoneforalljustfinalstatesconvergence(N=100,numens=1000):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingoneforall
    alldatamaxes=[[] for i in range(99)]
    alldatameans=[[] for i in range(99)]
    for P0 in range(1,100):
        print P0
        for delta in range(1,100):
            a=loadingoneforall(round(0.01*P0,2),round(0.01*delta,2),N,'Int Grupal - Grupos Variables - N=','Convergence')[0]
            alldatamaxes[P0-1].append(a[0])
            alldatameans[P0-1].append(a[1])

    return alldatamaxes,alldatameans
    
    
 #   loadingpair(P0,delta,N=100,folder='Int Pares - Grupos Variables - N=',specifications='')
 
def collectdataoneforalljustfinalstatesforgroupanalysis(N=100,numens=100):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingoneforall
    alldatacounts0=[[] for i in range(99)]
    alldatacountsdec=[[] for i in range(99)]
    alldatacounts0new=[[] for i in range(99)]
    alldatacountsdecnew=[[] for i in range(99)]
    for P0 in range(1,100):
        print P0
        for delta in range(1,100):
            a=loadingoneforall(round(0.01*P0,2),round(0.01*delta,2),N,'IntGrupalN','forgroupanalysis')[0]
            totalcount0=0
            totalcountdec=0
            totalcountbip=0
            count0dec=0
            countbipdec=0
            for i in range(len(a)):
                count0=0
                countdec=0
                countbip=0
                for j in range(len(a[0])):
                    if N/10 in a[i][j][1:]:
                        countdec+=1
                        totalcountdec+=1
                    elif N/10==a[i][j][0]:
                        count0+=1
                        totalcount0+=1
                    else:
                        countbip+=1
                        totalcountbip+=1
                if count0!=0 and countdec!=0:
                    count0dec+=1
                if countbip!=0 and countdec!=0:
                    countbipdec+=1
                    
            alldatacounts0[P0-1].append(totalcount0/numens)
            alldatacountsdec[P0-1].append(totalcountdec/numens)
            alldatacounts0new[P0-1].append(count0dec/float(numens))
            alldatacountsdecnew[P0-1].append(countbipdec/float(numens))

    return alldatacounts0,alldatacountsdec,alldatacounts0new,alldatacountsdecnew

def collectdatapairsjustfinalstatesforgroupanalysis(N=100,numens=100):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingpair
    alldatacounts0=[[] for i in range(99)]
    alldatacountsdec=[[] for i in range(99)]
    alldatacounts0new=[[] for i in range(99)]
    alldatacountsdecnew=[[] for i in range(99)]
    for P0 in range(1,100):
        print P0
        for delta in range(1,100):
            a=loadingpair(round(0.01*P0,2),round(0.01*delta,2),N,'IntParesN','forgroupanalysis')[0]
            totalcount0=0
            totalcountdec=0
            totalcountbip=0
            count0dec=0
            countbipdec=0
            for i in range(len(a)):
                count0=0
                countdec=0
                countbip=0
                for j in range(len(a[0])):
                    if N/10 in a[i][j][1:]:
                        countdec+=1
                        totalcountdec+=1
                    elif N/10==a[i][j][0]:
                        count0+=1
                        totalcount0+=1
                    else:
                        countbip+=1
                        totalcountbip+=1
                if count0!=0 and countdec!=0:
                    count0dec+=1
                if countbip!=0 and countdec!=0:
                    countbipdec+=1
                    
            alldatacounts0[P0-1].append(totalcount0/numens)
            alldatacountsdec[P0-1].append(totalcountdec/numens)                    
            alldatacounts0new[P0-1].append(count0dec/float(numens))
            alldatacountsdecnew[P0-1].append(countbipdec/float(numens))

    return alldatacounts0,alldatacountsdec,alldatacounts0new,alldatacountsdecnew
    
def collectdatadistrpop(N,alpha,kind='normal'):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingdistrpop
    import numpy as np
    alldata=[]
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    interval=range(1,100)
    for P0 in interval:
        alldataund=[]
        alldatapl=[]
        alldatami=[]
        for delta in range(1,100):
            a=loadingdistrpop('fix'+str(round(0.01*delta,2))+'delta',round(0.01*round(P0),2),'trio',kind,N,alpha)
            alldataund.append(a[0])
            alldatapl.append(a[1])
            alldatami.append(a[2])
        alldata.append((alldataund,alldatapl,alldatami))
    return alldata
    
def collectdatadistrpopsmall(N,alpha,kind='normal'):
    import os
    import numpy as np
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingdistrpop
    alldata=[]
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    if N==10:
        interval=range(1,100,10)
    for P0 in interval:
        alldataund=[]
        alldatapl=[]
        alldatami=[]
        for delta in range(1,100):
            a=loadingdistrpop('fix'+str(0.01*delta)+'delta',round(0.01*P0,2),'trio',kind,N,alpha)
            alldataund.append(a[0])
            alldatapl.append(a[1])
            alldatami.append(a[2])
            #Cada uno de estos va a ser una lista con los valores para cada delta. Esos valores, a su vez,
            #constituyen listas de los valores para indecisos y demás, sin promediar en ensambles.
        #Ahora que tengo todos los deltas guardados, junto los tres tipos en un tuple, y los guardo como un P0.
        #De esta manera, quedan con la misma estructura que salía de collectdata1.
        alldata.append((alldataund,alldatapl,alldatami))
    return alldata
    
def collectdatafinalgroupsimulation(inf=0.1,N=1000,Nen=20):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingfinalgroupsimulation
    import numpy as np

    alldataund=[]
    alldatapl=[]
    alldatami=[]
    if inf==0.0001:
        interval=range(60,100)
    else:
        interval=range(1,100)
    for P0 in interval:
        a=loadingfinalgroupsimulation(round(0.01*P0,2),inf,N,Nen)[0]
        alldataund.append(a[0])
        alldatapl.append(a[1])
        alldatami.append(a[2])
    return alldataund,alldatapl,alldatami
    
def collectdatafinalgroupsimulationformissingdeltas(inf=0.1,N=1000,Nen=20):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingfinalgroupsimulationformissingdeltas
    import numpy as np
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    interval=range(1,100)
    for P0 in interval:
        alldataund1=[]
        alldatapl1=[]
        alldatami1=[]
        for delta in range(1,10):
            a=loadingfinalgroupsimulationformissingdeltas(round(0.01*P0,2),round(0.01*delta,2),inf,N,Nen)[0]
            alldataund1.append(a[0][-1])
            alldatapl1.append(a[1][-1])
            alldatami1.append(a[2][-1])
        alldataund.append(alldataund1)
        alldatapl.append(alldatapl1)
        alldatami.append(alldatami1)        
    return alldataund,alldatapl,alldatami

def collectdatafinalgroupsimulationformissingdeltasconvergence(inf=0.1,N=10000,Nen=20):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingfinalgroupsimulationformissingdeltas
    import numpy as np
    allconvers=[]
    interval=range(1,100)
    for P0 in interval:
        convers=[]
        for delta in range(1,10):
            a=loadingfinalgroupsimulationformissingdeltas(round(0.01*P0,2),round(0.01*delta,2),inf,N,Nen)[1]
            convers.append(a[-1])
        allconvers.append(convers)
   
    return allconvers


def collectdatafinalgroupsimulationrandp(infdown=100,infup=999,N=1000,Nen=20):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingfinalgroupsimulationrandp
    import numpy as np

    alldataund=[]
    alldatapl=[]
    alldatami=[]
    if infdown==0.0001:
        interval=range(60,100)
    else:
        interval=range(1,100)
    for P0 in interval:
        a=loadingfinalgroupsimulationrandp(round(0.01*P0,2),infdown,infup,N,Nen)
        alldataund.append(a[0])
        alldatapl.append(a[1])
        alldatami.append(a[2])
    return alldataund,alldatapl,alldatami    

def collectdatafinalgroupsimulationconvergence(inf=0.1,N=1000,Nen=20):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingfinalgroupsimulation
    import numpy as np

    steps=[]
    if inf==0.0001:
        interval=range(60,100)
    else:
        interval=range(1,100)
    for P0 in interval:
        a=loadingfinalgroupsimulation(round(0.01*P0,2),inf,N,Nen)[1]
        steps.append(a)
    return steps        
                        
                                                
def collectdatadistrpopx(N,alpha,kind=4):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingdistrpopx
    import numpy as np
    alldata=[]
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    interval=range(1,100)
    for P0 in interval:
        alldataund=[]
        alldatapl=[]
        alldatami=[]
        for delta in range(1,100):
            a=loadingdistrpopx('fix'+str(round(0.01*delta,2))+'delta',round(0.01*round(P0),2),'trio',kind,N,alpha)
            alldataund.append(a[0])
            alldatapl.append(a[1])
            alldatami.append(a[2])
        alldata.append((alldataund,alldatapl,alldatami))
    return alldata
    
    
def collectdatadistrpopmovida(N,alpha,kind='m1'):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingdistrpopmovida
    import numpy as np
    alldata=[]
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    interval=range(1,100)
    for P0 in interval:
        alldataund=[]
        alldatapl=[]
        alldatami=[]
        for delta in range(1,100):
            a=loadingdistrpopmovida('fix'+str(round(0.01*delta,2))+'delta',round(0.01*round(P0),2),'trio',kind,N,alpha)
            alldataund.append(a[0])
            alldatapl.append(a[1])
            alldatami.append(a[2])
        alldata.append((alldataund,alldatapl,alldatami))
    return alldata
    
    
def collectdatadistrpopskewed(N,alpha):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingdistrpopskewed
    import numpy as np
    alldata=[]
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    interval=range(1,100)
    for P0 in interval:
        alldataund=[]
        alldatapl=[]
        alldatami=[]
        for delta in range(1,100):
            a=loadingdistrpopskewed('fix'+str(round(0.01*delta,2))+'delta',round(0.01*round(P0),2),'trio',N,alpha)
            alldataund.append(a[0])
            alldatapl.append(a[1])
            alldatami.append(a[2])
        alldata.append((alldataund,alldatapl,alldatami))
    return alldata
    
    
def collectdatafortestingspecificdeltas(delta,poptype,alpha,N):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingforspecificdeltas
    import numpy as np
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    interval=range(1,100)
    kind='temp'
    for P0 in interval:
        a=loadingforspecificdeltas('fix'+str(delta)+'delta',round(0.01*round(P0),2),'trio',kind,delta,poptype,alpha,N)
        alldataund.append(a[0])
        alldatapl.append(a[1])
        alldatami.append(a[2])
            #Cada uno de estos va a ser una lista con los valores para cada delta. Esos valores, a su vez,
            #constituyen listas de los valores para indecisos y demás, sin promediar en ensambles.
        #Ahora que tengo todos los deltas guardados, junto los tres tipos en un tuple, y los guardo como un P0.
        #De esta manera, quedan con la misma estructura que salía de collectdata1.
    return alldataund,alldatapl,alldatami
    
    
def collectdatafortestingspecificdeltasmult(delta,poptype,alpha,N,mult):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingforspecificdeltasmult
    import numpy as np
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    interval=range(1,100)
    kind='temp'
    for P0 in interval:
        a=loadingforspecificdeltasmult('fix'+str(delta)+'delta',round(0.01*round(P0),2),'trio',kind,delta,poptype,alpha,N,mult)
        alldataund.append(a[0])
        alldatapl.append(a[1])
        alldatami.append(a[2])
            #Cada uno de estos va a ser una lista con los valores para cada delta. Esos valores, a su vez,
            #constituyen listas de los valores para indecisos y demás, sin promediar en ensambles.
        #Ahora que tengo todos los deltas guardados, junto los tres tipos en un tuple, y los guardo como un P0.
        #De esta manera, quedan con la misma estructura que salía de collectdata1.
    return alldataund,alldatapl,alldatami
    
def collectdatafortestingspecificdeltasmovida(delta,poptype,alpha,N,tipo):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingforspecificdeltastipo
    import numpy as np
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    interval=range(1,100)
    kind='temp'
    for P0 in interval:
        a=loadingforspecificdeltastipo('fix'+str(delta)+'delta',round(0.01*round(P0),2),'trio',kind,delta,poptype,alpha,N,tipo)
        alldataund.append(a[0])
        alldatapl.append(a[1])
        alldatami.append(a[2])
            #Cada uno de estos va a ser una lista con los valores para cada delta. Esos valores, a su vez,
            #constituyen listas de los valores para indecisos y demás, sin promediar en ensambles.
        #Ahora que tengo todos los deltas guardados, junto los tres tipos en un tuple, y los guardo como un P0.
        #De esta manera, quedan con la misma estructura que salía de collectdata1.
    return alldataund,alldatapl,alldatami
    
def collectdatafortestingspecificPrs(Pr):
    import os
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
    from loading import loadingforspecificPrs
    import numpy as np
    alldataund=[]
    alldatapl=[]
    alldatami=[]
    interval=range(1,100)
    kind='temp'
    for Ppl in interval:
        a=loadingforspecificPrs('fix'+str(Pr)+'PrandPplwithPpl',0.01*Ppl,'all',kind)
        alldataund.append(a[0])
        alldatapl.append(a[1])
        alldatami.append(a[2])
            #Cada uno de estos va a ser una lista con los valores para cada delta. Esos valores, a su vez,
            #constituyen listas de los valores para indecisos y demás, sin promediar en ensambles.
        #Ahora que tengo todos los deltas guardados, junto los tres tipos en un tuple, y los guardo como un P0.
        #De esta manera, quedan con la misma estructura que salía de collectdata1.
    return alldataund,alldatapl,alldatami
    
    
#        alldata.append((alldataund,alldatapl,alldatami))
#   return alldata