cpdef createlistofarguments(int allarguments=60,int baseimpact=1,int rangeofimpacts=1):
    '''allarguments must be an even integer'''
    cdef list listofarguments, positivevalences, negativevalences
    cdef int arguments
    listofarguments=[]
    from Argument2 import Argument 
    if rangeofimpacts==1:
        for arguments in range(allarguments):
            if arguments<allarguments/2.0:
                listofarguments.append(Argument(1,baseimpact))
            else:
                listofarguments.append(Argument(-1,baseimpact))
    elif rangeofimpacts!=1:
        positivevalences=range(1,rangeofimpacts+1)
        negativevalences=range(1,rangeofimpacts+1)
        for arguments in range(allarguments):
            if arguments<allarguments/2.0:
                listofarguments.append(Argument(1,positivevalences[0]))
                positivevalences.pop(0)
            else:
                listofarguments.append(Argument(-1,negativevalences[0]))            
                negativevalences.pop(0)
                
    return listofarguments
            