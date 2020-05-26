'''The functions on this file are used to analyse contrary information flux, and make the plot of Figure 7 (b).'''

#First, select the proper directory
import os
os.chdir('D:\\Doctorado\\Simulation_Functions\\') 

def runargsimwithPCBcontraryflux(allargs=60,N=10,numofrelevargs=6,steps=10000,p=0.5,Ct=1.0, Cmax=3.0,intertype='Bid'):
    '''This function is mainly the same as newrunargsim, found in newrunargsim.py. The comments for most lines of code
    can be found there, and will not be repeated here. However, we will add comments to the new lines. New input:
        "p" is the probability of confirmation bias.'''
    
    #First, we import a special type of interaction used for this simulation alone. It returns the arguments exchanged
    #between the agents when their interaction involves contrary flux. This is the only important difference between this
    #function and argumentativeinteraction of newinteraction.py, which we thoroughly commented. We did not apply thorough comments
    #to this version, but we added a note at the beginning of the file, listing all changes. If needed, please refer to that comment.
    from argumentativeinteractioncontraryflux import argumentativeinteractioncontraryflux
    #The rest of the functions required:
    from population import argumentativepopulation
    from createlistofarguments import createlistofarguments
    from getundecidedcounts import getundecidedcounts
    from getagentspersuasion import getagentspersuasion
    import numpy as np

    listofarguments=createlistofarguments(allargs,1,allargs/2)

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
           
    #new initializations    
    fluxevolution=[] 
    strengthevolution=[]         
    
    for i in range(steps):
        
        #New lines: here we determine if the interaction for this step will involve confirmation bias or not.
        if np.random.random()<p:
            cb='yes'
        else:
            cb='no'
            
            
        subpersuasions=getagentspersuasion(popu)  
        for j in range(len(popu)):
            persuasions[j]+=subpersuasions[j]
            
        #Beginning of new code:
        
        #new initializations
        flux=0 
        strength=0    
            

        b=argumentativeinteractioncontraryflux(popu, listofarguments, Cmax, intertype, cb,'bidirectional') #use the new interaction
        #described above
        if b==0:
            pass #if there was no flux, we do nothing here
        else: #if there was flux of contrary information:
                        
            flux+=1 #This simply counts how many interactions involved exchange of opposing arguments. It is one way of measuring flux.
            #This measures flux by the (signless) weight of the opposing arguments exchanged; this is the way of measurement used in the 
            #paper.
            
            #First argument exchanged:
            if b[1]>=30:
               strength+=(b[1]-30)+1 
            elif b[1]<30 and b[1]!=-1:
                strength+=b[1]+1
            #Second argument exchanged:    
            if b[2]>=30:
               strength+=(b[2]-30)+1
            elif b[2]<30 and b[1]!=-1:
                strength+=b[2]+1
                    
        fluxevolution.append(flux) #We save the flux measured by the first method, in this interaction.
        strengthevolution.append(strength) #we save the flux measured by the second method, in this interaction.
         
        #end of new code.                     
                        
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
    # we now also return the sum of flux for all interactions, as measured by both methods.
    return countsund, countspro, countsagainst,flag,sum(fluxevolution),sum(strengthevolution) 


def analysingflux(Nen=1000,p=0.0):
    '''This function is used for analysing the results of the previous one. It runs the previous function Nen times (copies of the ensamble),
    and returns the results for both methods of measurement of flux. It should be run for each value of P_CB.'''
    #Initializations
    cases=[]
    strengths=[]
    #For each copy of the ensamble:
    for i in range(Nen):      
        A=runargsimwithPCBcontraryflux(60,10,6,10000,p,Ct=1.0, Cmax=3.0,intertype='Bid') #run simulation
        cases.append(A[4]) #save result 1 in a list.
        strengths.append(A[5]) #save result 2 in a list.
    return cases,strengths #return results.
            
def explorfluxsim():
    '''This functions uses the previous one for exploring all possible values of P_CB'''
    import numpy as np
    #initializations
    allcases=[]
    allstrenghts=[]
    for p in [0.0,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0]: #all the values we studied of P_CB
        print(p) #for keeping truck
        alpha=analysingflux(1000,p) #results of the previous functions
        allcases.append(np.mean(alpha[0])) #list of results of method 1 of measuring flux
        allstrenghts.append(np.mean(alpha[1])) #list of results of method 2 of measuring flux
        
    from saving import savinggeneric #import a function for saving the results.
    savinggeneric([allcases,allstrenghts],'fluxsimforM6') #save the results with the appropriate name.
    
def plottingflux():
    '''This function is used for plotting the results of the Contrary Flux variable vs. P_CB, seen in Figure 7, (b).'''
    import pylab as py
    from loading import loadinggeneric #loading function
    a=loadinggeneric('fluxsimforM6') #loading saved data.
    
    weights=a[1] #measured weights
    Ps=[0.0,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0] #P_CB values explored
    
    #plotting commands
    py.plot(Ps,weights,lw=4)
    py.xlabel(u'P',size=16)
    py.ylabel(u'$\\varphi$',size=16)
    py.yticks(range(0,151,50),size=16)
    py.xticks(size=16)
    #save the figure
    py.savefig(u'phi.svg', bbox_inches='tight')      