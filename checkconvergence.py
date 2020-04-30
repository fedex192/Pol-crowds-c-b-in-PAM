# -*- coding: utf-8 -*-
def checkconvergence(popu,cb='no'):
    import numpy as np
    persuasions=[]
    for i in range(len(popu)):
        #print 'Persuasión del Agente '+str(i+1)+': '+str(popu[i].getpersuasion())
        persuasions.append(float(popu[i].getpersuasion()))
    
    a=np.unique(persuasions)
    
    #print(a)
    
    if len(a)==1:
        convergence=True
    elif len(a)==2:
        if float(abs(a[1]))==float(3) and float(abs(a[0]))==float(3):
            convergence=True
        elif np.sign(a[1])==np.sign(a[0]) and abs(a[1])>1 and abs(a[0])>1:
            convergence=True
        # elif np.sign(a[1])==np.sign(a[0]) and abs(a[1])<=1 and abs(a[0])<=1: #atrapa oscilaciones. En teoría, podria perderse 
        #     #algún caso no oscilatorio, que sea tomado como moderado, pero que haya sido no convergido.
        #     convergence=True           
        else:
            convergence=False
        if cb=='yes':
            if np.sign(a[1])!=np.sign(a[0]) and abs(a[1])>1 and abs(a[0])>1: #si hay CB, opuestos no se hablan. Si son de opiniones opuestas, ya convergieron.
                convergence=True            
    else:
        
        # if len(a)==3 and (float(3) in a) and (float(-3) in a) and len(np.unique(abs(np.array(a))>1))==1: #Con esto pretendo capturar oscilaciones nuevas creadas por homofilia fuerte.
        #     convergence=True
        # elif len(a)==4 and (float(3) in a) and (float(-3) in a) and len(np.unique(abs(np.array(a))>1))==1: #Con esto pretendo capturar oscilaciones nuevas creadas por homofilia fuerte.
        #     convergence=True                  
        # elif len(a)==5 and (float(3) in a) and (float(-3) in a) and len(np.unique(abs(np.array(a))>1))==1: #Con esto pretendo capturar oscilaciones nuevas creadas por homofilia fuerte.
        #     convergence=True                
        if len(np.unique(np.sign(a)))==1 and len(np.unique(abs(np.array(a))>1))==1:
            convergence=True
        else:
            convergence=False
            
        if cb=='yes':
            if len(np.unique(np.sign(a)))==2 and sum((abs(np.array(a))>1))==len(a): #Si hay CB, y están los dos signos, pero son todos orientados, ya convergieron.
                convergence=True
        
    return convergence