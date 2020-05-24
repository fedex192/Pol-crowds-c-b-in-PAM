def gettingopinionsevolutions(N=10,which=1):        
        '''This function is used for generating the input for plottingopinions. Choose the appropriate N, and the state you wish to study.
        If which=0, then it is the moderate consensus. If which=1, then it is oriented positive consensus. If which=2, then it is
        oriented negative consensus. If which=3, it is bipolarization (only found for the case with confirmation bias or homophily,
        both of which are turned off here).'''                              
        import numpy as np
        
        #initializations
        countsund=np.array([0 for i in range(6001)]) #this last number is related to the number of steps to use in newrunargsim. It must be steps+1.
        countspro=np.array([0 for i in range(6001)])
        countsagainst=np.array([0 for i in range(6001)])
        newcountsund=[]
        newcountspro=[]
        newcountsagainst=[]

        i=0
        
        from newrunargsim import newrunargsim #using newrunargsimforprofiling is also possible, but here we can choose the necessary steps.
        
        while i<100: #this is the number of copies one wishes to have, that end in the chosen final state. For example, 100 copies of moderate state.
            a=newrunargsim(60,30,N,6,6000,'no','no',0,1.0,3.0,'Bid') #note the number of steps. No confirmation bias and no homophily (this can be changed).-

            if a[which][-1]==N:
                
                countsund+=np.array(a[0])
                countspro+=np.array(a[1])
                countsagainst+=np.array(a[2])  
                #these next variables are for use with the function for plotting opinions with errors.
                newcountsund.append(np.array(a[0]))
                newcountspro.append(np.array(a[1]))
                newcountsagainst.append(np.array(a[2]))
                i+=1   
        
        return countsund,countspro,countsagainst,newcountsund,newcountspro,newcountsagainst

def plottingopinions(a):           
        '''This function is used for plotting the evolution of opinions. The input must be the output of gettingopinionsevolution or newrunargsim or
        newrunargsimforprofiling. This was used for the opinion evolution plots of Figure 3.'''        
        #number of agents of each opinion, for each copy of the ensamble:
        countsund=a[0]
        countspro=a[1]
        countsagainst=a[2]                                                        
                                                                                                                                        
        import pylab as py
        py.figure()    
        
        N=10 #this number must be changed depending on the simulation parameters. 
        
        factor=100.0*N #For the paper, we always used 100 copies. If this changes, the number 100.0 must be replaced.
        
        py.plot(py.array(countsund)/factor,alpha=1.0,color='k')
        py.plot(py.array(countspro)/factor,alpha=1.0,color='r')
        py.plot(py.array(countsagainst)/factor,alpha=1.0,color='b')
        py.ylim([-0.05,1.05])
        py.legend(['Moderate O=0','Oriented O=+1','Oriented O=-1'])
        #py.title('Opiniones')
        py.ylabel('Proportion of Agents with O')
        py.xlabel('Temporal Steps')
        
        #we only used two values of N for the plots of the paper:
        if N==100:
            py.xlim([0,1105])
        else:
            py.xlim([0,105])
            
        py.savefig('D:\\Doctorado\\Paper Argumentos\\Review\\'+'opinionesmoderadozona2g2.svg', bbox_inches='tight') 
        
        
def plottingopinionswitherrors(a,N,tipo):       
        '''This function does the same as the one before, but it adds shaded error regions to the plots. Only
        the new lines are commented. The new "tipo" variable is used for saving the plot. "consenso1" saves oriented positive consensus.
        "consensus2" saves oriented negative consensus. Any other string saves moderate consensus. This function was used for making
        some of the plots in Figure 3 (the second column).'''
            
        import pylab as py 
        import numpy as np
             
        countsund=a[0]
        countspro=a[1]
        countsagainst=a[2] 
        
        #We will also need the errors. For this, we use the last three variables returned by gettingopinionsevolutions:
        copias0=np.array(np.transpose(a[3]))
        copiaspos=np.array(np.transpose(a[4]))
        copiasneg=np.array(np.transpose(a[5]))
        
        serrors0=[]
        serrorspos=[]
        serrorsneg=[]
                
        for i in range(len(copias0)):
            serrors0.append(np.std(copias0[i])/float(np.sqrt(100))/float(N))
            serrorspos.append(np.std(copiaspos[i])/float(np.sqrt(100))/float(N))
            serrorsneg.append(np.std(copiasneg[i])/float(np.sqrt(100))/float(N))

        #This way we got the errors we needed
        
        py.figure()    
        factor=N*100.0
        
        py.plot(py.array(countsund)/factor,alpha=1.0,color='k')
        #We also plot the shaded regions:
        py.fill_between(range(len(py.array(countsund)/factor)),py.array(countsund)/factor-serrors0, py.array(countsund)/factor+serrors0,alpha=0.5,facecolor='k')
        
        #The same for both cases of oriented consensus:
        py.plot(py.array(countspro)/factor,alpha=1.0,color='r')
        py.fill_between(range(len(py.array(countspro)/factor)),py.array(countspro)/factor-serrorspos, py.array(countspro)/factor+serrorspos,alpha=0.5,facecolor='r')
        py.plot(py.array(countsagainst)/factor,alpha=1.0,color='b')
        py.fill_between(range(len(py.array(countsagainst)/factor)),py.array(countsagainst)/factor-serrorsneg, py.array(countsagainst)/factor+serrorsneg,alpha=0.5,facecolor='b')        

       
        if N==10:
            py.xlim([0,101])
        else:
            py.xlim([0,1001])
        
        py.ylim([-0.05,1.05])
        
        #Saving plot commands; changing directory is necessary for use in other computers.
        if tipo=='consenso1':
            py.savefig('D:\\Doctorado\\Paper Argumentos\\Review\\'+'PROBANDOCONERRORopinionesconsenso1.svg', bbox_inches='tight')
        elif tipo=='consenso2':
            py.savefig('D:\\Doctorado\\Paper Argumentos\\Review\\'+'PROBANDOCONERRORopinionesconsenso2.svg', bbox_inches='tight')            
        else:
            py.savefig('D:\\Doctorado\\Paper Argumentos\\Review\\'+'PROBANDOCONERRORopinionesindecisozona2.svg', bbox_inches='tight')