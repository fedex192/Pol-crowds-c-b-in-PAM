# -*- coding: utf-8 -*-
import os
#os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
#os.chdir('C:\\Users\\Fede\\Desktop\\Simulation_Functions\\') 
os.chdir('D:\\Doctorado\\Simulation_Functions\\') 

def argumentativepopulation(listofarguments,N=10,numofrelevargs=5,Ct=1.0, Cmax=3.0,old=''):
    '''listofarguments must have even length'''
    import random
    from Agent import Argumentativeagent
    popu=[]
    for agent in range(N):
        #creo listas con todos los argumentos existentes, positivos y negativos. Los ordeno aleatoriamente.
        pros=range(len(listofarguments)/2)
        cons=range(len(listofarguments)/2, len(listofarguments))
        random.shuffle(pros)
        random.shuffle(cons)
        relevancevector=[0 for i in range(len(listofarguments))]
        
        #Elijo un número inicial de argumentos aleatorio para este agente.
        initialargs=numofrelevargs
        while initialargs==numofrelevargs+1:
            initialargs=random.randrange(0,numofrelevargs+1) #podría pedir más, pero igual la persuasión depende sólo de 5, así que da igual.
        
        #Elijo un número inicial de argumentos positivos aleatorio para este agente.
        posargs=random.randrange(0,initialargs+1)
        while posargs==initialargs+1:
            posargs=random.randrange(0,initialargs+1)
         
        #Por la regla de los argumentos iguales, tengo que revisar que los que voy a agregar no vienen con su counter.
        allargs=len(relevancevector)
        tobeusedcons=[]
        if posargs!=0:
            tobeusedpros=pros[-posargs:] #tomo los pro que voy a usar.
        else:
            tobeusedpros=[]
        i=initialargs-posargs
        
        if old=='True':
            while i>0 and cons!=[]:
                if (cons[-1]-allargs/2) not in tobeusedpros:
                    tobeusedcons.append(cons[-1])
                    cons.pop()
                    i-=1
                else:
                    cons.pop()
        else:
            if i!=0:
                tobeusedcons=cons[-i:] #tomo los pro que voy a usar.

        
 #probé con posargs=0. Probar con posargs=initialargs y con el caso mixto.           
        
                  
        proused=[]
        consused=[]
        
        #Asigno posargs argumentos positivos para el agente.
        for i in range(len(tobeusedpros)):
            relevancevector[tobeusedpros[-1]]=1
            proused.append(tobeusedpros.pop())
        #Asigno los restantes argumentos negativos para el agente.
        for i in range(len(tobeusedcons)):            
            relevancevector[tobeusedcons[-1]]=1
            consused.append(tobeusedcons.pop())
            
        positiveindexes=sorted(proused)
        negativeindexes=sorted(consused)
                
        #Ahora calculo la persuasión en función de estos argumentos
        newpersuasion=0
        
        for i in range(initialargs):
            #Si tengo argumentos positivos y negativos, me fijo el más fuerte entre ambos grupos, y agrego ese.
                if len(positiveindexes)!=0 and len(negativeindexes)!=0:
                    if positiveindexes[-1]>negativeindexes[-1]-(allargs/2.0): #En el caso de 60 args, el 59 es como el 29 en índices. O sea, -30.
                        newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                        positiveindexes.pop()
                    elif positiveindexes[-1]<negativeindexes[-1]-(allargs/2.0):           
                        newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                        negativeindexes.pop()
                    elif positiveindexes[-1]==negativeindexes[-1]-(allargs/2.0): #agregué este elif al sacar lo de aniquilación
                        used=random.choice([positiveindexes[-1],negativeindexes[-1]])
                        newpersuasion+=listofarguments[used].getvalence()*listofarguments[used].getimpact()/float(allargs/2.0)
                        if used==positiveindexes[-1]:
                            positiveindexes.pop()
                        else:
                            negativeindexes.pop()
                    else:
                        print 'whyyyy?'
            #Si sólo tengo argumentos negativos, de una los agrego.
                elif len(positiveindexes)==0 and len(negativeindexes)!=0:
                    newpersuasion+=listofarguments[negativeindexes[-1]].getvalence()*listofarguments[negativeindexes[-1]].getimpact()/float(allargs/2.0)
                    negativeindexes.pop()
            #Si sólo tengo argumentos positivos, de una los agrego.
                elif len(negativeindexes)==0 and len(positiveindexes)!=0:
                        newpersuasion+=listofarguments[positiveindexes[-1]].getvalence()*listofarguments[positiveindexes[-1]].getimpact()/float(allargs/2.0)
                        positiveindexes.pop()
                else:
                    pass
                    #print 'this can not be right'
                    #return 'this can not be right'
      
        #Ahora, calculo la opinión.          
        if Ct<=newpersuasion:
            opinion=1
        elif -(Ct)>=newpersuasion:
            opinion=-1
        else: 
            opinion=0    
        
        #Por último, reviso que la persuasión no sea mayor a Cmax o -Cmax.
        if newpersuasion>Cmax:
            newpersuasion=Cmax
        elif newpersuasion<-Cmax:
            newpersuasion=-Cmax
        
        
        popu.append(Argumentativeagent(2, relevancevector, 0, newpersuasion, numofrelevargs, opinion, Ct))
    
    return popu   

def newrunargsim(allargs=60,rangeofimpacts=30,N=10,numofrelevargs=5,steps=6000,cb='yes',plotting='',homo=0,Ct=1.0, Cmax=3.0,intertype='Bid'):
    from createlistofarguments import createlistofarguments
    from newinteraction import newargumentativeinteraction
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
    if N<50:
        breakcount=6000
    elif N>=50 and N<80:
        breakcount=500
    else:
        breakcount=6000
        
    for i in range(steps):
        subpersuasions=getagentspersuasion(popu)  
        for j in range(len(popu)):
            persuasions[j]+=subpersuasions[j]          
        b=newargumentativeinteraction(popu, listofarguments, Cmax, intertype, cb,'bidirectional',homo)
        #b=argumentativeinteraction(popu, listofarguments, Cmax, intertype, cb,'no')
        if b!=None:
            print b
            #break
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
            #print('oopsi')
            break
    if i>9000:
        #print 'osc'
        flag=1
    else:
        flag=0    
    
    subpersuasions=getagentspersuasion(popu)  
    for j in range(len(popu)):
        persuasions[j]+=subpersuasions[j]        
                        
    if plotting=='yes':    
        arguments=[[] for i in range(len(popu))]
        for j in range(len(popu)):
            for i in range(len(popu[j].relevancevector)):
                if popu[j].relevancevector[i]==1:
                    #print i
                    arguments[j].append(i)
        #if a[0]!=0 and a[0]!=10:
        #makingargumenthistograms(arguments,allargs) 
        plottingopinions(a)       
        #plottingpersuasions(persuasions)
        #return 0

    return countsund, countspro, countsagainst,flag#,persuasions#, arguments, persuasions
    
def plottingopinions(a,N):           
                
        countsund=a[0]
        countspro=a[1]
        countsagainst=a[2]                                                        
                                                                                                                                        
        import pylab as py
        py.figure()    
        trueN=N*100.0
        py.plot(py.array(countsund)/trueN,alpha=1.0,color='k')
        py.plot(py.array(countspro)/trueN,alpha=1.0,color='r')
        py.plot(py.array(countsagainst)/trueN,alpha=1.0,color='b')
        py.ylim([-0.05,1.05])
        py.legend(['Moderate O=0','Oriented O=+1','Oriented O=-1'])
        #py.title('Opiniones')
        py.ylabel('Proportion of Agents with O')
        py.xlabel('Temporal Steps')
        py.xlim([0,1001])
        py.savefig('D:\\Doctorado\\Paper Argumentos\\Review\\'+'PROBANDOopinionesindecisozona2.svg', bbox_inches='tight') 
        

def plottingopinionswitherrors(a,N,tipo):           
        import pylab as py 
        import numpy as np
             
        countsund=a[0]
        countspro=a[1]
        countsagainst=a[2] 
        #Calculando los errores:
        
        copias0=np.array(np.transpose(a[3]))
        copiaspos=np.array(np.transpose(a[4]))
        copiasneg=np.array(np.transpose(a[5]))
        
        serrors0=[]
        serrorspos=[]
        serrorsneg=[]
                
        for i in range(len(copias0)):
            serrors0.append(np.std(copias0[i])/float(np.sqrt(100))/float(N))
            serrorspos.append(np.std(copiaspos[i])/float(np.sqrt(100))/float(N))
            serrorsneg.append(np.std(copiasneg[i])/float(np.sqrt(100))/float(N))

        
        py.figure()    
        trueN=N*100.0
        py.plot(py.array(countsund)/trueN,alpha=1.0,color='k')
        py.fill_between(range(len(py.array(countsund)/trueN)),py.array(countsund)/trueN-serrors0, py.array(countsund)/trueN+serrors0,alpha=0.5,facecolor='k')
        if N==10:
            py.xlim([0,101])
        else:
            py.xlim([0,1001])
        py.plot(py.array(countspro)/trueN,alpha=1.0,color='r')
        py.fill_between(range(len(py.array(countspro)/trueN)),py.array(countspro)/trueN-serrorspos, py.array(countspro)/trueN+serrorspos,alpha=0.5,facecolor='r')
        py.plot(py.array(countsagainst)/trueN,alpha=1.0,color='b')
        py.fill_between(range(len(py.array(countsagainst)/trueN)),py.array(countsagainst)/trueN-serrorsneg, py.array(countsagainst)/trueN+serrorsneg,alpha=0.5,facecolor='b')        
        py.ylim([-0.05,1.05])
        #py.legend(['Moderate O=0','Oriented O=+1','Oriented O=-1'])
        #py.title('Opiniones')
        #py.ylabel('Proportion of Agents with O')
        #py.xlabel('Temporal Steps')
        if tipo=='consenso1':
            py.savefig('D:\\Doctorado\\Paper Argumentos\\Review\\'+'PROBANDOCONERRORopinionesconsenso1.svg', bbox_inches='tight')
        elif tipo=='consenso2':
            py.savefig('D:\\Doctorado\\Paper Argumentos\\Review\\'+'PROBANDOCONERRORopinionesconsenso2.svg', bbox_inches='tight')            
        else:
            py.savefig('D:\\Doctorado\\Paper Argumentos\\Review\\'+'PROBANDOCONERRORopinionesindecisozona2.svg', bbox_inches='tight')
            
        

def gettingopinionsevolutions(N=10,which=1):        
                        
        import numpy as np
        countsund=np.array([0 for i in range(6001)])
        countspro=np.array([0 for i in range(6001)])
        countsagainst=np.array([0 for i in range(6001)])
        newcountsund=[]
        newcountspro=[]
        newcountsagainst=[]
        i=0
        while i<100:
            a=newrunargsim(60,30,N,6,6000,'no','no',0,1.0,3.0,'Bid')
            if a[which][-1]==N:
                
                countsund+=np.array(a[0])
                countspro+=np.array(a[1])
                countsagainst+=np.array(a[2])  
                newcountsund.append(np.array(a[0]))
                newcountspro.append(np.array(a[1]))
                newcountsagainst.append(np.array(a[2]))
                i+=1       
        
        import pylab as py
        py.figure()    
        trueN=N*100.0
        py.plot(py.array(countsund)/trueN,alpha=1.0,color='k')
        py.plot(py.array(countspro)/trueN,alpha=1.0,color='r')
        py.plot(py.array(countsagainst)/trueN,alpha=1.0,color='b')
        py.ylim([-0.05,1.05])
        py.legend(['Moderate O=0','Oriented O=+1','Oriented O=-1'])
        #py.title('Opiniones')
        py.ylabel('Proportion of Agents with O')
        py.xlabel('Temporal Steps')
        if N==10:
            py.xlim([0,101])
        else:
            py.xlim([0,1001])
        
        return countsund,countspro,countsagainst,newcountsund,newcountspro,newcountsagainst






def checkingargumentsevolution(allargs=60,rangeofimpacts=30,N=10,numofrelevargs=5,steps=10000,cb='yes',Ct=1.0, Cmax=3.0,intertype='Bid'):
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

#A[-2][0][10] (A[-2] te da los argumentos. Primero tenés los pasos temporales; adentro, los 10 agentes; adentro los argumentos).
def restructuringargumentvalues(b,k):
    for i in range(len(b[k])):
        for j in range(len(b[k][i])):
            if b[k][i][j]<30:
                b[k][i][j]+=1
            elif b[k][i][j]>=30:
                b[k][i][j]-=29
                b[k][i][j]=-b[k][i][j]
    return b[k]


def plottingargumentsnew(tipo=5,cb='no',Ars=60,N=10,rel=6,l=0,bins=5,chosen='indeciso'):    
    import pylab as py
    if tipo!=4:
        c=checkingargumentsevolution(Ars,Ars/2,N,rel,2000,cb)
        b=c[-2]
    #plottingopinions(c[0],c[1],c[2])       
    #plottingpersuasions(c[-1])
    if tipo==5:
        import numpy as np
        count=0
        evolutions=[]
        while count<100:
            c=checkingargumentsevolution(Ars,Ars/2,N,rel,2000,cb)
            b=c[-2]
            opinions=[]
            for i in range(N):
                if c[-1][i][-1]<-1:
                    opinions.append(-1)
                elif c[-1][i][-1]>1:
                    opinions.append(1)
                else:
                    opinions.append(0)
            if opinions==[1 for i in range(N)]:
                chosentype='consenso1'
            elif opinions==[-1 for i in range(N)]:
                chosentype='consenso2'
            elif opinions==[0 for i in range(N)]:
                chosentype='indeciso'
            elif 0 not in opinions:
                chosentype=u'bip'
            else:
                chosentype=u'otros'

            if chosen==chosentype:
                argumentbins=[]
                for k in range(len(b)):
                    b[k]=restructuringargumentvalues(b,k)
                    systemargs=b[k][0]
                    for i in range(1,N):
                        systemargs+=b[k][i]                
                    a=np.histogram(systemargs,np.arange(-Ars/2,Ars/2+2,bins))
                    
                    argumentbins.append(list(a[0]))
                evolutions.append(argumentbins)
                count+=1
        return evolutions    