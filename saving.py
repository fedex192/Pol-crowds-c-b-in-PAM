# -*- coding: utf-8 -*-
def saving(var,P0,delta,folder,N=1000,opsys='w',specifications=''):
    '''var is the variable to be saved. P0 and delta are the parameters. folder is the name of the folder in which
    it is to be saved (specify everything that is needed to distinguish it from the other simulation). opsys is the
    operating system, 'w' for windows,'u' for ubuntu or 'lu' for lubuntu. Finally, specifications are used in the
    name of the file to be saved; for example, I've used 'trio' before, for files containing undecided, prodecided
    and againstdecideds.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)):
            os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N))
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N))
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariablesoneforall/'+folder+str(N)):
            os.makedirs('/home/fbarrera/SavedVariablesoneforall/'+folder+str(N))
        os.chdir('/home/fbarrera/SavedVariablesoneforall/'+folder+str(N))
    elif opsys=='lu':
        if not os.path.exists('/home/fede/Desktop/SavedVariables'+folder+str(N)):
            os.makedirs('/home/fede/Desktop/SavedVariables'+folder+str(N))
        os.chdir('/home/fede/Desktop/SavedVariables'+folder+str(N))
    elif opsys=='w2':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\'+folder+str(N)):
            os.makedirs('C:\\Macrocosmos\\Universal\\'+folder+str(N))
        os.chdir('C:\\Macrocosmos\\Universal\\'+folder+str(N))        
    f = open('simP0'+str(P0)+'andDelta'+str(delta)+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(A)

def savingargumentvariables(var,specifications='',N=100,opsys='w',folder='MasSimulation'):
    import pickle, os
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\'+folder+str(N)):
            os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\'+folder+str(N))
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\'+folder+str(N))
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/'+folder+str(N)):
            os.makedirs('/home/fbarrera/'+folder+str(N))
        os.chdir('/home/fbarrera/'+folder+str(N))
    
    f = open(specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(A)

def savingfinalgroupsimulation(var,specifications='',N=1000,opsys='w',folder='FinalGroupSimulation'):
    import pickle, os
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\'+folder+str(N)):
            os.makedirs('C:\\Macrocosmos\\Universal\\'+folder+str(N))
        os.chdir('C:\\Macrocosmos\\Universal\\'+folder+str(N))
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/'+folder+str(N)):
            os.makedirs('/home/fbarrera/'+folder+str(N))
        os.chdir('/home/fbarrera/'+folder+str(N))
    
    f = open(specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(A)

def savingexplorationsforsingleinteraction(var,newCtini,newCtfin,folder,N=10,opsys='w',specifications=''):
    '''var is the variable to be saved. P0 and delta are the parameters. folder is the name of the folder in which
    it is to be saved (specify everything that is needed to distinguish it from the other simulation). opsys is the
    operating system, 'w' for windows,'u' for ubuntu or 'lu' for lubuntu. Finally, specifications are used in the
    name of the file to be saved; for example, I've used 'trio' before, for files containing undecided, prodecided
    and againstdecideds.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    A=os.getcwd()
 #   C:\\Users\\Guillermo Lemarchand\\Desktop\\Avances de la Tesis\\Segunda Parte\\Explorando Persuasion Inter de a Pares\\
    #C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\
    if opsys=='w':
        if not os.path.exists('C:\\Users\\Guillermo Lemarchand\\Desktop\\Avances de la Tesis\\Segunda Parte\\Explorando Persuasion Inter de a Pares\\'+folder+str(N)):
            os.makedirs('C:\\Users\\Guillermo Lemarchand\\Desktop\\Avances de la Tesis\\Segunda Parte\\Explorando Persuasion Inter de a Pares\\'+folder+str(N))
        os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Avances de la Tesis\\Segunda Parte\\Explorando Persuasion Inter de a Pares\\'+folder+str(N))
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariables/'+folder+str(N)):
            os.makedirs('/home/fbarrera/SavedVariables/'+folder+str(N))
        os.chdir('/home/fbarrera/SavedVariables/'+folder+str(N))
    elif opsys=='lu':
        if not os.path.exists('/home/fede/Desktop/SavedVariables'+folder+str(N)):
            os.makedirs('/home/fede/Desktop/SavedVariables'+folder+str(N))
        os.chdir('/home/fede/Desktop/SavedVariables'+folder+str(N))
    f = open('newCtini - '+str(newCtini)+' - newCtfin - '+str(newCtfin)+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(A)

def savingexplorationsforsingleinteractionsameinits(var,newCtini,newCtfin,folder,N=10,opsys='w',specifications=''):
    '''var is the variable to be saved. P0 and delta are the parameters. folder is the name of the folder in which
    it is to be saved (specify everything that is needed to distinguish it from the other simulation). opsys is the
    operating system, 'w' for windows,'u' for ubuntu or 'lu' for lubuntu. Finally, specifications are used in the
    name of the file to be saved; for example, I've used 'trio' before, for files containing undecided, prodecided
    and againstdecideds.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    A=os.getcwd()
 #   C:\\Users\\Guillermo Lemarchand\\Desktop\\Avances de la Tesis\\Segunda Parte\\Explorando Persuasion Inter de a Pares\\
    #C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\
    if opsys=='w':
        if not os.path.exists('C:\\Users\\Guillermo Lemarchand\\Desktop\\Avances de la Tesis\\Segunda Parte\\Explorando Persuasion Inter de a Pares\\Same Initial Conditions\\'+folder+str(N)):
            os.makedirs('C:\\Users\\Guillermo Lemarchand\\Desktop\\Avances de la Tesis\\Segunda Parte\\Explorando Persuasion Inter de a Pares\\Same Initial Conditions\\'+folder+str(N))
        os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Avances de la Tesis\\Segunda Parte\\Explorando Persuasion Inter de a Pares\\Same Initial Conditions\\'+folder+str(N))
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariables/'+folder+str(N)):
            os.makedirs('/home/fbarrera/SavedVariables/'+folder+str(N))
        os.chdir('/home/fbarrera/SavedVariables/'+folder+str(N))
    elif opsys=='lu':
        if not os.path.exists('/home/fede/Desktop/SavedVariables'+folder+str(N)):
            os.makedirs('/home/fede/Desktop/SavedVariables'+folder+str(N))
        os.chdir('/home/fede/Desktop/SavedVariables'+folder+str(N))
    f = open('newCtini - '+str(newCtini)+' - newCtfin - '+str(newCtfin)+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(A)


def savinggeneric(var,specifications='a',path='D:\\Doctorado\\Simulation_Functions\\'):
    '''var is the variable to be saved. P0 and delta are the parameters. folder is the name of the folder in which
    it is to be saved (specify everything that is needed to distinguish it from the other simulation). opsys is the
    operating system, 'w' for windows,'u' for ubuntu or 'lu' for lubuntu. Finally, specifications are used in the
    name of the file to be saved; for example, I've used 'trio' before, for files containing undecided, prodecided
    and againstdecideds.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    direct=os.getcwd()
    f = open(path+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(direct)
 
    
def savingoneforall(var,delta,P0,N,folder='Int Grupal - Grupos Variables - N=',opsys='w',specifications=''):
    '''var is the variable to be saved. P0 and delta are the parameters. folder is the name of the folder in which
    it is to be saved (specify everything that is needed to distinguish it from the other simulation). opsys is the
    operating system, 'w' for windows,'u' for ubuntu or 'lu' for lubuntu. Finally, specifications are used in the
    name of the file to be saved; for example, I've used 'trio' before, for files containing undecided, prodecided
    and againstdecideds.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)):
            os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N))
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N))
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariables/'+folder+str(N)):
            os.makedirs('/home/fbarrera/SavedVariables/'+folder+str(N))
        os.chdir('/home/fbarrera/SavedVariables/'+folder+str(N))
    elif opsys=='lu':
        if not os.path.exists('/home/fede/Desktop/SavedVariables'+folder+str(N)):
            os.makedirs('/home/fede/Desktop/SavedVariables'+folder+str(N))
        os.chdir('/home/fede/Desktop/SavedVariables'+folder+str(N))
    f = open('simP0'+str(P0)+'andDelta'+str(delta)+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(A)

def savingoneforallconvergence(var,delta,P0,N,folder='Int Grupal - Grupos Variables - N=',opsys='w',specifications=''):
    '''var is the variable to be saved. P0 and delta are the parameters. folder is the name of the folder in which
    it is to be saved (specify everything that is needed to distinguish it from the other simulation). opsys is the
    operating system, 'w' for windows,'u' for ubuntu or 'lu' for lubuntu. Finally, specifications are used in the
    name of the file to be saved; for example, I've used 'trio' before, for files containing undecided, prodecided
    and againstdecideds.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'Convergence'):
            os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'Convergence')
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'Convergence')
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariables/'+folder+str(N)+'Convergence'):
            os.makedirs('/home/fbarrera/SavedVariables/'+folder+str(N)+'Convergence')
        os.chdir('/home/fbarrera/SavedVariables/'+folder+str(N)+'Convergence')
    elif opsys=='lu':
        if not os.path.exists('/home/fede/Desktop/SavedVariables'+folder+str(N)):
            os.makedirs('/home/fede/Desktop/SavedVariables'+folder+str(N))
        os.chdir('/home/fede/Desktop/SavedVariables'+folder+str(N))
    f = open('simP0'+str(P0)+'andDelta'+str(delta)+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(A)


def savingoneforallforgroupanalysis(var,delta,P0,N,folder='Int Grupal - Grupos Variables - N=',opsys='w',specifications=''):
    '''var is the variable to be saved. P0 and delta are the parameters. folder is the name of the folder in which
    it is to be saved (specify everything that is needed to distinguish it from the other simulation). opsys is the
    operating system, 'w' for windows,'u' for ubuntu or 'lu' for lubuntu. Finally, specifications are used in the
    name of the file to be saved; for example, I've used 'trio' before, for files containing undecided, prodecided
    and againstdecideds.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'forgroupanalysis'):
            os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'forgroupanalysis')
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'forgroupanalysis')
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariables/'+folder+str(N)+'forgroupanalysis'):
            os.makedirs('/home/fbarrera/SavedVariables/'+folder+str(N)+'forgroupanalysis')
        os.chdir('/home/fbarrera/SavedVariables/'+folder+str(N)+'forgroupanalysis')
    elif opsys=='lu':
        if not os.path.exists('/home/fede/Desktop/SavedVariables'+folder+str(N)):
            os.makedirs('/home/fede/Desktop/SavedVariables'+folder+str(N))
        os.chdir('/home/fede/Desktop/SavedVariables'+folder+str(N))
    f = open('simP0'+str(P0)+'andDelta'+str(delta)+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(A)
    

def savinggrouppairinteraction(var,delta,P0,N,opsys='w',folder='Int Pares - Grupos Variables - N=',specifications=''):
    '''var is the variable to be saved. P0 and delta are the parameters. folder is the name of the folder in which
    it is to be saved (specify everything that is needed to distinguish it from the other simulation). opsys is the
    operating system, 'w' for windows,'u' for ubuntu or 'lu' for lubuntu. Finally, specifications are used in the
    name of the file to be saved; for example, I've used 'trio' before, for files containing undecided, prodecided
    and againstdecideds.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)):
            os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N))
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N))
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariables/'+folder+str(N)):
            os.makedirs('/home/fbarrera/SavedVariables/'+folder+str(N))
        os.chdir('/home/fbarrera/SavedVariables/'+folder+str(N))
    elif opsys=='lu':
        if not os.path.exists('/home/fede/Desktop/SavedVariables'+folder+str(N)):
            os.makedirs('/home/fede/Desktop/SavedVariables'+folder+str(N))
        os.chdir('/home/fede/Desktop/SavedVariables'+folder+str(N))
    f = open('simP0'+str(P0)+'andDelta'+str(delta)+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(A)
 
  
def savinggrouppairinteractionforgroupanalysis(var,delta,P0,N,opsys='w',folder='IntParesN',specifications=''):
    '''var is the variable to be saved. P0 and delta are the parameters. folder is the name of the folder in which
    it is to be saved (specify everything that is needed to distinguish it from the other simulation). opsys is the
    operating system, 'w' for windows,'u' for ubuntu or 'lu' for lubuntu. Finally, specifications are used in the
    name of the file to be saved; for example, I've used 'trio' before, for files containing undecided, prodecided
    and againstdecideds.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'forgroupanalysis'):
            os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'forgroupanalysis')
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'forgroupanalysis')
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariables/'+folder+str(N)+'forgroupanalysis'):
            os.makedirs('/home/fbarrera/SavedVariables/'+folder+str(N)+'forgroupanalysis')
        os.chdir('/home/fbarrera/SavedVariables/'+folder+str(N)+'forgroupanalysis')
    elif opsys=='lu':
        if not os.path.exists('/home/fede/Desktop/SavedVariables'+folder+str(N)):
            os.makedirs('/home/fede/Desktop/SavedVariables'+folder+str(N))
        os.chdir('/home/fede/Desktop/SavedVariables'+folder+str(N))
    f = open('simP0'+str(P0)+'andDelta'+str(delta)+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(A)
  
    
def savinggrouppairinteractionconvergence(var,delta,P0,N,opsys='w',folder='Int Pares - Grupos Variables - N=',specifications=''):
    '''var is the variable to be saved. P0 and delta are the parameters. folder is the name of the folder in which
    it is to be saved (specify everything that is needed to distinguish it from the other simulation). opsys is the
    operating system, 'w' for windows,'u' for ubuntu or 'lu' for lubuntu. Finally, specifications are used in the
    name of the file to be saved; for example, I've used 'trio' before, for files containing undecided, prodecided
    and againstdecideds.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'Convergence'):
            os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'Convergence')
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Sim Grupal\\'+folder+str(N)+'Convergence')
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariables/'+folder+str(N)+'Convergence'):
            os.makedirs('/home/fbarrera/SavedVariables/'+folder+str(N)+'Convergence')
        os.chdir('/home/fbarrera/SavedVariables/'+folder+str(N)+'Convergence')
    elif opsys=='lu':
        if not os.path.exists('/home/fede/Desktop/SavedVariables'+folder+str(N)):
            os.makedirs('/home/fede/Desktop/SavedVariables'+folder+str(N))
        os.chdir('/home/fede/Desktop/SavedVariables'+folder+str(N))
    f = open('simP0'+str(P0)+'andDelta'+str(delta)+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(A)
    
def savingargumentsimulation(finalresult,allargs,N,numens,opsys='w',specifications=''):   
    import pickle, os
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsindbid\\'+'FullExploration'+specifications+str(numens)):
            os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsindbid\\'+'FullExploration'+specifications+str(numens))
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsindbid\\'+'FullExploration'+specifications+str(numens))
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariables/ArgumentsSimsindbid/FullExploration'+specifications+str(numens)):
            os.makedirs('/home/fbarrera/SavedVariables/ArgumentsSimsindbid/FullExploration'+specifications+str(numens))
        os.chdir('/home/fbarrera/SavedVariables/ArgumentsSimsindbid/FullExploration'+specifications+str(numens))
    f = open('allargs'+str(allargs)+', N='+str(N)+', Ens='+str(numens)+'.pckl', 'wb')
    pickle.dump(finalresult, f)
    f.close()
    os.chdir(A)
    
def savingargumentsimulation2(finalresult,rel,N,numens,opsys='w',specifications=''):   
    import pickle, os
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsRel\\'+'FullExploration'+specifications+str(numens)):
            os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsRel\\'+'FullExploration'+specifications+str(numens))
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsRel\\'+'FullExploration'+specifications+str(numens))
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariables/ArgumentsSimsRel/FullExploration'+specifications+str(numens)):
            os.makedirs('/home/fbarrera/SavedVariables/ArgumentsSimsRel/FullExploration'+specifications+str(numens))
        os.chdir('/home/fbarrera/SavedVariables/ArgumentsSimsRel/FullExploration'+specifications+str(numens))
    f = open('rel'+str(rel)+', N='+str(N)+', Ens='+str(numens)+'.pckl', 'wb')
    pickle.dump(finalresult, f)
    f.close()
    os.chdir(A)
    
def savingargumentsimulation3(finalresult,rel,Ars,numens,opsys='w',specifications=''):   
    import pickle, os
    A=os.getcwd()
    if opsys=='w':
        if not os.path.exists('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsRelArs\\'+'FullExploration'+specifications+str(numens)):
            os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsRelArs\\'+'FullExploration'+specifications+str(numens))
        os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsRelArs\\'+'FullExploration'+specifications+str(numens))
    elif opsys=='u':
        if not os.path.exists('/home/fbarrera/SavedVariables/ArgumentsSimsRelArs/FullExploration'+specifications+str(numens)):
            os.makedirs('/home/fbarrera/SavedVariables/ArgumentsSimsRelArs/FullExploration'+specifications+str(numens))
        os.chdir('/home/fbarrera/SavedVariables/ArgumentsSimsRelArs/FullExploration'+specifications+str(numens))
    f = open('rel'+str(rel)+', Ars='+str(Ars)+', Ens='+str(numens)+'.pckl', 'wb')
    pickle.dump(finalresult, f)
    f.close()
    os.chdir(A)
    
def newsavinggeneric(var,specifications='a',path='C:\\Users\\Fede\\Desktop\\Datos_Argumentos\\'):
    '''var is the variable to be saved. P0 and delta are the parameters. folder is the name of the folder in which
    it is to be saved (specify everything that is needed to distinguish it from the other simulation). opsys is the
    operating system, 'w' for windows,'u' for ubuntu or 'lu' for lubuntu. Finally, specifications are used in the
    name of the file to be saved; for example, I've used 'trio' before, for files containing undecided, prodecided
    and againstdecideds.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    direct=os.getcwd()
    if not os.path.exists(path):
       os.makedirs(path)
    f = open(path+'var'+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(direct)    
    
# def newsavingargumentsimulation(finalresult,allargs,N,numens,opsys='w',specifications=''):   
#     import pickle, os
#     A=os.getcwd()
#     if opsys=='w':
#         if not os.path.exists('Datos_Argumentos\\ArgumentsSimsindbid\\'+'FullExploration'+specifications+str(numens)):
#             os.makedirs('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsindbid\\'+'FullExploration'+specifications+str(numens))
#         os.chdir('C:\\Macrocosmos\\Universal\\F\xedsica\\Tesis de Licenciatura\\Argument Simulations\\ArgumentsSimsindbid\\'+'FullExploration'+specifications+str(numens))
#     elif opsys=='u':
#         if not os.path.exists('/home/fbarrera/SavedVariables/ArgumentsSimsindbid/FullExploration'+specifications+str(numens)):
#             os.makedirs('/home/fbarrera/SavedVariables/ArgumentsSimsindbid/FullExploration'+specifications+str(numens))
#         os.chdir('/home/fbarrera/SavedVariables/ArgumentsSimsindbid/FullExploration'+specifications+str(numens))
#     f = open('allargs'+str(allargs)+', N='+str(N)+', Ens='+str(numens)+'.pckl', 'wb')
#     pickle.dump(finalresult, f)
#     f.close()
#     os.chdir(A)    