def getopinions(popu):
    '''This function returns the opinions of all agents in the population popu'''
    import numpy as np
    opinions=[]
    for i in range(len(popu)):
        opinions.append(popu[i].getopinion())
    return np.array(opinions)