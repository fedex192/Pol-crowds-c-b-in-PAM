# -*- coding: utf-8 -*-
'''This file contains functions for making almost all of the plots used for the different figures of the paper. The exceptions are: 
Figure 3, Figure 2 b) and c), and Figure 6. code for those plots are found in files "plottingopinions.py" (Figure 3 column 2), 
"plottingarguments.py" (Figure 3 column 1, Figure 2 b) and c)), "PCBSimulation.py" (Figure 6 a)) and "ContraryFluxSimulation.py" (Figure 6 b)). 
In most of these functions, there is commented code near the beginning, which was used for loading the files resulting from the explorations,
and saving the results in an useful way for plotting; this was done via the functions of the file "newcollectdata.py". The process of 
loading the data is time-consuming, and it is not necessary to do it every time one wishes to run one of this functions. Instead, the 
commented code can be used to do it once, and then those compiled results are saved, and then from that moment on, one only needs to load 
the compiled results. That is why that code is commented, but was left there for easy access.'''

#First, select the proper directory
import os
os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
#os.chdir('C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\') 


def analyzingargsimphasediagram(homo=4,cb='no'):
    '''This is the main plotting function. We will make thorough comments for this one, and then omit them for the rest of the functions
    (except for new code or changes).'''
    
    #Import useful libraries:   
    import copy
    import numpy as np
    import pylab as py
    from loading import loadinggeneric #this function can load compiled exploration results.
    import matplotlib as mpl    

    numens=1000 #the number of copies used.
    
    #The following commented code can be use to load, restructure, and save the exploration results. Since doing the loading and
    #restructuring directly from the saved exploration files is very time consuming, using this once and producing a compilation
    #of the results with the proper structure is the most efficient way to procede.
    
    # homo=4 #select the homophily parameter
    # from saving import savinggeneric #import the saving function for saving the restructured data
    # from newcollectdata import newcollectargsimdataconvergente #import the function that loads and reestructures results.
    # alldata=newcollectargsimdataconvergente(homo,'no') #use that function. The second variable is cb (='yes' if it is present, ='no' if it's not).
    # plotting=[alldata[0],alldata[1],alldata[2],alldata[6]]  #choose which variables you wish to keep for plotting. See the used function for description of which is which.
    # savinggeneric(plotting,'sinCBconvergente'+'homo'+str(homo),'D:\\Doctorado\\Simulation_Functions\\') #save results. The first input is the variable, the second is the file name, the thirs is the directory.
    
    #Choose the colors to be used for plotting. These were used for making the fifth kind of plots, which are the once used for the paper.
    colors = [[0,120/255.0,255/255.0,150/255.0], [215/255.0,50/255.0,0/255.0,240/255.0], [0/255.0,155/255.0,0/255.0,220/255.0], [0/255.0,155/255.0,0/255.0,110/255.0]]
    cmap = mpl.colors.ListedColormap(colors) #Create a colormap with those colors  
    
    #Having done once the process in the commented code, we now have a saved file with all the restructured results. Now we load them:
    if cb=='no':
        plotting=loadinggeneric('sinCB'+'homo'+str(homo),'D:\\Doctorado\\Simulation_Functions\\')                              
    elif cb=='yes':
        plotting=loadinggeneric('conCB'+'homo'+str(homo),'D:\\Doctorado\\Simulation_Functions\\')            
          
        
    #Now on to plotting. The first 4 plots are probability plots: we plot the probability of a given final state (e.g. moderate consensus)
    #in every point of parameter space. The fifth plot determines the regions where a specific state is likelier than all the others. This
    #plot uses only as many colors as final states, and is the kind used for Figures 2, 4, 5,and 7, in the paper. Figure 5 also included a
    #plot similar to these, which was made by a subsequent function on this file. 
    for j in range(len(plotting)+1):            
        py.figure()
        if (j==2 and cb=='no' and homo<3) or (j==3): #this makes some plots with the appropriate scale to see them, that would otherwise not be seen. 
            py.imshow(np.array(plotting[j]),aspect='auto',vmin=0, vmax=numens/10)
        elif j==4: #this is the code for the fifth plot
            
                newplotting2=copy.deepcopy(plotting[0]) #first, we copy the structure of the probability of finding moderate consensus.
                for iii in range(len(plotting[0])):
                    for jjj in range(len(plotting[0][0])): #now, for each point in space parameter, we check which state is more probable, and assign a specific color for each one
                        if plotting[0][iii][jjj]>plotting[1][iii][jjj] and plotting[0][iii][jjj]>plotting[2][iii][jjj] and plotting[0][iii][jjj]>plotting[3][iii][jjj]:
                            newplotting2[iii][jjj]=0 #color for moderate consensus will be assigned to 0
                        elif plotting[1][iii][jjj]>plotting[0][iii][jjj] and plotting[1][iii][jjj]>plotting[2][iii][jjj] and plotting[1][iii][jjj]>plotting[3][iii][jjj]:
                            newplotting2[iii][jjj]=1 #color for oriented consensus will be assigned to 1                            
                        elif plotting[2][iii][jjj]>plotting[0][iii][jjj] and plotting[2][iii][jjj]>plotting[1][iii][jjj] and plotting[2][iii][jjj]>plotting[3][iii][jjj]:
                            newplotting2[iii][jjj]=2 #color for bipolarization will be assigned to 0          
                        else:
                            newplotting2[iii][jjj]=3 #color metastable states or oscillations will be assigned to 3.
                py.imshow(newplotting2,aspect='auto',vmin=0, vmax=3, cmap=cmap) #plot using the colormap previously created.               
        else:
            py.imshow(np.array(plotting[j]),aspect='auto',vmin=0, vmax=numens) #this makes the first four plots, which are:
            #1) Probability of moderate consensus final state.
            #2) Probability of oriented consensus (of either type) final state.
            #3) Probability of bipolarization
            #4) Probability of oscillations or metastable states. When homophily increases, bipolarization states take an increasingly
            #long time to break and lead to consensus (in cases where the final state would be consensus and not bipolarization if enough
            #time passes by). However, this metastable bipolarization states can also stabilize and lead to bipolarization. Coincidentally, 
            #when homophily increases, probability of oscillations decreases (and it is already very low for homo=0), so all cases in 
            #this variable correspond to metastable bipolarization states for homo=2 or higher. This metastable bipolarization states 
            #were taken into consideration in Figure 7 of the paper.      
        
        #ticks and limits. Note: if you don't run this, the y axis will look inverted. 
        #This is the most important part of making a proper plot. IF you do not set this right, the plot will look off or deceiving.
        ax=py.gca()  
        py.xticks(np.arange(0,91,30),size=16)               
        ax.xaxis.set_ticklabels(range(10,101,30))
        py.yticks(np.arange(0,46,15),size=16)             
        ax.yaxis.set_ticklabels(range(10,101,30))      
        py.ylim([-0.5,45.5])
        py.xlim([-0.5,90.5])

        #axes labels
        py.xlabel(u'N',size=16)
        py.ylabel(u'$N_{A}$',size=16)
        
        #include a colorbar
        C=py.colorbar()    
        for l in C.ax.yaxis.get_ticklabels():
            l.set_size(14)    
        
        #Now we save the resulting Figures. 
        import os
        elviejo=os.getcwd()
        os.chdir('D:\\Doctorado\\Simulation_Functions\\') #select the directory you wish to use for saving the figure files
        
        if cb=='no':
                if j==0:
                    py.savefig('01 - PCM sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==1:
                    py.savefig('02 - PCO sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==2:
                    py.savefig(u'03 - PBip sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==3:
                    py.savefig(u'04 - Posc sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==4:
                    py.savefig(u'05 - Regiones sin CB '+'- Homo '+str(homo)+'.svg', bbox_inches='tight') #changing extension changes file type                         
                os.chdir(elviejo) #go back to the original directory set at the beginning of the file
        elif cb=='yes':            
                if j==0:
                    py.savefig('06 - PCM con CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==1:
                    py.savefig('07 - PCO con CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==2:
                    py.savefig(u'08 - PBip con CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==3:
                    py.savefig(u'09 - Posc con CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==4:
                    py.savefig(u'10 - Regiones con CB '+'- Homo '+str(homo)+'.svg', bbox_inches='tight')                             
                os.chdir(elviejo) #go back to the original directory set at the beginning of the file                         
        
                                      
def analyzingargsimphasediagramMayPops():
    '''This function is very similar to the one preceding it, but the kind of plots it makes is different. It was used for making the 
    plot of Figure 5 b). Since most of the code is the same (it is actually much simpler), we will only comment the new lines of code.
    We originally had some extra code used for removing the region of moderate consensus (as seen in Figure 5 b), but we lost that code,
    so it will not be included here. Some editing with Inkscape was necessary to completely remove that region. With this code, the entire
    plot will be shown, including the region we removed for the paper.'''  

    import numpy as np
    import pylab as py
    
    #As before, commented lines to load and restructure saved data. This time we use another function for collecting data, which
    #we used to load saved data from a previous exploration that did not consider the possibility of including homophily. This was
    #easier for us since we already had these functions from before we considered the inclusion of the homophily parameter and modified
    #our functions accordingly. Results are the same, since this is essentially the case for cb='yes' and homo=0.
    
    
    # cb='yes' #we only used this for this particular case with confirmation bias, and without homophily.
    # numens=1000
    # from newcollectdata import collectargsimdata
    # alldata=collectargsimdata(numens,cb)
    # plotting=[alldata[0],alldata[1],alldata[2],alldata[3],alldata[4],alldata[5],alldata[6]]  
    # from saving import savinggeneric
    # if cb=='no':
    #     savinggeneric(plotting,'sinCB')     
    # else:
    # savinggeneric(plotting,'conCBpoblsmay')
       
    from loading import loadinggeneric    
    plotting=loadinggeneric('conCBpoblsmay','D:\\Doctorado\\Simulation_Functions\\')    
             
    py.figure()
        
    py.imshow(np.array(plotting[-1]),aspect='auto',vmin=0.5, vmax=0.75) #this time, we only need one plot.

    ax=py.gca() 
    py.xticks(np.arange(0,91,30),size=16)               
    ax.xaxis.set_ticklabels(range(10,101,30)) 
    py.yticks(np.arange(0,46,15),size=16)             
    ax.yaxis.set_ticklabels(range(10,101,30))      
    py.ylim([-0.5,45.5]) #arranca en 10
    py.xlim([-0.5,90.5]) #arranca en 10

    py.xlabel(u'N',size=16)
    py.ylabel(u'$N_{A}$',size=16)
    
    C=py.colorbar()    
    for l in C.ax.yaxis.get_ticklabels():
        l.set_size(14) 
        
    import os
    elviejo=os.getcwd()
    os.chdir('C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')    
    py.savefig('11 - Pobl May con CB '+'original.svg', bbox_inches='tight')
    os.chdir(elviejo)          
                                                                                                                                
                                                                                                                    
def analyzingargsimphasediagramreview(homo=0,cb='no'):
    '''This function is very similar to the ones preceding it, but the kind of plots it makes is different. It was used for making the 
    plot of Figure 4. We will only comment the new lines.'''
    import numpy as np
    import pylab as py
    import copy
    from loading import loadinggeneric
    import matplotlib as mpl    

    
    homo=0
    
    #Once again, commented code to be run only once:
    #numens=1000
    #from saving import savinggeneric    
    #from newcollectdata import newcollectargsimdatareview2
    #alldataraw=newcollectargsimdatareview2(homo,'no')
    #savinggeneric(alldataraw,'BarridoFino','D:\\Doctorado\\Simulation_Functions\\') 
     
    alldataraw=loadinggeneric('BarridoFino') #we changed the name to "alldataraw" in case we accidentally deleted alldata, used later.
    deltaswho=alldataraw[7] #all values N_A/N = delta explored for this.
            
    colors = [[0,120/255.0,255/255.0,150/255.0], [215/255.0,50/255.0,0/255.0,240/255.0], [0/255.0,155/255.0,0/255.0,220/255.0], [0/255.0,155/255.0,0/255.0,110/255.0],[0,0,0,0]]
    cmap = mpl.colors.ListedColormap(colors)    
    
    #In order to correctly make plots similar to the ones made for Figures 2, 5, and 7, we had to use bins, to account for differently
    #spaced values of N_A/N. For example, for N_A/N >=6, the only possible values found by using N_A in range [10,100] in steps of 2, 
    #and N in range [10,100], are 6, 7, 8, 9, and 10 (with no other values in between). We only plotted from the samllest value (0.1) to
    #N_A/N = 7, but this required not only to use bins grouping a set of close values together (similar to averaging windows), but we
    #also required to fill in some missing values in those windows, which we did by nearest neighbors aproximations. The following code
    #was used for this.
    
    factordebineado=0.05  #Size of bins. Smaller is possible, but the bound of the regions becomes noisier.
        
    #initialization    
    alldata=[[[0 for j in range(len(np.arange(0,10.1,factordebineado)))] for i in range(6,51,2)] for k in range(4)]
    
    for i in range(len(range(6,51,2))): #for every possible value of M
        
        counters=[0.0 for rrrr in range(len(np.arange(0,10.1,factordebineado)))]#initialization of counters of how many values are in the bins.

        for j in range(len(deltaswho)): #for each possible value of delta=N_A/N we got
            flag=0
            k=0
            while flag==0: #we use this to check in which bin that delta is located
                if deltaswho[j]>=factordebineado*k+0.1 and deltaswho[j]<factordebineado*k+factordebineado+0.1: #if we found it
                    flag=1
                    if not np.isnan(alldataraw[0][i][j]): #if it is not a nan value, assigned to the region where M>=N_A
                        alldata[0][i][k]+=alldataraw[0][i][j]
                        alldata[1][i][k]+=alldataraw[1][i][j]
                        alldata[2][i][k]+=alldataraw[2][i][j]
                        alldata[3][i][k]+=alldataraw[6][i][j]
                        counters[k]+=1.0        
                k+=1
                
                if k>1001: #this catches odd cases. It was used for debugging.
                    flag=1
                                        
                
        if 0.0 in counters: #if there were bins without any value inside them.
            for l in range(len(counters)):
                if counters[l]==0.0: #if there were no values in this bin
                    if l!=0: #if it is not the first bin
                        if l!=len(counters)-1: #if it is not the last bin
                            #we approximate its value as the mean of the values of this bins neighbors
                            alldata[0][i][l]=(alldata[0][i][l-1]+alldata[0][i][l+1])/2.0
                            alldata[1][i][l]=(alldata[1][i][l-1]+alldata[1][i][l+1])/2.0
                            alldata[2][i][l]=(alldata[2][i][l-1]+alldata[2][i][l+1])/2.0
                            alldata[3][i][l]=(alldata[3][i][l-1]+alldata[3][i][l+1])/2.0
                            counters[l]=(counters[l-1]+counters[l+1])/2
                        else: #if it is the last bin, we approximate its value by using the previous bin.
                            alldata[0][i][l]=alldata[0][i][l-1]
                            alldata[1][i][l]=alldata[1][i][l-1]
                            alldata[2][i][l]=alldata[2][i][l-1]
                            alldata[3][i][l]=alldata[3][i][l-1]
                            counters[l]=counters[l-1]                                                                                   
                    else: #if it is the first bin, we approximate its value by using the next bin.                      
                        alldata[0][i][l]=alldata[0][i][l+1]
                        alldata[1][i][l]=alldata[1][i][l+1]
                        alldata[2][i][l]=alldata[2][i][l+1]
                        alldata[3][i][l]=alldata[3][i][l+1]
                        counters[l]=counters[l+1]             
                
        #we  divide the values of the bins by how many delta values fell in them:        
        alldata[0][i]=list(np.array(alldata[0][i])/np.array(counters))
        alldata[1][i]=list(np.array(alldata[1][i])/np.array(counters))
        alldata[2][i]=list(np.array(alldata[2][i])/np.array(counters))
        alldata[3][i]=list(np.array(alldata[3][i])/np.array(counters))
    
    plotting=[alldata[0],alldata[1],alldata[2],alldata[3]] #we are ready for making the plots 
   
    #The only kind of plot we are interested in here is the one which uses colors for the regions where one state is likelier than the rest.
    #We omit the other plots.
    for j in [4]: #we only did this so that we did not need to reindent all the code below.       
        py.figure()
#        if N==10 or N==20 or N==50:            
        if j==4:      
                newplotting2=copy.deepcopy(plotting[0])
                for iii in range(len(plotting[0])):
                    for jjj in range(len(plotting[0][0])):
                        if plotting[0][iii][jjj]>plotting[1][iii][jjj] and plotting[0][iii][jjj]>plotting[2][iii][jjj] and plotting[0][iii][jjj]>plotting[3][iii][jjj]:
                            newplotting2[iii][jjj]=0
                        elif plotting[1][iii][jjj]>plotting[0][iii][jjj] and plotting[1][iii][jjj]>plotting[2][iii][jjj] and plotting[1][iii][jjj]>plotting[3][iii][jjj]:
                            newplotting2[iii][jjj]=1                            
                        elif plotting[2][iii][jjj]>plotting[0][iii][jjj] and plotting[2][iii][jjj]>plotting[1][iii][jjj] and plotting[2][iii][jjj]>plotting[3][iii][jjj]:
                            newplotting2[iii][jjj]=2          
                        else:
                            newplotting2[iii][jjj]=3    
                        if np.isnan(plotting[1][iii][jjj]):
                            newplotting2[iii][jjj]=4
                py.imshow(newplotting2,aspect='auto',vmin=0, vmax=4, cmap=cmap)  

        
        py.ylim([-0.5,22.5])
        ax=py.gca()  
        if factordebineado==0.01: #other possible value we tested.
            py.xlim([0,710])
            xmax=710
        elif factordebineado==0.05:
            py.xlim([0,142])      
            xmax=142       
        py.yticks(np.arange(2,23,20/4.0),size=16)    
        py.xticks([20.2,60.6,101,142],size=16) #this was optimized for factordebineado=0.05. It must be changed for other values.                       
        ax.xaxis.set_ticklabels([1,3,5,7])      
        ax.yaxis.set_ticklabels(range(10,51,10)) 
        
        py.xlabel(u'$N_A/N$',size=16)
        py.ylabel(u'M',size=16)
        
        C=py.colorbar()    
        for l in C.ax.yaxis.get_ticklabels():
            l.set_size(14)    
                           
                                                               
        import os
        elviejo=os.getcwd()
        os.chdir('D:\\Doctorado\\Simulation_Functions\\')
        py.savefig(u'05 - Regiones sin CB Reviewer '+'- Homo '+str(homo)+'.svg', bbox_inches='tight')                             
        os.chdir(elviejo)