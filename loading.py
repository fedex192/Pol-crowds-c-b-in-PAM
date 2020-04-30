# -*- coding: utf-8 -*-
def loadingmasargumentvariables(specifications='ThirdRun',folder='MasSimulation',N=100):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\'+folder+str(N))
    f = open(specifications+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var

def loadingargumentvariables(allargs,N,numens=1000,cb='no'):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    if cb=='no':
        os.chdir('D:\\Doctorado\\Simulation_Functions\\Barrido Anterior\\FullExplorationRel6-'+str(numens)+'\\')
    else:
        os.chdir('D:\\Doctorado\\Simulation_Functions\\Barrido Anterior\\FullExplorationRel6ConCB-'+str(numens)+'\\')
            
    f = open('allargs'+str(allargs)+', N='+str(N)+', Ens='+str(numens)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingargumentvariablesrel(rel,N,numens=1000,folder='FullExploration'):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsRel\\'+folder+str(numens))
    f = open('rel'+str(rel)+', N='+str(N)+', Ens='+str(numens)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingargumentvariablesrelars(rel,Ars,numens=1000,folder='FullExploration'):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsRelArs\\'+folder+str(numens))
    f = open('rel'+str(rel)+', Ars='+str(Ars)+', Ens='+str(numens)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingargumentvariables2(allargs,N,numens=1000,folder='P0.5'):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSims'+folder+'\\'+'FullExploration'+str(numens))
    f = open('allargs'+str(allargs)+', N='+str(N)+', Ens='+str(numens)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var

def loadinggeneric(specifications='a',path='D:\\Doctorado\\Simulation_Functions\\'):
    import pickle, os
    A=os.getcwd()
    os.chdir(path)
    f = open(specifications+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var


def loadingexplorations(N):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+'populations'+str(N))
    f = open('simP0'+'all'+'andDelta'+'all'+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingexplorationsforphasediagram(N):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    if N==11:
            os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\populationscompleterandom11\\Corrida Completa')
    else:
            os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+'populationsforpd'+str(N))

    f = open('simP0'+'all'+'andDelta'+'all'+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loading(name,trial,i,kind,N=0):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    if kind=='full':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Simulaci\xf3n Preliminar\\Variables Guardadas')
        f = open(name+str(trial)+str(i)+'.pckl', 'rb')
    elif kind=='temp':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\SavedVariablesSize'+str(N)+'Ens100')
        f = open(name+str(trial)+str(i)+'.pckl', 'rb') 
    elif kind=='temp2':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\SavedVariablesSize'+str(N)+'Ens100-2')
        f = open(name+str(trial)+str(i)+'.pckl', 'rb') 
    elif kind=='temp3':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Simulaci\xf3n Preliminar\\Variables Guardadas\\Diagrama de Fases')
        f = open(name+str(trial)+str(i)+'unsync.pckl', 'rb') 
    elif kind=='temp4':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\SavedVariablesSize'+str(N)+'Ens20')
        f = open(name+str(trial)+str(i)+'.pckl', 'rb')
    elif kind=='temp5':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\SavedVariablesSize'+str(10)+'withppl')
        f = open(name+str(trial)+str(i)+'.pckl', 'rb')        
    elif kind=='ten':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\SavedVariablesSize'+str(N)+'Ens1000') 
        f = open(name+str(trial)+str(i)+'.pckl', 'rb')
        
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingexplorationsallforone(N):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+'populationsallforone'+str(N))
    f = open('simP0'+'all'+'andDelta'+'all'+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
       
def loadingpartsandsavingone(N,parts):
    import os, pickle
    from saving import saving
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+'populationscompleterandom'+str(N))
    #os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+'populationsallforoneallatoncerandomorder10')
    f = open('simP0'+str(parts[0])+'andDelta'+str(parts[1])+'.pckl', 'rb')
    var1 = pickle.load(f)
    f.close()
    f = open('simP0'+str(parts[1])+'andDelta'+str(parts[2])+'.pckl', 'rb')
    var2 = pickle.load(f)
    f.close()
    f = open('simP0'+str(parts[2])+'andDelta'+str(parts[3])+'.pckl', 'rb')
    var3 = pickle.load(f)
    f.close()
    f = open('simP0'+str(parts[3])+'andDelta'+str(parts[4])+'.pckl', 'rb')
    var4 = pickle.load(f)
    f.close()
    saving(var1+var2+var3+var4,'all','all','populationscompleterandom',N,'w') 
    os.chdir(A)

#loadingpartsandsavingone(10,[0,1,4,7,10])
        
def loadingexplorationscompleterandom(N):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+'populationscompleterandom'+str(N)+'\\Corrida Completa')
    f = open('simP0'+'all'+'andDelta'+'all'+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingexplorationsforphasediagramcompleterandom(N):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+'populationscompleterandom'+str(N)+'\\Corrida Completa')
    f = open('simP0'+'all'+'andDelta'+'all'+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var

def loadingexplorationsforsingleinteraction(N,newCtini,newCtfin):
    import pickle, os    
    A=os.getcwd()
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Avances de la Tesis\\Segunda Parte\\Explorando Persuasion Inter de a Pares\\'+'N='+str(N))
    f = open('newCtini - '+str(newCtini)+' - newCtfin - '+str(newCtfin)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var

def loadingexplorationsforsingleinteractionsameinits(N,newCtini,newCtfin):
    import pickle, os    
    A=os.getcwd()
    os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Avances de la Tesis\\Segunda Parte\\Explorando Persuasion Inter de a Pares\\Same Initial Conditions\\'+'N='+str(N))
    f = open('newCtini - '+str(newCtini)+' - newCtfin - '+str(newCtfin)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var    
            
def generalloadingpartsandsavingone(N,parts,folder='populationsallforoneallatoncerandomorder'):
    import os, pickle
    from saving import saving
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N))
    var=[]
    for part in range(len(parts)-1):
        f = open('simP0'+str(parts[part])+'andDelta'+str(parts[part+1])+'.pckl', 'rb')
        var+=pickle.load(f)
        f.close()
    saving(var,'all','all',folder,N,'w') 
    os.chdir(A)
    return var

def loadingexplorationsallatonceallforonerandomorder(N):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+'populationsallforoneallatoncerandomorder'+str(N))
    f = open('simP0'+'all'+'andDelta'+'all'+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var

   
def loadingoneforall(P0,delta,N=100,folder='Int Grupal - Grupos Variables - N=',specifications=''):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+specifications)
    f = open('simP0'+str(P0)+'andDelta'+str(delta)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var

def loadingpair(P0,delta,N=100,folder='Int Pares - Grupos Variables - N=',specifications=''):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+specifications)
    f = open('simP0'+str(P0)+'andDelta'+str(delta)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var    
    
  
    
def loadingexplorationsallforonecompleterandom(N):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+'populationsallforonecompleterandom'+str(N))
    f = open('simP0'+'all'+'andDelta'+'all'+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
    
def loadingpartsandsavingoneforoneforall(N=100,parts=[0,10,20,30,40,50,60,80,99]):
    import os, pickle
    from saving import saving
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+'populationscompleterandom'+str(N))
    #os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+'populationsallforoneallatoncerandomorder10')
    f = open('simP0'+str(parts[0])+'andDelta'+str(parts[1])+'.pckl', 'rb')
    var1 = pickle.load(f)
    f.close()
    f = open('simP0'+str(parts[1])+'andDelta'+str(parts[2])+'.pckl', 'rb')
    var2 = pickle.load(f)
    f.close()
    f = open('simP0'+str(parts[2])+'andDelta'+str(parts[3])+'.pckl', 'rb')
    var3 = pickle.load(f)
    f.close()
    f = open('simP0'+str(parts[3])+'andDelta'+str(parts[4])+'.pckl', 'rb')
    var4 = pickle.load(f)
    
    f = open('simP0'+str(parts[4])+'andDelta'+str(parts[5])+'.pckl', 'rb')
    var5 = pickle.load(f)
    f.close()
    f = open('simP0'+str(parts[5])+'andDelta'+str(parts[6])+'.pckl', 'rb')
    var6 = pickle.load(f)
    f.close()
    f = open('simP0'+str(parts[6])+'andDelta'+str(parts[7])+'.pckl', 'rb')
    var7 = pickle.load(f)
    f.close()
    f = open('simP0'+str(parts[7])+'andDelta'+str(parts[8])+'.pckl', 'rb')
    var8 = pickle.load(f)
    f.close()
    saving(var1+var2+var3+var4+var5+var6+var7+var8,'all','all','populationscompleterandom',N,'w') 
    os.chdir(A)
    
    
def loadingdistrpop(name,trial,i,kind,N=1000,alpha=0.1):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    if kind=='normal':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\distrpop\\SavedVariablesSize'+str(N)+'Ens100'+'Alpha'+str(alpha))
        f = open(name+str(trial)+str(i)+'.pckl', 'rb')
    elif kind=='corrida':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\distrpopcorrida\\SavedVariablesSize'+str(N)+'Ens100'+'Alpha'+str(alpha))
        f = open(name+str(trial)+str(i)+'.pckl', 'rb')        
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingdistrpopx(name,trial,i,kind,N=1000,alpha=0.1):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\distrpopx'+str(kind)+'\\SavedVariablesSize'+str(N)+'Ens100'+'Alpha'+str(alpha))
    f = open(name+str(trial)+str(i)+'.pckl', 'rb')        
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingdistrpopmovida(name,trial,i,kind,N=1000,alpha=0.1):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\distrpopmovida'+str(kind)+'\\SavedVariablesSize'+str(N)+'Ens100'+'Alpha'+str(alpha))
    f = open(name+str(trial)+str(i)+'.pckl', 'rb')        
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingfinalgroupsimulation(P0,inf=0.1,N=1000,Nen=20):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\FinalGroupSimulationResults'+str(N)+'-'+str(inf)+'\\')
    f = open('P0='+str(P0)+', Nen='+str(Nen)+', Inf='+str(inf)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingfinalgroupsimulationrandp(P0,infdown=100,infup=999,N=1000,Nen=20):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\FinalGroupSimulationResultsrandp'+'-'+str(infdown)+'-'+str(infup)+'\\')
    f = open('P0='+str(P0)+', Nen='+str(Nen)+', Infdown='+str(infdown)+', Infup='+str(infup)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var


def loadingfinalgroupsimulationformissingdeltas(P0,delta,inf=0.1,N=1000,Nen=20):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
#    if inf==0.001 or inf==0.005:
 #       os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\FinalGroupSimulation2-'+str(0.001)+'-deltasfaltantes2'+str(N)+'\\')
#    else:
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\FinalGroupSimulationResultsDeltas'+str(N)+'-'+str(inf)+'\\')
    f = open('P0='+str(P0)+', Nen='+str(Nen)+', Inf='+str(inf)+', Delta='+str(delta)+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingdistrpopskewed(name,trial,i,N=1000,alpha=0.1):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\distrpopskewed'+'\\SavedVariablesSize'+str(N)+'Ens100'+'Alpha'+str(alpha))
    f = open(name+str(trial)+str(i)+'.pckl', 'rb')        
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
    
def loadingforspecificdeltas(name,trial,i,kind,delta,poptype,alpha,N=0):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    if kind=='full':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Simulaci\xf3n Preliminar\\Variables Guardadas')
        f = open(name+str(trial)+str(i)+'.pckl', 'rb')
    elif kind=='temp':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\CorridasDeltasFijos\\delta='+str(delta)+'-'+poptype+str(alpha))
        f = open(name+str(trial)+str(i)+'.pckl', 'rb') 
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var

def loadingforspecificdeltasmult(name,trial,i,kind,delta,poptype,alpha,N=0,mult=2):
    
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    if kind=='full':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Simulaci\xf3n Preliminar\\Variables Guardadas')
        f = open(name+str(trial)+str(i)+'.pckl', 'rb')
    elif kind=='temp':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\CorridasDeltasFijos\\delta='+str(delta)+'-'+poptype)
        f = open(name+str(trial)+str(i)+str(mult)+str(alpha)+'.pckl', 'rb') 
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingforspecificdeltastipo(name,trial,i,kind,delta,poptype,alpha,N=0,tipo=0.1):
    #El otro tipo posible es skewed
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    if kind=='full':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Simulaci\xf3n Preliminar\\Variables Guardadas')
        f = open(name+str(trial)+str(i)+'.pckl', 'rb')
    elif kind=='temp':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\CorridasDeltasFijos\\delta='+str(delta)+'-'+poptype)
        if tipo==0.1:
            f = open(name+str(trial)+str(i)+'case'+str(tipo)+'.pckl', 'rb') 
        else:
            f = open(name+str(trial)+str(i)+str(tipo)+'.pckl', 'rb') 
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var
    
def loadingforspecificPrs(name,trial,i,kind):
    import pickle, os
    #f = open('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\\Variables Guardadas\\P0'+str(i)+'.pckl', 'rb')
    A=os.getcwd()
    if kind=='full':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\RepProb')
        f = open(name+str(trial)+'.'+str(i)+'.pckl', 'rb')
    elif kind=='temp':
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Nueva Sim\\RepProb2')
        f = open(name+str(trial)+str(i)+'.pckl', 'rb') 
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var