# -*- coding: utf-8 -*-
'''NOTE: posture is called persuasion in this code.'''

def getagentspersuasion(popu):
    '''This function creates a list with the persuasions of each agent in population popu (list of Agents)'''
    persuasions=[]
    for i in range(len(popu)):
        #print 'Persuasión del Agente '+str(i+1)+': '+str(popu[i].getpersuasion())
        persuasions.append([popu[i].getpersuasion()])
        
    return persuasions

def getagentspersuasion2(popu):
    '''This function creates a list with the persuasions of each agent in population popu (list of Agents)'''
    persuasions=[]
    for i in range(len(popu)):
        #print 'Persuasión del Agente '+str(i+1)+': '+str(popu[i].getpersuasion())
        persuasions.append(popu[i].getpersuasion())
        
    return persuasions
    
#Both functions are the same, but the first one returnes a list of lists, and the second one returns a list of numbers. Both are used in different functions.