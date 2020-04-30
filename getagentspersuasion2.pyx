# -*- coding: utf-8 -*-
cpdef list getagentspersuasion(list popu):
    cdef list persuasions
    cdef int i
    persuasions=[]
    for i in range(len(popu)):
        #print 'Persuasión del Agente '+str(i+1)+': '+str(popu[i].getpersuasion())
        persuasions.append([popu[i].getpersuasion()])
        
    return persuasions

cpdef list getagentspersuasion2(list popu):    
    cdef list persuasions
    cdef int i    
    persuasions=[]
    for i in range(len(popu)):
        #print 'Persuasión del Agente '+str(i+1)+': '+str(popu[i].getpersuasion())
        persuasions.append(popu[i].getpersuasion())
        
    return persuasions