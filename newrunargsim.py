# -*- coding: utf-8 -*-
import os
#os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
#os.chdir('C:\\Users\\Fede\\Desktop\\Simulation_Functions\\') 
os.chdir('D:\\Doctorado\\Simulation_Functions\\') 

def newrunargsim(allargs=60,rangeofimpacts=30,N=10,numofrelevargs=5,steps=6000,cb='yes',plotting='',homo=0,Ct=1.0, Cmax=3.0,intertype='Bid'):
    from population import argumentativepopulation
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
    
def plottingopinions(a):           
                
        countsund=a[0]
        countspro=a[1]
        countsagainst=a[2]                                                        
                                                                                                                                        
        import pylab as py
        py.figure()    
        N=100.0*100
        py.plot(py.array(countsund)/N,alpha=1.0,color='k')
        py.plot(py.array(countspro)/N,alpha=1.0,color='r')
        py.plot(py.array(countsagainst)/N,alpha=1.0,color='b')
        py.ylim([-0.05,1.05])
        py.legend(['Moderate O=0','Oriented O=+1','Oriented O=-1'])
        #py.title('Opiniones')
        py.ylabel('Proportion of Agents with O')
        py.xlabel('Temporal Steps')
        py.xlim([0,1105])
        py.savefig('D:\\Doctorado\\Paper Argumentos\\Review\\'+'opinionesmoderadozona2g2.svg', bbox_inches='tight') 
        

def gettingopinionsevolutions(N=10):        
                        
        import numpy as np
        countsund=np.array([0 for i in range(6001)])
        countspro=np.array([0 for i in range(6001)])
        countsagainst=np.array([0 for i in range(6001)])
        i=0
        while i<100:
            a=newrunargsim(60,30,N,6,6000,'no','no',0,1.0,3.0,'Bid')
            if a[0][-1]==N:
                
                countsund+=np.array(a[0])
                countspro+=np.array(a[1])
                countsagainst+=np.array(a[2])  
                i+=1       
        
        return countsund,countspro,countsagainst
        
        
def explorargsimforrelandN(relini=5,relfin=56,allargs=60,numens=1000,cb='no',opsys='w'):
    from saving import savingargumentsimulation2
    for rel in range(relini,relfin,5):
        print rel
        for N in range(10,111,5):
            #print N
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
                a=runargsim(allargs,allargs/2,N,rel,10000,cb,'no')
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
            savingargumentsimulation2((counts0,countspl,countsmin,countsbip,otherstuff,osc,ensamblestates),rel,N,numens,opsys)#finalresult,allargs,N,numens,opsys)

def explorargsimforrelandN2(relini=5,relfin=56,allargs=60,numens=1000,cb='no',opsys='w'):
    from saving import savingargumentsimulation2
    for rel in range(relini,relfin,5):
        print rel
        for N in range(10,111,5):
            #print N
            counts0,countspl,countsmin,countsbip,otherstuff,osc=checkingfinalstates(numens,N,allargs,10000,cb,rel)
                #result.append(a)
            #finalresult.append((counts0,countspl,countsmin,countsbip,otherstuff))#,result))
            savingargumentsimulation2((counts0,countspl,countsmin,countsbip,otherstuff,osc),rel,N,numens,opsys)#finalresult,allargs,N,numens,opsys)




def explorargsimforrelandArs(relini=5,relfin=56,N=60,numens=1000,cb='no',opsys='w'):
    from saving import savingargumentsimulation3
    for rel in range(relini,relfin,5):
        print rel
        for Ars in range(10,113,6):
            #print Ars
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
                a=runargsim(Ars,Ars/2,N,rel,10000,cb,'no')
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
            savingargumentsimulation3((counts0,countspl,countsmin,countsbip,otherstuff,osc,ensamblestates),rel,Ars,numens,opsys)#finalresult,allargs,N,numens,opsys)
        
        
def newrunargsimforprofiling(allargs=60,rangeofimpacts=30,N=10,numofrelevargs=5,steps=10000,cb='yes',plotting='',homo=0,Ct=1.0, Cmax=3.0,intertype='Bid'):
    from population2 import argumentativepopulation
    from createlistofarguments2 import createlistofarguments
    from newinteraction2 import newargumentativeinteraction
    from getundecidedcounts2 import getundecidedcounts
    from getagentspersuasion2 import getagentspersuasion
    from checkconvergence2 import checkconvergence
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
    # 
    # if N<50:
    #     breakcount=300
    # elif N>=50 and N<80:
    #     breakcount=500
    # else:
    #     breakcount=1500
        
    # for i in range(steps):
    flag=0        
    while not checkconvergence(popu,cb):
        stepcount+=1        
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
        if stepcount>10000:
            flag=1
            break
    # tempcount=0
    #     if i!=0:
    #         for persuasion in range(len(persuasions)):
    #             if persuasions[persuasion][-1]==persuasions[persuasion][-2]:
    #                 tempcount+=1
    #         if tempcount==N:
    #             stepcount+=1
    #         else:
    #             stepcount=0
    #     if stepcount==breakcount:
    #         #print('oopsi')
    #         break
    # if i>9000:
    #     #print 'osc'
    #     flag=1
    # else:
    #     flag=0    
    
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
        plottingopinions(countsund,countspro,countsagainst)       
        #plottingpersuasions(persuasions)
        return 0

    return countsund, countspro, countsagainst,flag,stepcount#,flag#,persuasions#, arguments, persuasions
#     

#h=0, sin cb: N=20>Nars=10: 50.4300000667572

def checkingargumentsevolution(allargs=60,rangeofimpacts=30,N=10,numofrelevargs=5,steps=10000,cb='yes',Ct=1.0, Cmax=3.0,intertype='Bid'):
    from population import argumentativepopulation
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


def plottingarguments(tipo=1,cb='yes',Ars=60,N=10,rel=5,l=0,bins=5,chosen='indeciso'):    
    import pylab as py
    if tipo!=4:
        c=checkingargumentsevolution(Ars,Ars/2,N,rel,2000,cb)
        b=c[-2]
    #plottingopinions(c[0],c[1],c[2])       
    #plottingpersuasions(c[-1])
    if tipo==1:
        for k in range(len(b)):
            b[k]=restructuringargumentvalues(b,k)
            py.figure()                
            for i in range(10):
                if c[-1][i][-1]<-1:
                    py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'b-.')
                elif c[-1][i][-1]>1:
                    py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'r-.')
                else:
                    py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'k-.')
            for i in range(10):
                if c[-1][i][-1]<-1:
                    py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'bD')
                elif c[-1][i][-1]>1: 
                    py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'rs')
                else:
                    py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'ko')
            ax=py.gca()
            #py.xlim([1,61])
            py.xlim([-31,31])
            #py.xticks(list(py.arange(1,66,5)))
            py.xticks(list(py.arange(-30,0,5))+[-1]+[1]+list(py.arange(5,31,5)),size=18)
            py.xlabel('Peso del Argumento',size=18)
            py.ylabel('Agentes',size=18)            
            #py.xlim([61,-1])
            py.grid('on')
            ##########a=list(py.arange(-30,31,5))
            #negs=list(-1*py.arange(1,32,5))        
            ##########negs.reverse()
            #pos=list(py.arange(1,30,5))
            pos=list(py.arange(5,31,5))
            negs=list(py.arange(-30,0,5))
            ax.xaxis.set_ticklabels(negs+[-1]+[1]+pos)       
                 
            py.yticks(range(1,11),size=18)
            py.title(u'Argumentos de los 10 Agentes - Paso Temporal '+str(k),size=18)
        
            if k<10:   
                py.savefig(u'Argumentos de los 10 Agentes - Paso Temporal 00'+str(k)+'.png', bbox_inches='tight')
            elif k>=10 and k<100:
                py.savefig(u'Argumentos de los 10 Agentes - Paso Temporal 0'+str(k)+'.png', bbox_inches='tight')  
            else:
                py.savefig(u'Argumentos de los 10 Agentes - Paso Temporal '+str(k)+'.png', bbox_inches='tight')            
            py.close('all')
        return c    
    elif tipo==2:
        #k=0
        #b[k]=restructuringargumentvalues(b,k)
        #py.figure()
        #for i in range(10):
        #    if c[-1][i][-1]<-1:
        #        py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'b-.')
        #    elif c[-1][i][-1]>1:
        #        py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'r-.')
        #    else:
        #        py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'k-.')
        #for i in range(10):
        #    if c[-1][i][-1]<-1:
        #        py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'bo')
        #    elif c[-1][i][-1]>1: 
        #        py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'ro')
        #    else:
        #        py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'ko')
        #ax=py.gca()
        ##py.xlim([1,61])
        #py.xlim([-31,31])
        ##py.xticks(list(py.arange(1,66,5)))
        #py.xticks(list(py.arange(-30,0,5))+[-1]+[1]+list(py.arange(5,31,5)),size=18)
        #
        ##py.xlim([61,-1])
        #py.grid('on')
        ###########a=list(py.arange(-30,31,5))
        ##negs=list(-1*py.arange(1,32,5))        
        ###########negs.reverse()
        ##pos=list(py.arange(1,30,5))
        #pos=list(py.arange(5,31,5))
        #negs=list(py.arange(-30,0,5))
        #ax.xaxis.set_ticklabels(negs+['-1 ']+[' 1']+pos)
        #
        #py.yticks(range(1,11),size=18)
        #py.title(u'Argumentos - 10 Agentes, '+str(k)+', CB='+cb,size=18)
        #py.xlabel('Peso del Argumento',size=18)
        #py.ylabel('Agentes',size=18)
        #
        #if k<10:   
        #    py.savefig(u'Argumentos Iniciales de los 10 Agentes - Paso Temporal 00'+str(k)+'- CB='+cb+'.png', bbox_inches='tight')
        #elif k>=10 and k<100:
        #    py.savefig(u'Argumentos Iniciales de los 10 Agentes - Paso Temporal 0'+str(k)+'- CB='+cb+'.png', bbox_inches='tight')  
        #else:
        #    py.savefig(u'Argumentos Iniciales de los 10 Agentes - Paso Temporal '+str(k)+'- CB='+cb+'.png', bbox_inches='tight') 


        k=len(b)-1
        b[k]=restructuringargumentvalues(b,k)
        opinions=[]
        for i in range(N):
            if c[-1][i][-1]<-1:
                opinions.append(-1)
            elif c[-1][i][-1]>1:
                opinions.append(1)
            else:
                opinions.append(0)
        if opinions==[0 for i in range(N)]:
            return 0
                    
                
        py.figure()
        for i in range(10):
            if c[-1][i][-1]<-1:
                py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'b-.')
            elif c[-1][i][-1]>1:
                py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'r-.')
            else:
                py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'k-.')
        for i in range(10):
            if c[-1][i][-1]<-1:
                py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'bD')
            elif c[-1][i][-1]>1: 
                py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'r^')
            else:
                py.plot(b[k][i],[i+1 for j in range(len(b[k][i]))],'ko')
        ax=py.gca()
        #py.xlim([1,61])
        py.xlim([-31,31])
        #py.xticks(list(py.arange(1,66,5)))
        py.xticks(list(py.arange(-30,0,5))+[-1]+[1]+list(py.arange(5,31,5)),size=18)
        
        #py.xlim([61,-1])
        py.grid('on')
        ##########a=list(py.arange(-30,31,5))
        #negs=list(-1*py.arange(1,32,5))        
        ##########negs.reverse()
        #pos=list(py.arange(1,30,5))
        pos=list(py.arange(5,31,5))
        negs=list(py.arange(-30,0,5))
        ax.xaxis.set_ticklabels(negs+['-1 ']+[' 1']+pos)
        
        py.yticks(range(1,11),size=18)
        py.title(u'Argumentos - 10 Agentes, '+str(k)+', CB='+cb,size=18)
        py.xlabel('Peso del Argumento',size=18)
        py.ylabel('Agentes',size=18)
        
        if k<10:   
            py.savefig(u'Argumentos Finales de los 100 Agentes - Paso Temporal 00'+str(l)+'- CB='+cb+'.png', bbox_inches='tight')
        elif k>=10 and k<100:
            py.savefig(u'Argumentos Finales de los 100 Agentes - Paso Temporal 0'+str(l)+'- CB='+cb+'.png', bbox_inches='tight')  
        else:
            py.savefig(u'Argumentos Finales de los 100 Agentes - Paso Temporal '+str(l)+'- CB='+cb+'.png', bbox_inches='tight') 
    elif tipo==3:
        import numpy as np
        argumentbins=[]
        for k in range(len(b)):
            b[k]=restructuringargumentvalues(b,k)
            systemargs=b[k][0]
            for i in range(1,N):
                systemargs+=b[k][i]                
            a=np.histogram(systemargs,np.arange(-Ars/2,Ars/2+2,bins))
            
            argumentbins.append(a[0])
            
        B=np.transpose(argumentbins)
        py.figure()  
        py.imshow(B,cmap='gray_r',aspect='auto',vmax=N)
        py.ylabel(u'Argumentos',size=18)
        py.xlabel(u'Pasos Temporales',size=18)
        py.ylim([-0.25,(Ars/bins)+0.5])
        py.xticks(size=18)
        length=len(np.arange(-Ars,Ars+1,5))
        length=np.linspace(-0.25,(Ars/bins)+0.5,Ars/5+1)
        py.yticks(length,size=18)
        ax=py.gca()
        ax.yaxis.set_ticklabels(np.arange(-Ars/2,Ars/2+1,5))
        py.xlim([0,1000])
        C=py.colorbar()    
        for m in C.ax.yaxis.get_ticklabels():
            m.set_size(18)
        
        opinions=[]
        for i in range(N):
            if c[-1][i][-1]<-1:
                opinions.append(-1)
            elif c[-1][i][-1]>1:
                opinions.append(1)
            else:
                opinions.append(0)
        if opinions==[1 for i in range(N)]:
            chosentype='Consenso Orientado'
        elif opinions==[-1 for i in range(N)]:
            chosentype='Consenso Orientado'
        elif opinions==[0 for i in range(N)]:
            chosentype='Consenso Moderado'
        elif 0 not in opinions:
            chosentype=u'Bipolarización'
        else:
            chosentype=u'Bipolarización Total'

        py.title('Sistema Converge a '+chosentype,size=18)                  
        py.savefig(u'Argumentos Finales de los Agentes, Caso - '+str(l)+'- CB='+cb+'End - '+chosentype+'.png', bbox_inches='tight') 
    elif tipo==4:
        import numpy as np
        argumentbins=[]
        count=0
        a=[]
        while count<100:
            c=checkingargumentsevolution(Ars,Ars/2,N,rel,10000,cb)
            b=c[-2]
            k=len(b)-1
            b[k]=restructuringargumentvalues(b,k)
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
                systemargs=[]
                for i in range(len(b[k])):
                    systemargs+=b[k][i]            
                
                a+=systemargs
                count+=1  
                          
        return a    
    elif tipo==5:
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
