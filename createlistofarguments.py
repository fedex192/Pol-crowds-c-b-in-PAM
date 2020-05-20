def createlistofarguments(allarguments=60,baseimpact=1,rangeofimpacts=30):
    '''allarguments must be an even integer'''
    listofarguments=[]
    from Argument import Argument
    
    #The first condition is used to create arguments with the same impact. The second one is used if impacts vary (as in our simulations). 
    
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
            