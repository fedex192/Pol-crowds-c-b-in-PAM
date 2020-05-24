# -*- coding: utf-8 -*-
'''Saving functions used to save the results of the simulations. NOTE: posture is called persuasion inside this code'''

def savinggeneric(var,specifications='a',path='D:\\Doctorado\\Simulation_Functions\\'):
    '''This is the most generic saving method used in most of the functions. It is easy and straightforward to use:
    "var" is the variable to be saved.
    "specifications" is the name of the file to be saved.
    "path" is the path where the file should be saved.
    It does not return anything. It does not change the initial directory after being used.'''
    
    import pickle, os
    #filepath = os.path.join('C:\Macrocosmos\Universal\Física\Tesis de Licenciatura\Simulación Preliminar\Variables Guardadas', 'P0'+str(i)+'.pckl')
    #f = open(filepath, 'wb')
    direct=os.getcwd()
    f = open(path+specifications+'.pckl', 'wb')
    pickle.dump(var, f)
    f.close()
    os.chdir(direct)
 
    
def savingargumentsimulation2(finalresult,rel,N,numens,opsys='w',specifications=''): 
    '''This saving function was used for the results of the function explorargsimforrelandN, in exploringM.py. It was used in windows and
    linux; it checks if the chosen path exists or not, its named can be modified by using the specifications input, and it has some 
    parameters specific to the functions that used this. NOTE: if you are running those explorations, it would be better to use savinggeneric 
    instead of this, but this can still be used if the directories are modified appropriately. Note: there was a "1" version of this, but
    it was not used for the paper.'''
    
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
    '''This saving function was used for the results of the functions explorargsimforrelandArs, in exploringM.py. As before, it was used in windows and 
    linux, it checks if the chosen path exists or not and creates it if needed, its named can be modified by using the specifications input, and it has 
    some parameters specific to the functions that used this. NOTE: if you are running those explorations, it would be better to use savinggeneric 
    instead of this, but this can still be used if the directories are modified appropriately".'''       
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