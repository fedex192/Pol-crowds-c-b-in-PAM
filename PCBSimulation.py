'''The functions on this file are used to analyse the case where there is a Probability of Confirmation Bias (P_CB), 
and make the plot of Figure 6 (a). NOTE: posture is called persuasion in all this code.'''

def runargsimwithPCB(allargs=60,rangeofimpacts=30,N=10,numofrelevargs=6,steps=10000,p=0.5,Ct=1.0, Cmax=3.0,intertype='Bid'):
    '''This function is very similar to newrunargsim, found in newrunargsim.py. The only difference is that the interaction is
    done with or without confirmation bias, depending on the new input "p", which is P_CB, the probability of confirmation bias.
    Since that function was thoroughly commented, we will not be adding comments to this one, except for the new lines of code.'''
    
    from population import argumentativepopulation
    from createlistofarguments import createlistofarguments
    from interaction import argumentativeinteraction
    from getundecidedcounts import getundecidedcounts
    from getagentspersuasion import getagentspersuasion
    import numpy as np

    listofarguments=createlistofarguments(allargs,1,rangeofimpacts)
    
    popu=argumentativepopulation(listofarguments,N,numofrelevargs,Ct,Cmax)
    
    countsund=[]
    countspro=[]
    countsagainst=[]
    a=getundecidedcounts(popu)
    countsund.append(a[0])
    countspro.append(a[1])
    countsagainst.append(a[2])
    
    persuasions=[[] for i in range(len(popu))]
    
    stepcount=0
    if N<50:
        breakcount=6000
    elif N>=50 and N<80:
        breakcount=6000
    else:
        breakcount=6000
        
    for i in range(steps):
        
        #new lines of code:
        if np.random.random()<p: #this uses p to determine if the interaction is performed with or without confirmation bias.
            cb='yes'
        else:
            cb='no'
        #end of new lines of code.
        
        subpersuasions=getagentspersuasion(popu)  
        for j in range(len(popu)):
            persuasions[j]+=subpersuasions[j]          
            
        b=argumentativeinteraction(popu, listofarguments, Cmax, intertype, cb,'bidirectional')
        
        a=getundecidedcounts(popu)
        countsund.append(a[0])
        countspro.append(a[1])
        countsagainst.append(a[2])
        
        tempcount=0
        if i!=0:
            for persuasion in range(len(persuasions)):
                if persuasions[persuasion][-1]==persuasions[persuasion][-2]:
                    tempcount+=1
            if tempcount==N:
                stepcount+=1
            else:
                stepcount=0
        if stepcount==breakcount:
            break

    if i>9000:
        flag=1
    else:
        flag=0 
        
    subpersuasions=getagentspersuasion(popu)  
    for j in range(len(popu)):
        persuasions[j]+=subpersuasions[j]

    return countsund, countspro, countsagainst,flag
    
        
def exploringfinalstateswithPCB(numens=1000,N=10,allargs=50,steps=10000,p=0.5,numofrelevargs=6):
        '''This function is used for parameter exploration, using the previous one. It is very similar to all other parameter
        exploration functions, found in newexplorargsim.py, exploringM.py and exploringDelta.py, so we will not be adding
        additional comments to it. The only new input is:
            "p" is P_CB, the probability of interacting with confirmation bias.'''
        
        counts0=0
        countspl=0
        countsmin=0
        countsbip=0
        otherstuff=0
        countosc=0
        for i in range(numens):
            a=runargsimwithPCB(allargs,allargs/2,N,6,steps,p)
            if a[1][-1]==N:
                countspl+=1
            elif a[2][-1]==N:
                countsmin+=1
            elif a[0][-1]==N:
                counts0+=1
            elif a[0][-1]==0:
                countsbip+=1 
            else:                        
                otherstuff+=1  
            
            countosc+=a[-1] 
        
        from saving import savinggeneric
        
        savinggeneric((counts0,countspl,countsmin,countsbip,otherstuff,countosc),'PCBNargs50simwithp'+str(p))
        
        return counts0,countspl,countsmin,countsbip,otherstuff,countosc 
        
        
def runexplorfinalstateswithPCB():
    '''This functions uses the previous one for exploring all possible values of P_CB'''
    for p in [0.0,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0]:
        exploringfinalstateswithPCB(1000,10,60,10000,p,6)  
        
        
        
def plottingPCB(N=10,Ars=60,Rel=6):
    '''This function is used for plotting the results of the Final States vs. P_CB exploration, seen in Figure 7, (a).'''
    import pylab as py
    #Initialization
    results=[]
    #Studied values of P_CB
    probs=[0.0,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0]

    from loading import loadinggeneric #for loading the results
    
    for i in range(len(probs)):
        results.append(loadinggeneric('PCBsimwithp'+str(probs[i]))) #we load each result
    
    results=py.array(results)/1000.0 #divide by the ensamble size (we used a 1000; this must be changed if another one is used).
    
    #initializations
    ind=[] #moderate consensus  
    cons=[] #oriented consensus
    bip=[] #bipolarization
    others=[] #other states (if there are any, which there are not)
    osc=[] #oscillations, to be on the safe side
    for i in range(len(results)):
        ind.append(results[i][0])
        cons.append(results[i][1]+results[i][2])
        bip.append(results[i][3])
        others.append(results[i][4])
        osc.append(results[i][5])
        
    #We choose which colors to use
    colors=[0,120/255.0,255/255.0,150/255.0], [215/255.0,50/255.0,0/255.0,240/255.0], [0/255.0,155/255.0,0/255.0,220/255.0]
    
    #plotting commands
    py.figure()
    py.xlabel(u'$P_{CB}$',size=18) 
    py.ylabel(u'$P_{finstats}$',size=18)
    py.plot(probs,ind,'o-',color=colors[0],lw=4)
    py.plot(probs,cons,'-.',color=colors[1],lw=4)
    py.plot(probs,bip,'o-',color=colors[2],lw=4)
    py.xticks(size=18)
    py.yticks(size=18)
    py.legend([u'Moderate Consensus','Oriented Consensus','Bipolarization'],prop={'size':16})
    #save the figure
    py.savefig(u'Estados Finales vs Prob - '+'N'+str(N)+'Ars'+str(Ars)+'Rel'+str(Rel)+'.svg', bbox_inches='tight')  