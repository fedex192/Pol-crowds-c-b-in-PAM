def getundecidedcounts(popu):
    '''This functions simply counts how many agents of each opinion there are in population popu (list of Agents).'''
    count0=0
    countpl=0
    for l in range(len(popu)):
        if popu[l].getopinion()==0:
           count0+=1
        elif popu[l].getopinion()==1:
           countpl+=1
    return count0,countpl,len(popu)-count0-countpl