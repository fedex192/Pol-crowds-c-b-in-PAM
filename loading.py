def loadinggeneric(specifications='a',path='D:\\Doctorado\\Simulation_Functions\\'):
    '''This is the counterpart of the savinggeneric function of saving.py. It loads individual files saved by the exploration functions.
    "specifications" should be the name of the file.
    "path" is the directory where it is saved.
    It returns the saved variables.'''
    
    import pickle, os
    A=os.getcwd()
    os.chdir(path)
    f = open(specifications+'.pckl', 'rb')
    var = pickle.load(f)
    f.close()
    os.chdir(A)
    return var