def gettingopinionsevolutions(N=10):        
        '''This function is used for generating the input for plottingopinions. Choose the appropriate N, and change the code to choose which
        state you are looking for.'''                              
        import numpy as np
        
        #initializations
        countsund=np.array([0 for i in range(6001)]) #this last number is related to the number of steps to use in newrunargsim. It must be steps+1.
        countspro=np.array([0 for i in range(6001)])
        countsagainst=np.array([0 for i in range(6001)])

        i=0
        
        from newrunargsim import newrunargsim #using newrunargsimforprofiling is also possible, but here we can choose the necessary steps.
        
        while i<100: #this is the number of copies one wishes to have, that end in the chosen final state. For example, 100 copies of moderate state.
            a=newrunargsim(60,30,N,6,6000,'no','no',0,1.0,3.0,'Bid') #note the number of steps.
            
            if a[0][-1]==N: #this is key for selecting the final state. If the first index is 0 (as it is now) it will be moderate. If it is 1,
                #it will be oriented consensus to O=1. If it is 2, it will be oriented consensus to O=-1. If there is confirmation bias (we are
                #not using it here, as seen in the first "no"), 3 will be bipolarization.
                countsund+=np.array(a[0])
                countspro+=np.array(a[1])
                countsagainst+=np.array(a[2])  
                i+=1       
        
        return countsund,countspro,countsagainst

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
        
        py.plot(py.array(countsund)/N,alpha=1.0,color='k')
        py.plot(py.array(countspro)/N,alpha=1.0,color='r')
        py.plot(py.array(countsagainst)/N,alpha=1.0,color='b')
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