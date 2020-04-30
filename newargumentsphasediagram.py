# -*- coding: utf-8 -*-
import os
os.chdir('D:\\Doctorado\\Simulation_Functions\\') 
#os.chdir('C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\') 

def analyzingargsimphasediagram3(homo=4,tipo='convergente',cb='no'):
    import numpy as np
    import pylab as py
    import copy
    from loading import loadinggeneric
    import matplotlib.pyplot as plt
    import matplotlib as mpl    

    numens=1000
    # homo=4
    # from saving import savinggeneric    
    # from newcollectdata import newcollectargsimdataconvergente
    # alldata=newcollectargsimdataconvergente(homo,'no')
    # plotting=[alldata[0],alldata[1],alldata[2],alldata[6]]  
    # # savinggeneric(plotting,'sinCBconvergente'+'homo'+str(homo),'D:\\Doctorado\\Simulation_Functions\\')     
    # savinggeneric(plotting,'sinCBconvergente'+'homo'+str(homo),'C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')     
    # 
    colors = [[0,120/255.0,255/255.0,150/255.0], [215/255.0,50/255.0,0/255.0,240/255.0], [0/255.0,155/255.0,0/255.0,220/255.0], [0/255.0,155/255.0,0/255.0,110/255.0]]
    bounds = [0,1,2]

    cmap = mpl.colors.ListedColormap(colors)    
    
    #plotting=loadinggeneric('sinCB'+tipo+'homo'+str(homo),'D:\\Doctorado\\Simulation_Functions\\')    
    if cb=='no':
        #plotting=loadinggeneric('sinCB'+tipo+'homo'+str(homo),'C:\\Users\\Fede\\Desktop\\Simulation_Functions\\')     
        plotting=loadinggeneric('sinCB'+tipo+'homo'+str(homo),'D:\\Doctorado\\Simulation_Functions\\') 
        #plotting=loadinggeneric('sinCB'+tipo+'homo'+str(homo),'C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')         
                              
    elif cb=='yes':
        #plotting=loadinggeneric('conCB'+tipo+'homo'+str(homo),'C:\\Users\\Fede\\Desktop\\Simulation_Functions\\')   
        plotting=loadinggeneric('conCB'+tipo+'homo'+str(homo),'D:\\Doctorado\\Simulation_Functions\\')            
        #plotting=loadinggeneric('conCB'+tipo+'homo'+str(homo),'C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')            
          
        
 
   
    for j in range(len(plotting)+1):            
        py.figure()
#        if N==10 or N==20 or N==50:            
        if (j==2 and cb=='no' and homo<3) or (j==3 and tipo==''):      
            py.imshow(np.array(plotting[j]),aspect='auto',vmin=0, vmax=numens/10)#,extent=[0,1,1,0])
        elif j==3 and tipo=='convergente':
            py.imshow(np.array(plotting[j]),aspect='auto',vmin=0)
        elif j==4:
            
                newplotting2=plotting[0]
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
                py.imshow(newplotting2,aspect='auto',vmin=0, vmax=3, cmap=cmap)                 
        else:
            py.imshow(np.array(plotting[j]),aspect='auto',vmin=0, vmax=numens)
            
        ax=py.gca()  
        
        if tipo=='':
            py.ylim([-0.5,16.5])
            py.xticks(np.arange(0,20,2),size=16)               
            ax.xaxis.set_ticklabels(range(10,101,10)) #Cambiar ini por 4 y paso por 10 para arrancar en 4; ini por 6, paso por 12 para arrancar en 6.
            py.yticks(np.arange(0.85,17,1.7),size=16)             
            ax.yaxis.set_ticklabels(range(10,101,10))              
            
            
        else:

            py.xticks(np.arange(0,91,30),size=16)               
            ax.xaxis.set_ticklabels(range(10,101,30)) #Cambiar ini por 4 y paso por 10 para arrancar en 4; ini por 6, paso por 12 para arrancar en 6.
            py.yticks(np.arange(0,46,15),size=16)             
            ax.yaxis.set_ticklabels(range(10,101,30))      
            py.ylim([-0.5,45.5]) #arranca en 10
            py.xlim([-0.5,90.5]) #arranca en 10
#        else:
#            py.imshow(np.array(plotting[j]),vmax=1)#aspect='auto',vmin=0,vmax=1,extent=[0,1,1,0]) 
#            py.xlim([0,100])
#            py.ylim([0,100])
        py.xlabel(u'N',size=16)
        py.ylabel(u'$N_{Ars}$',size=16)
        C=py.colorbar()    
        for l in C.ax.yaxis.get_ticklabels():
            l.set_size(14)    
                           
                                                               
#        py.xlim([1,97]) #Si quiero plotear desde 4, arrancar en -1. Para hacerlo desde 6, es en 1, tics hasta 99.
        # py.ylim([2,47.5]) #arranca en 10
        # py.xlim([5,96.5]) #arranca en 10

#        else:
#            py.imshow(np.array(plotting[j]),vmax=1)#aspect='auto',vmin=0,vmax=1,extent=[0,1,1,0]) 
#            py.xlim([0,100])
#            py.ylim([0,100])

        #ax.locator_params(nbins=10) #nticks=nbins/2
#        py.minorticks_on()
        #ax.xaxis.set_ticklabels(range(6,103,12)) #Cambiar ini por 4 y paso por 10 para arrancar en 4; ini por 6, paso por 12 para arrancar en 6.
        #ax.yaxis.set_ticklabels(range(6,103,12))
  
        
        ax.tick_params(axis='y',which='minor',left='off')
        #if N==20:
        #    py.colorbar(ticks=range(0,21,4))
        #else:
        #    py.colorbar()
        import os
        elviejo=os.getcwd()
        os.chdir('D:\\Doctorado\\Simulation_Functions\\')
        #os.chdir('C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')
        
        if tipo=='convergente':
            if cb=='no':
                if j==0:
                    #py.title('Probabilidad de Hallar Consenso Moderado',size=18)
                    py.savefig('01 - PCM sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==1:
                    #py.title('Probabilidad de Hallar Consenso Orientado',size=18)
                    py.savefig('02 - PCO sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==2:
                #py.title(u'Probabilidad de Hallar Bipolarización',size=18)   
                    py.savefig(u'03 - PBip sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==3:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'04 - Posc sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==4:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'05 - Regiones sin CB '+'- Homo '+str(homo)+'.svg', bbox_inches='tight')                             
                os.chdir(elviejo)
            elif cb=='yes':            
                if j==0:
                    #py.title('Probabilidad de Hallar Consenso Moderado',size=18)
                    py.savefig('06 - PCM con CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==1:
                    #py.title('Probabilidad de Hallar Consenso Orientado',size=18)
                    py.savefig('07 - PCO con CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==2:
                #py.title(u'Probabilidad de Hallar Bipolarización',size=18)   
                    py.savefig(u'08 - PBip con CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==3:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'09 - Posc con CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==4:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'10 - Regiones con CB '+'- Homo '+str(homo)+'.svg', bbox_inches='tight')                             
                os.chdir(elviejo)
                
        if tipo=='':
            if cb=='no':
                if j==0:
                    #py.title('Probabilidad de Hallar Consenso Moderado',size=18)
                    py.savefig('01 - PCM sin CB - Homo '+str(homo)+'limitado.png', bbox_inches='tight')
                elif j==1:
                    #py.title('Probabilidad de Hallar Consenso Orientado',size=18)
                    py.savefig('02 - PCO sin CB - Homo '+str(homo)+'limitado.png', bbox_inches='tight')
                elif j==2:
                #py.title(u'Probabilidad de Hallar Bipolarización',size=18)   
                    py.savefig(u'03 - PBip sin CB - Homo '+str(homo)+'limitado.png', bbox_inches='tight')
                elif j==3:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'04 - Posc sin CB - Homo '+str(homo)+'limitado.png', bbox_inches='tight')
                elif j==4:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'05 - Regiones sin CB '+'- Homo '+str(homo)+'.svg', bbox_inches='tight')                         
                os.chdir(elviejo)
            elif cb=='yes':            
                if j==0:
                    #py.title('Probabilidad de Hallar Consenso Moderado',size=18)
                    py.savefig('06 - PCM con CB - Homo '+str(homo)+'limitado.png', bbox_inches='tight')
                elif j==1:
                    #py.title('Probabilidad de Hallar Consenso Orientado',size=18)
                    py.savefig('07 - PCO con CB - Homo '+str(homo)+'limitado.png', bbox_inches='tight')
                elif j==2:
                #py.title(u'Probabilidad de Hallar Bipolarización',size=18)   
                    py.savefig(u'08 - PBip con CB - Homo '+str(homo)+'limitado.png', bbox_inches='tight')
                elif j==3:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'09 - Posc con CB - Homo '+str(homo)+'limitado.png', bbox_inches='tight')
                elif j==4:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'10 - Regiones con CB '+'- Homo '+str(homo)+'.svg', bbox_inches='tight')                
                os.chdir(elviejo)                                        
                
                
def analyzingargsimphasediagram3old(cb='no'):
    numens=1000
    import numpy as np
    import pylab as py
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    colors = [[0,120/255.0,255/255.0,150/255.0], [215/255.0,50/255.0,0/255.0,240/255.0], [0/255.0,155/255.0,0/255.0,220/255.0]]
    bounds = [0,1,2]

    cmap = mpl.colors.ListedColormap(colors)
    #norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    import copy
    from loading import loadinggeneric
    # if numens==1000:
    #     from collectdata import collectargsimdata
    #     alldata=collectargsimdata(numens,cb)
    # plotting=[alldata[0],alldata[1],alldata[2],alldata[3]]  
    # from saving import savinggeneric
    # if cb=='no':
    #     savinggeneric(plotting,'sinCB')     
    # else:
    #     savinggeneric(plotting,'conCB')   
        
    if cb=='no':        
        plotting=loadinggeneric('sinCB')      
    else:
        plotting=loadinggeneric('conCB')      
   
    for j in range(len(plotting)+1):            
        py.figure()
#        if N==10 or N==20 or N==50:            
        if j==3:      
            py.imshow(np.array(plotting[j])/1000.0,aspect='auto',vmin=0, vmax=0.1)#,extent=[0,1,1,0])
        elif j==4:
            if cb=='no':
                newplotting=(np.array(plotting[1])>np.array(plotting[0])) #si gana el moderado es 0.
                py.imshow(newplotting,aspect='auto',vmin=0, vmax=2, cmap=cmap)
                
            else:
                newplotting2=plotting[0]
                for iii in range(len(plotting[0])):
                    for jjj in range(len(plotting[0][0])):
                        if plotting[0][iii][jjj]>plotting[1][iii][jjj] and plotting[0][iii][jjj]>plotting[2][iii][jjj]:
                            newplotting2[iii][jjj]=0
                        elif plotting[1][iii][jjj]>plotting[0][iii][jjj] and plotting[1][iii][jjj]>plotting[2][iii][jjj]:
                            newplotting2[iii][jjj]=1
                        else:
                            newplotting2[iii][jjj]=2          
                py.imshow(newplotting2,aspect='auto',vmin=0, vmax=2, cmap=cmap)                         
        else:
            py.imshow(np.array(plotting[j])/1000.0,aspect='auto',vmin=0, vmax=1)
#        py.ylim([0,48])
#        py.xlim([1,97]) #Si quiero plotear desde 4, arrancar en -1. Para hacerlo desde 6, es en 1, tics hasta 99.
        ax=py.gca() 

        py.xticks(np.arange(0,91,30),size=16)               
        ax.xaxis.set_ticklabels(range(10,101,30)) #Cambiar ini por 4 y paso por 10 para arrancar en 4; ini por 6, paso por 12 para arrancar en 6.
        py.yticks(np.arange(0,46,15),size=16)             
        ax.yaxis.set_ticklabels(range(10,101,30))      
        py.ylim([-0.5,45.5]) #arranca en 10
        py.xlim([-0.5,90.5]) #arranca en 10
#        else:
#            py.imshow(np.array(plotting[j]),vmax=1)#aspect='auto',vmin=0,vmax=1,extent=[0,1,1,0]) 
#            py.xlim([0,100])
#            py.ylim([0,100])
        py.xlabel(u'N',size=16)
        py.ylabel(u'$N_{Ars}$',size=16)
        C=py.colorbar()    
        for l in C.ax.yaxis.get_ticklabels():
            l.set_size(14)    
   
        #ax.locator_params(nbins=10) #nticks=nbins/2
        # py.minorticks_on()
        # py.yticks(range(2,49,5),size=18)
        # py.xticks(range(6,99,10),size=18) #Si quiero plotear desde 4, arrancar en 0. Para hacerlo desde 6, es en 2. A parte, para el caso de 4, el paso es de 10, y fin es 97. Caso 6: de 12, fin de 99.
        # #ax.xaxis.set_ticklabels(range(6,103,12)) #Cambiar ini por 4 y paso por 10 para arrancar en 4; ini por 6, paso por 12 para arrancar en 6.
        # #ax.yaxis.set_ticklabels(range(6,103,12))
        # ax.xaxis.set_ticklabels(range(10,101,10)) #Cambiar ini por 4 y paso por 10 para arrancar en 4; ini por 6, paso por 12 para arrancar en 6.
        # ax.yaxis.set_ticklabels(range(10,101,10))        
        
        # ax.tick_params(axis='y',which='minor',left='off')
        #if N==20:
        #    py.colorbar(ticks=range(0,21,4))
        #else:
        #    py.colorbar()
        
        
        
        
        
        import os
        elviejo=os.getcwd()
        os.chdir('D:\\Doctorado\\Simulation_Functions\\')
        if cb=='no':
                if j==0:
                    #py.title('Probabilidad de Hallar Consenso Moderado',size=18)
                    py.savefig('01 - PCM sin CB '+'original.svg', bbox_inches='tight')
                elif j==1:
                    #py.title('Probabilidad de Hallar Consenso Orientado',size=18)
                    py.savefig('02 - PCO sin CB '+'original.svg', bbox_inches='tight')
                elif j==2:
                #py.title(u'Probabilidad de Hallar Bipolarización',size=18)   
                    py.savefig(u'03 - PBip sin CB '+'original.svg', bbox_inches='tight')
                elif j==3:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'04 - Posc sin CB '+'original.svg', bbox_inches='tight')
                elif j==4:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'05 - Regiones sin CB '+'original.svg', bbox_inches='tight')                  
                os.chdir(elviejo)
        elif cb=='yes':            
                if j==0:
                    #py.title('Probabilidad de Hallar Consenso Moderado',size=18)
                    py.savefig('06 - PCM con CB '+'original.svg', bbox_inches='tight')
                elif j==1:
                    #py.title('Probabilidad de Hallar Consenso Orientado',size=18)
                    py.savefig('07 - PCO con CB '+'original.svg', bbox_inches='tight')
                elif j==2:
                #py.title(u'Probabilidad de Hallar Bipolarización',size=18)   
                    py.savefig(u'08 - PBip con CB '+'original.svg', bbox_inches='tight')
                elif j==3:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'09 - Posc con CB '+'original.svg', bbox_inches='tight')
                elif j==4:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'10 - Regiones con CB '+'original.svg', bbox_inches='tight')                          
        os.chdir(elviejo)  
        
def makerelarggraphswithoutCBBIDposta():
    import numpy as np
    import pylab as py
    vectors10=[(671, 169, 160, 0, 0, 58),(330, 339, 331, 0, 0, 2),(508, 235, 257, 0, 0, 71),(230, 406, 364, 0, 0, 0),
    (343, 336, 321, 0, 0, 69),(147, 445, 408, 0, 0, 2),(269, 384, 347, 0, 0, 52),(107, 426, 467, 0, 0, 0),
    (203, 396, 401, 0, 0, 49),(63, 484, 453, 0, 0, 0),(146, 418, 436, 0, 0, 32),(71, 444, 485, 0, 0, 1),
    (124, 458, 418, 0, 0, 29),(54, 491, 455, 0, 0, 0),(134, 418, 448, 0, 0, 41),(49, 483, 468, 0, 0, 0),
    (137, 427, 434, 0, 2, 48),(48, 477, 475, 0, 0, 0)]
    bip10=[]
    otros10=[]
    cons10=[]
    ind10=[]
    osc10=[]
    for i in range(len(vectors10)):
        bip10.append(vectors10[i][3])
        otros10.append(vectors10[i][4])
        cons10.append(vectors10[i][2]+vectors10[i][1])
        ind10.append(vectors10[i][0])
        osc10.append(vectors10[i][-1])

    rels=range(3,21)


    # py.figure()
    # py.ylabel(u'Fracción de Estados Finales',size=18)
    # py.xlabel(u'M',size=18)
    # py.xticks(range(4,21,2),size=18)
    # py.yticks(range(0,1001,200),size=18)
    # py.ylim([-1,1001])
    # ax=py.gca()
    # ax.yaxis.set_ticklabels(py.arange(0.0,1.01,0.2),size=18)
    # 
    # py.plot(rels,ind10,lw=4)
    # py.plot(rels,cons10,lw=4)
    # #py.plot(rels,bip10,lw=4)
    # #py.plot(rels,otros10,lw=4)
    # #py.plot(rels,osc10,'-.k',lw=4)
    # py.legend(['C. Moderado','C. Orientado',u'Bipolarización','Otros Estados','Oscilaciones'],prop={'size':16})
    # #py.title('N=10, Sin CB',size=18)
    # py.savefig(u'Rels N=10 Sin CB Bid.png', bbox_inches='tight') 
    
    py.figure()
    py.ylabel(u'Probability of Final States',size=16)
    py.xlabel(u'M',size=16)
    py.ylim([-10,1010])
    py.xticks(range(4,21,4),size=16)
    py.yticks(range(0,1001,200),size=16)
    ax=py.gca()
    ax.yaxis.set_ticklabels(py.arange(0.0,1.01,0.2),size=18)
    #py.plot([rels[i] for i in range(0,18,2)],[ind10[i] for i in range(0,18,2)],'-^',lw=1,color='k')   , 
    py.plot([rels[i] for i in range(1,18,2)],[ind10[i] for i in range(1,18,2)],'-^',lw=3,color=[0,120/255.0,255/255.0,150/255.0],MarkerSize=10)   
    #py.plot([rels[i] for i in range(0,18,2)],[cons10[i] for i in range(0,18,2)],'-o',lw=1,color='g')
    py.plot([rels[i] for i in range(1,18,2)],[cons10[i] for i in range(1,18,2)],'-o',lw=3,color=[215/255.0,50/255.0,0/255.0,240/255.0],MarkerSize=10)
#    py.plot([rels[i] for i in range(3,21,2)],[bip10[i] for i in range(3,21,2)],lw=4)
#    py.plot([rels[i] for i in range(3,21,2)],[otros10[i] for i in range(3,21,2)],lw=4)  
    #py.plot([rels[i] for i in range(0,18,2)],[ind10[i] for i in range(0,18,2)],'o',lw=4,color='k')
    #py.plot([rels[i] for i in range(1,18,2)],[ind10[i] for i in range(1,18,2)],'o',lw=4,color='r')
    #py.plot([rels[i] for i in range(0,18,2)],[cons10[i] for i in range(0,18,2)],'^',lw=4,color='k')
    #py.plot([rels[i] for i in range(1,18,2)],[cons10[i] for i in range(1,18,2)],'^',lw=4,color='r')
#    py.plot([rels[i] for i in range(3,21,2)],[osc10[i] for i in range(3,21,2)],'-.k',lw=4)
    py.legend(['Moderate Consensus','Oriented Consensus',],prop={'size':16})
    #py.title('N=10, Sin CB',size=18)
    py.savefig(u'Rels N=10 Sin CB Bid.svg', bbox_inches='tight')
    
    #py.figure()
    #py.ylabel(u'Nestf - N° de Estados Finales',size=18)
    #py.xlabel(u'Rels - N° de Argumentos Relevantes',size=18)
    #py.xticks(size=18)
    #py.yticks(size=18)
    #py.plot(rels,ind30,lw=4)
    #py.plot(rels,cons30,lw=4)
    #py.plot(rels,bip30,lw=4)
    #py.plot(rels,otros30,lw=4)
    #py.plot(rels,osc30,'-.k',lw=4)
    #py.legend(['C. Moderado','C. Orientado',u'Bipolarización','Otros Estados','Oscilaciones'],prop={'size':16})#,location='SouthWest')
    #py.title('N=30, Sin CB',size=18)
    #py.savefig(u'Rels N=30 Sin CB Bid.png', bbox_inches='tight') 
    ##py.xlim([0,51])
    #
    #py.figure()
    #py.ylabel(u'N - Número de Estados Finales')
    #py.xlabel(u'Rels - Cantidad de Argumentos Relevantes')
    #py.plot(rels,ind100,lw=4)
    #py.plot(rels,cons100,lw=4)
    #py.plot(rels,bip100,lw=4)
    #py.plot(rels,otros100,lw=4)
    #py.plot(rels,osc100,color='k',lw=4)
    #py.legend([u'Indecisión','Consenso',u'Bipolarización','Otros Estados','Oscilaciones'],loc=3)#,location='SouthWest')
    #py.title('N=100, Sin CB')
    
def makerelarggraphswithCBBIDposta():
    import numpy as np
    import pylab as py
    vectors10=[(715, 74, 67, 144, 0, 106),(284, 43, 63, 610, 0, 0),(524, 29, 29, 418, 0, 119),(113, 7, 17, 863, 0, 0),(255, 6, 6, 733, 0, 77),
    (26, 3, 2, 969, 0, 0),(105, 0, 3, 892, 0, 39),(5, 0, 3, 992, 0, 0),(44, 0, 1, 955, 0, 14),(2, 1, 0, 997, 0, 0),(19, 0, 1, 980, 0, 11),(2, 1, 0, 997, 0, 0),
    (10, 0, 1, 987, 2, 4),(0, 1, 1, 998, 0, 0),(5, 0, 1, 994, 0, 3),(0, 0, 0, 1000, 0, 0),(1, 0, 0, 998, 1, 1),(0, 0, 0, 999, 1, 0)]
    bip10=[]
    otros10=[]
    cons10=[]
    ind10=[]
    osc10=[]
    for i in range(len(vectors10)):
        bip10.append(vectors10[i][3])
        otros10.append(vectors10[i][4])
        cons10.append(vectors10[i][2]+vectors10[i][1])
        ind10.append(vectors10[i][0])
        osc10.append(vectors10[i][-1])

    rels=range(3,21)


    py.figure()
    py.ylabel(u'Fracción de Estados Finales',size=18)
    py.xlabel(u'M',size=18)
    py.xticks(range(4,21,2),size=18)
    py.plot(rels,ind10,lw=4,color='r')
    py.plot(rels,cons10,'b-.',lw=4,)
    py.plot(rels,bip10,lw=4,color='k')
    py.ylim([-10,1010])    
    py.yticks(range(0,1001,200),size=18)
    ax=py.gca()
    ax.yaxis.set_ticklabels(py.arange(0.0,1.01,0.2),size=18)
    #py.plot(rels,otros10,lw=4)
    #py.plot(rels,osc10,'-.k',lw=4)
    py.legend(['C. Moderado','C. Orientado',u'Bipolarización','Otros Estados','Oscilaciones'],prop={'size':16})
    #py.title('N=10, Sin CB',size=18)
    py.savefig(u'Rels N=10 Con CB Bid.png', bbox_inches='tight') 
    
    py.figure()
    py.ylabel(u'Fracción de Estados Finales',size=18)
    py.xlabel(u'M',size=18)
    py.xticks(range(4,21,2),size=18)
    py.yticks(size=18)
    py.ylim([-10,1010])    
    py.yticks(range(0,1001,200),size=18)
    ax=py.gca()
    ax.yaxis.set_ticklabels(py.arange(0.0,1.01,0.2),size=18)
    py.plot([rels[i] for i in range(0,18,2)],[ind10[i] for i in range(0,18,2)],'-^',lw=1,color='k')   
    py.plot([rels[i] for i in range(1,18,2)],[ind10[i] for i in range(1,18,2)],'-^',lw=1,color='r')   
    py.plot([rels[i] for i in range(0,18,2)],[cons10[i] for i in range(0,18,2)],'-o',lw=1,color='g')
    py.plot([rels[i] for i in range(1,18,2)],[cons10[i] for i in range(1,18,2)],'-o',lw=1,color='b')    
    
#    py.plot([rels[i] for i in range(0,18,2)],[ind10[i] for i in range(0,18,2)],'-.',lw=4)
#    py.plot([rels[i] for i in range(1,18,2)],[ind10[i] for i in range(1,18,2)],'-.',lw=4)
#    py.plot([rels[i] for i in range(0,18,2)],[cons10[i] for i in range(0,18,2)],'-.',lw=4)
##    py.plot([rels[i] for i in range(3,21,2)],[bip10[i] for i in range(3,21,2)],lw=4)
##    py.plot([rels[i] for i in range(3,21,2)],[otros10[i] for i in range(3,21,2)],lw=4)
#
#    py.plot([rels[i] for i in range(1,18,2)],[cons10[i] for i in range(1,18,2)],'-.',lw=1)
    py.plot([rels[i] for i in range(0,18,2)],[bip10[i] for i in range(0,18,2)],'-.',lw=1,color='k')
    py.plot([rels[i] for i in range(1,18,2)],[bip10[i] for i in range(1,18,2)],'-.',lw=1,color='r')
#    py.plot([rels[i] for i in range(3,21,2)],[osc10[i] for i in range(3,21,2)],'-.k',lw=4)
    py.legend(['C. Moderado M Impar','C. Moderado M Par','C. Orientado M Impar','C. Orientado M Par',u'Bipolarización M Impar',u'Bipolarización M Par'],prop={'size':16})
    #py.title('N=10, Sin CB',size=18)
    py.savefig(u'Rels N=10 Con CB Bid Pares e Impares.png', bbox_inches='tight')
    
    #py.figure()
    #py.ylabel(u'Nestf - N° de Estados Finales',size=18)
    #py.xlabel(u'Rels - N° de Argumentos Relevantes',size=18)
    #py.xticks(size=18)
    #py.yticks(size=18)
    #py.plot(rels,ind30,lw=4)
    #py.plot(rels,cons30,lw=4)
    #py.plot(rels,bip30,lw=4)
    #py.plot(rels,otros30,lw=4)
    #py.plot(rels,osc30,'-.k',lw=4)
    #py.legend(['C. Moderado','C. Orientado',u'Bipolarización','Otros Estados','Oscilaciones'],prop={'size':16})#,location='SouthWest')
    #py.title('N=30, Sin CB',size=18)
    #py.savefig(u'Rels N=30 Sin CB Bid.png', bbox_inches='tight') 
    ##py.xlim([0,51])
    #
    #py.figure()
    #py.ylabel(u'N - Número de Estados Finales')
    #py.xlabel(u'Rels - Cantidad de Argumentos Relevantes')
    #py.plot(rels,ind100,lw=4)
    #py.plot(rels,cons100,lw=4)
    #py.plot(rels,bip100,lw=4)
    #py.plot(rels,otros100,lw=4)
    #py.plot(rels,osc100,color='k',lw=4)
    #py.legend([u'Indecisión','Consenso',u'Bipolarización','Otros Estados','Oscilaciones'],loc=3)#,location='SouthWest')
    #py.title('N=100, Sin CB')
    
def runargsimwithPCBcontraryflux(allargs=60,N=10,numofrelevargs=5,steps=10000,p=0.5,plotting='',Ct=1.0, Cmax=3.0,intertype='Bid'):
    from population import argumentativepopulation
    from createlistofarguments import createlistofarguments
    from interaction import argumentativeinteractioncontraryflux
    from getundecidedcounts import getundecidedcounts
    from getagentspersuasion import getagentspersuasion
    import numpy as np
#    import pylab as py
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
        breakcount=100
    elif N>=50 and N<80:
        breakcount=300
    else:
        breakcount=1000
        
    fluxevolution=[] 
    strengthevolution=[]         
    for i in range(steps):
        if np.random.random()<p:
            cb='yes'
        else:
            cb='no'
        subpersuasions=getagentspersuasion(popu)  
        for j in range(len(popu)):
            persuasions[j]+=subpersuasions[j]
            
        flux=0
        strength=0        
        for substep in range(1):

            b=argumentativeinteractioncontraryflux(popu, listofarguments, Cmax, intertype, cb,'bidirectional')
            if b==0:
                pass
            else:
                            
                flux+=1
                if b[1]>=30:
                   strength+=(b[1]-30)+1
                elif b[1]<30 and b[1]!=-1:
                    strength+=b[1]+1
                if b[2]>=30:
                   strength+=(b[2]-30)+1
                elif b[2]<30 and b[1]!=-1:
                    strength+=b[2]+1
        fluxevolution.append(flux)
        strengthevolution.append(strength)
                              
                        
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

    if i>200:
        #print 'osc'
        flag=1
    else:
        flag=0 
        
    subpersuasions=getagentspersuasion(popu)  
    for j in range(len(popu)):
        persuasions[j]+=subpersuasions[j]        
                        
    if plotting=='yes':    
        arguments=[[] for i in range(len(popu))]
        for j in range(len(popu)):
            for i in range(len(popu[j].relevancevector)):
                if popu[j].relevancevector[i]==1:
                    #print i
                    arguments[j].append(i)
        #if a[0]!=0 and a[0]!=10:
        makingargumenthistograms(arguments,allargs) 
        plottingopinions(countsund,countspro,countsagainst)       
        plottingpersuasions(persuasions)

    return countsund, countspro, countsagainst,flag,sum(fluxevolution),sum(strengthevolution)#, arguments, persuasions


def analysingflux(Nen=1000,p=0.0):
    cases=[]
    strengths=[]
    for i in range(Nen):      
        A=runargsimwithPCBcontraryflux(60,10,6,10000,p,plotting='',Ct=1.0, Cmax=3.0,intertype='Bid')
        cases.append(A[4])
        strengths.append(A[5])
    return cases,strengths
            
def explorfluxsim():
    import numpy as np
    allcases=[]
    allstrenghts=[]
    for p in [0.0,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0]:
        print(p)
        alpha=analysingflux(1000,p)
        allcases.append(np.mean(alpha[0]))
        allstrenghts.append(np.mean(alpha[1]))
        
    from saving import savinggeneric
    savinggeneric([allcases,allstrenghts],'fluxsimforM6')
    
        

def plottingflux():
    import pylab as py
    from loading import loadinggeneric
    a=loadinggeneric('fluxsimforM6')
    weights=a[1]
    #pesos=[93.251999999999995, 93.408000000000001, 90.688999999999993, 91.105000000000004, 83.025000000000006, 83.263000000000005, 81.882999999999996, 83.692999999999998, 74.332999999999998, 66.491, 56.640000000000001, 45.524000000000001, 0.0]
    Ps=[0.0,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0]
    py.plot(Ps,weights,lw=4)
    py.xlabel(u'P',size=16)
    py.ylabel(u'$\\varphi$',size=16)
    py.yticks(range(0,151,50),size=16)
    py.xticks(size=16)
    #py.ylim([-1,171])
    #py.legend(['Consenso Relativo','Consenso Absoluto'],prop={'size':16})
    #py.ylabel(u'Tamaño de la Región de Consenso',size=16)
    #py.xlim([9,110000])
    #py.xticks(size=16)
    #py.yticks(range(0,15,2),size=16)
    py.savefig(u'phi.svg', bbox_inches='tight')    
    
    
    
def runargsimwithPCB(allargs=60,rangeofimpacts=30,N=10,numofrelevargs=5,steps=10000,p=0.5,plotting='',Ct=1.0, Cmax=3.0,intertype='Bid'):
    from population import argumentativepopulation
    from createlistofarguments import createlistofarguments
    from interaction import argumentativeinteraction
    from getundecidedcounts import getundecidedcounts
    from getagentspersuasion import getagentspersuasion
    import numpy as np
#    import pylab as py
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
        breakcount=500
    elif N>=50 and N<80:
        breakcount=700
    else:
        breakcount=1000
        
    for i in range(steps):
        if np.random.random()<p:
            cb='yes'
        else:
            cb='no'
        subpersuasions=getagentspersuasion(popu)  
        for j in range(len(popu)):
            persuasions[j]+=subpersuasions[j]          
        b=argumentativeinteraction(popu, listofarguments, Cmax, intertype, cb,'bidirectional')
        if b!=None:
            print b
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

    if i>2000:
        #print 'osc'
        flag=1
    else:
        flag=0 
        
    subpersuasions=getagentspersuasion(popu)  
    for j in range(len(popu)):
        persuasions[j]+=subpersuasions[j]        
                        
    if plotting=='yes':    
        arguments=[[] for i in range(len(popu))]
        for j in range(len(popu)):
            for i in range(len(popu[j].relevancevector)):
                if popu[j].relevancevector[i]==1:
                    #print i
                    arguments[j].append(i)
        #if a[0]!=0 and a[0]!=10:
        makingargumenthistograms(arguments,allargs) 
        plottingopinions(countsund,countspro,countsagainst)       
        plottingpersuasions(persuasions)

    return countsund, countspro, countsagainst,flag#, arguments, persuasions
    
        
def checkingfinalstateswithPCB(numens=1000,N=10,allargs=50,steps=10000,p=0.5,numofrelevargs=6):
        counts0=0
        countspl=0
        countsmin=0
        countsbip=0
        otherstuff=0
        countosc=0
        for i in range(numens):
            a=runargsimwithPCB(allargs,allargs/2,N,6,steps,p,'no')
            if a[1][-1]==N:
                countspl+=1
            elif a[2][-1]==N:
                countsmin+=1
            elif a[0][-1]==N:
                counts0+=1
            elif a[0][-1]==0:
                countsbip+=1 
            else:                        
                #otherstuff.append((a[0][-1],a[1][-1],a[2][-1])) 
                otherstuff+=1  
            
            countosc+=a[-1] 
        
        from saving import savinggeneric
        
        savinggeneric((counts0,countspl,countsmin,countsbip,otherstuff,countosc),'PCBNargs50simwithp'+str(p))
        
        return counts0,countspl,countsmin,countsbip,otherstuff,countosc 
        
        
def explorfinalstateswithPCB():
    for p in [0.0,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0]:
        checkingfinalstateswithPCB(1000,10,60,10000,p,6)   
        
                  
        
def exploringPCB(N=10,Ars=60,Rel=6):
    #from loading import loadinggeneric
    import pylab as py
    #probs=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99,0.991,0.992,0.993,0.994,0.995,0.996,0.997,0.998,0.999,0.9991,0.9992,0.9993,0.9994,0.9995,0.9996,0.9997,0.9998,0.9999]
    #results=loadinggeneric('N'+str(N)+'Ars'+str(Ars)+'Rel'+str(Rel))
    results=[]
#    results=[(497, 255, 248, 0, 0, 66),(503, 246, 251, 0, 0, 75),(501, 238, 261, 0, 0, 68),(516, 258, 226, 0, 0, 61),(489, 248, 263, 0, 0, 44),(533, 240, 227, 0, 0, 65),(524, 244, 232, 0, 0, 73),(521, 246, 233, 0, 0, 61),
#    (496, 252, 252, 0, 0, 79),(488, 267, 245, 0, 0, 54),(487, 268, 245, 0, 0, 61),(497, 266, 237, 0, 0, 67),(399, 125, 104, 372, 0, 61)]
    probs=[0.0,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0]
    from loading import loadinggeneric
    
    for i in range(len(probs)):
        results.append(loadinggeneric('PCBsimwithp'+str(probs[i])))
    
    results=py.array(results)/1000.0
    
    ind=[]
    cons=[]
    bip=[]
    others=[]
    osc=[]
    for i in range(len(results)):
        ind.append(results[i][0])
        cons.append(results[i][1]+results[i][2])
        bip.append(results[i][3])
        others.append(results[i][4])
        osc.append(results[i][5])
    colors=[0,120/255.0,255/255.0,150/255.0], [215/255.0,50/255.0,0/255.0,240/255.0], [0/255.0,155/255.0,0/255.0,220/255.0]
    py.figure()
    py.xlabel(u'$P_{CB}$',size=18)
    py.ylabel(u'$P_{efin}$',size=18)
    py.plot(probs,ind,'o-',color=colors[0],lw=4)
    py.plot(probs,cons,'-.',color=colors[1],lw=4)
    py.plot(probs,bip,'o-',color=colors[2],lw=4)
#    py.plot(probs,others,'o-',lw=4)
 #   py.plot(probs,osc,'o-',lw=4)
    py.xticks(size=18)
    py.yticks(size=18)
    py.legend([u'Moderate Consensus','Oriented Consensus','Bipolarization','Otros Estados','Oscilaciones'],prop={'size':16})
    #py.title('N = '+str(N)+', Ars = '+str(Ars)+', Rel = '+str(Rel),size=18)
    py.savefig(u'Estados Finales vs Prob - '+'N'+str(N)+'Ars'+str(Ars)+'Rel'+str(Rel)+'.svg', bbox_inches='tight')            
    
         
              
                   
def newanalyzingargsimphasediagramBidrelvsN():
    numens=1000
    import numpy as np
    import pylab as py
    import copy
    from loading import loadinggeneric
    import matplotlib as mpl        
    colors = [[0,120/255.0,255/255.0,150/255.0], [215/255.0,50/255.0,0/255.0,240/255.0], [0/255.0,155/255.0,0/255.0,220/255.0], [0/255.0,155/255.0,0/255.0,110/255.0]]
    bounds = [0,1,2]

    cmap = mpl.colors.ListedColormap(colors)      
    #from saving import savinggeneric
    #if numens==1000 or numens==100:
    #    from collectdata import collectargsimdatarel
    #    alldata=collectargsimdatarel(numens,'FullExploration')
    #    
    #plotting=[alldata[0],alldata[1],alldata[2],alldata[3],alldata[4]]  
    #savinggeneric(plotting,'relN')  
    plotting=loadinggeneric('relN','C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')        
    for j in range(len(plotting)+1): 
        for tipo in ['par']:
            py.figure()
            if tipo=='impar':
                py.imshow(np.array(plotting[j][0:len(plotting[j]):2]),aspect='auto',vmin=0, vmax=numens,cmap='binary')
            else:
                if j!=5:
                    py.imshow(np.array(plotting[j][1:len(plotting[j]):2]),aspect='auto',vmin=0, vmax=numens,cmap='binary')  
                else:          
                    newplotting2=plotting[0][1:len(plotting[0]):2]
                    for iii in range(len(plotting[0][1:len(plotting[0]):2])):
                        for jjj in range(len(plotting[0][1:len(plotting[0]):2][0])):
                            if plotting[0][1:len(plotting[0]):2][iii][jjj]>plotting[1][1:len(plotting[1]):2][iii][jjj]:
                                newplotting2[iii][jjj]=0
                            elif plotting[1][1:len(plotting[1]):2][iii][jjj]>plotting[0][1:len(plotting[0]):2][iii][jjj]:
                                newplotting2[iii][jjj]=1                            
                    py.imshow(newplotting2,aspect='auto',vmin=0, vmax=3, cmap=cmap)                 
         
#        if N==10 or N==20 or N==50:            
            #if j==10:      
            #    py.imshow(np.array(plotting[j]),aspect='auto',vmin=0, vmax=numens)#,extent=[0,1,1,0])
            #elif j==13 or j==12:
            #    py.imshow(np.array(plotting[j]),aspect='auto',vmin=0, vmax=numens/100)#,extent=[0,1,1,0])
            #else:
            if tipo=='par':    
                py.ylim([-0.5,4.5])
            else:
                py.ylim([-0.5,5.5])
            py.xlim([-0.5,20.5])
            py.xlabel(u'N',size=18)
            py.ylabel(u'M',size=18)
            if j!=5:
                C=py.colorbar()    
                for l in C.ax.yaxis.get_ticklabels():
                    l.set_size(18)
            ax=py.gca()    
            #ax.locator_params(nbins=10) #nticks=nbins/2
            #py.minorticks_on()
            py.xticks(list(np.arange(0,21,2)))
            #py.yticks(list(np.arange(-0.5,4.75,1)))
            #ax.xaxis.set_ticklabels(range(10,101,10)+[' 110'],size=16)
            #py.xticks(list(np.arange(0,21,2)))
            py.xticks(list(np.arange(0,21,2)))
            ax.xaxis.set_ticklabels(range(10,101,30),size=16)
            
            if tipo=='impar':
                ax.yaxis.set_ticklabels(['']+range(5,56,10),size=16)
            else:
                ax.yaxis.set_ticklabels(['']+range(10,56,10),size=16)               
    

            import os
            os.chdir('C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')
            # if j==0:
            #     #py.title('Probabilidad de Hallar Consenso Moderado',size=18)
            #     py.savefig('Probabilidad de Hallar Consenso Moderado Rel vs. N '+tipo+'.png', bbox_inches='tight')
            # elif j==1:
            #     #py.title('Probabilidad de Hallar Consenso Orientado',size=18)
            #     py.savefig('Probabilidad de Hallar Consenso Orientado Rel vs. N '+tipo+'.png', bbox_inches='tight')
            # elif j==2:
            #     #py.title(u'Probabilidad de Hallar Bipolarización',size=18)   
            #     py.savefig(u'Probabilidad de Hallar Bipolarización Rel vs. N '+tipo+'.png', bbox_inches='tight')
            if j==5:
            #     #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                 py.savefig(u'Regiones Rel vs. N '+tipo+'.svg', bbox_inches='tight')
            os.chdir('C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')


def studyinginitialdistofopinions(allargs=60,N=10,rel=5,Ct=1.0,Cmax=3.0):
    from population import argumentativepopulation
    from createlistofarguments import createlistofarguments
    from getundecidedcounts import getundecidedcounts
    countsund=[]
    countspro=[]
    countsagainst=[]   
    for i in range(10000): 
        listofarguments=createlistofarguments(allargs,1,allargs/2)
        popu=argumentativepopulation(listofarguments,N,rel,Ct,Cmax)
    
        a=getundecidedcounts(popu)
        countsund.append(a[0])
        countspro.append(a[1])
        countsagainst.append(a[2])
        
    return countsund,countspro,countsagainst                                                          
    
    
def plottingopinions(countsund,countspro,countsagainst):
        import pylab as py
        #py.figure()    
        py.plot(countsund,alpha=0.1,color='r')
        #py.plot(countspro,alpha=0.1)
        #py.plot(countsagainst,alpha=0.1)
        py.ylim([-0.1,10.1])
        #py.legend(['Undecided','Prodecided','Againstdecided'])
        py.title('Opiniones')
        py.ylabel('Opiniones')
        py.xlabel('Pasos Temporales')
        
def plottingpersuasions(persuasions):
    import pylab as py
    py.figure()
    for i in range(len(persuasions)):
        py.plot(persuasions[i])
        py.ylim([-3.1,3.1])
    py.title('Posturas')
    py.xlabel('Pasos Temporales')
    py.ylabel('Posturas')    
    
    
def makingargumenthistograms(arguments,allargs):
    import pylab as py
    B=[]
    for i in range(len(arguments)):
        B.append(py.hist(arguments[i],range(allargs))) #acá pongo allargs
    
    C=py.array([0.0 for i in range(allargs-1)]) #acá pongo allargs-1
    for i in range(len(B)):
        C+=B[i][0]
    py.figure()    
    py.bar(list(py.arange(-allargs/2,0,1))+list(range(1,allargs/2)),C)#range(59),C) #acá pongo allargs-1
    #py.yticks(range(0,22,2))
    #py.xticks(list(py.arange(-30,31,3)))
    #py.xlim([-30,30])
    
def finalargumentdistribution(cb='no',chosen='consenso2',N=10,Nen=100):
    from loading import loadinggeneric
    if cb=='no':
        a=loadinggeneric(chosen+'sincb','D:\\Doctorado\\Simulation_Functions\\')
    else: 
        a=loadinggeneric(chosen+'concb','C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')    
    if N==100:
        a=loadinggeneric(chosen+'sincb100','D:\\Doctorado\\Simulation_Functions\\') 
                   
    import pylab as py
    py.figure()
    py.hist(a,61)
    py.ylabel(u'Proporción de Argumentos',size=18)
    py.xlabel('Peso de los Argumentos',size=18)
    py.xticks(size=18)
    if chosen=='bip':
        py.yticks([0,500,1000,1500],size=18)
    ax=py.gca() 
    if N==10 and chosen=='consenso1':
        py.ylim([0,700])  
    elif N==10 and chosen=='consenso2':
        py.ylim([0,600])   
    if N!=100:
        ax.yaxis.set_ticklabels(py.arange(0,1.0,0.1),size=18)
    elif N==100 and chosen!='indeciso':
        ax.yaxis.set_ticklabels([0.0,0.2,0.4,0.6,0.8],size=18)   
    else:
        ax.yaxis.set_ticklabels(py.arange(0,1.0,0.1),size=18)
                      
    py.savefig(chosen+'histcbfino'+cb+'.svg', bbox_inches='tight')     
    
    
def finalargumentsanalysis(rel=5,cb='no'):
    n=0
    resultspl=[]
    resultsneg=[]
    while n<1000:
        a=countingfinalarguments(cb,60,10,rel)
        if a!=0 and a!=-1:
            n+=1
            print n
            resultspl.append(a[0])
            resultsneg.append(a[1])
        elif a==-1:
            print 'error fatal'
    return resultspl,resultsneg
    
        
def plottingmanyevolutions(chosen='indeciso',cb='no',N=10,Ars=60,bins=5,rel=6):
        import numpy as np
        import pylab as py
        from loading import loadinggeneric
        if N==100:
            if rel==5:
                evolutions=loadinggeneric(chosen+'evolcb'+cb+'100','C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions\\')
            elif rel==6:
                evolutions=loadinggeneric(chosen+'evolcb'+cb+'100rel6','C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions\\')                
        else:
            if rel==5:
                evolutions=loadinggeneric(chosen+'evolcb'+cb,'D:\\Doctorado\\Simulation_Functions\\')
            else:
                evolutions=loadinggeneric(chosen+'evolcb'+cb+'10rel6','D:\\Doctorado\\Simulation_Functions\\')
                
            
        newevols=list([list([0 for alpha in range(12)]) for i in range(max([len(evolutions[i]) for i in range(len(evolutions))]))])
        a=max([len(evolutions[i]) for i in range(len(evolutions))])
        for i in range(len(evolutions)):
            if len(evolutions[i])!=a:
                evolutions[i]+=[evolutions[i][-1] for j in range(a-len(evolutions[i]))]
        
        for j in range(a):
            for k in range(12):
                for i in range(len(evolutions)):
                    newevols[j][k]+=int(list(evolutions[i][j])[k])
                newevols[j][k]/=float(10)
                
        B=np.transpose(newevols)
        fig=py.figure()  
        if N==10:
            py.imshow(B,cmap='gray_r',aspect='auto',vmax=10)
        else:
            if rel==5:
                py.imshow(B,cmap='gray_r',aspect='auto',vmax=100)
            else:
                py.imshow(B,cmap='gray_r',aspect='auto',vmax=300)                
        py.ylabel(u'Argumentos',size=18)
        py.xlabel(u'Pasos Temporales',size=18)
        py.ylim([-0.5,11+0.5])
        py.xticks(size=16)
        length=len(np.arange(-Ars,Ars+1,5))
        length=np.linspace(-0.5,11+0.5,Ars/10+1)
        py.yticks(length,size=16)
        ax=py.gca()
        ax.yaxis.set_ticklabels(np.arange(-Ars/2,Ars/2+1,10))
        py.xlim([0,150])
        
        
        
        C=py.colorbar()    
        for m in C.ax.yaxis.get_ticklabels():
            m.set_size(16)
        py.xticks(range(0,151,50))
        ax.xaxis.set_ticklabels([0,50,100,150])

        if N==100:
            py.xlim([0,2000])            
            py.get_current_fig_manager().window.showMaximized() 
        #py.title('Sistema Converge a '+chosentype,size=18)        
        fig.set_size_inches(20,10)          
        py.savefig('D:\\Doctorado\\'+chosen+'evolnueva'+'CB='+cb+'.svg', bbox_inches='tight') 
        
                        
        
def analyzingargsimphasediagram3oldPoblsMay():
    cb='yes'
    numens=1000
    import numpy as np
    import pylab as py
    import matplotlib as mpl

    colors = [[0,120/255.0,255/255.0,150/255.0], [215/255.0,50/255.0,0/255.0,240/255.0], [0/255.0,155/255.0,0/255.0,220/255.0]]
    bounds = [0,1,2]

    cmap = mpl.colors.ListedColormap(colors)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    import copy
    
    # from collectdata import collectargsimdata
    # alldata=collectargsimdata(numens,cb)
    # plotting=[alldata[0],alldata[1],alldata[2],alldata[3],alldata[4],alldata[5],alldata[6]]  
    # from saving import savinggeneric
    # if cb=='no':
    #     savinggeneric(plotting,'sinCB')     
    # else:
    # savinggeneric(plotting,'conCBpoblsmay')
       
    from loading import loadinggeneric    
    plotting=loadinggeneric('conCBpoblsmay','D:\\Doctorado\\Simulation_Functions\\')
#    'C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')      
   
    for j in range(len(plotting)+1):            
        py.figure()
        
        py.imshow(np.array(plotting[-1]),aspect='auto',vmin=0, vmax=1,cmap='gray_r')
#        py.ylim([0,48])
#        py.xlim([1,97]) #Si quiero plotear desde 4, arrancar en -1. Para hacerlo desde 6, es en 1, tics hasta 99.
        ax=py.gca() 

        py.xticks(np.arange(0,91,30),size=16)               
        ax.xaxis.set_ticklabels(range(10,101,30)) #Cambiar ini por 4 y paso por 10 para arrancar en 4; ini por 6, paso por 12 para arrancar en 6.
        py.yticks(np.arange(0,46,15),size=16)             
        ax.yaxis.set_ticklabels(range(10,101,30))      
        py.ylim([-0.5,45.5]) #arranca en 10
        py.xlim([-0.5,90.5]) #arranca en 10
#        else:
#            py.imshow(np.array(plotting[j]),vmax=1)#aspect='auto',vmin=0,vmax=1,extent=[0,1,1,0]) 
#            py.xlim([0,100])
#            py.ylim([0,100])
        py.xlabel(u'N',size=16)
        py.ylabel(u'$N_{A}$',size=16)
        C=py.colorbar()    
        for l in C.ax.yaxis.get_ticklabels():
            l.set_size(14)    
   
        #ax.locator_params(nbins=10) #nticks=nbins/2
        # py.minorticks_on()
        # py.yticks(range(2,49,5),size=18)
        # py.xticks(range(6,99,10),size=18) #Si quiero plotear desde 4, arrancar en 0. Para hacerlo desde 6, es en 2. A parte, para el caso de 4, el paso es de 10, y fin es 97. Caso 6: de 12, fin de 99.
        # #ax.xaxis.set_ticklabels(range(6,103,12)) #Cambiar ini por 4 y paso por 10 para arrancar en 4; ini por 6, paso por 12 para arrancar en 6.
        # #ax.yaxis.set_ticklabels(range(6,103,12))
        # ax.xaxis.set_ticklabels(range(10,101,10)) #Cambiar ini por 4 y paso por 10 para arrancar en 4; ini por 6, paso por 12 para arrancar en 6.
        # ax.yaxis.set_ticklabels(range(10,101,10))        
        
        # ax.tick_params(axis='y',which='minor',left='off')
        #if N==20:
        #    py.colorbar(ticks=range(0,21,4))
        #else:
        #    py.colorbar()
        
        
        
        
        
        import os
        elviejo=os.getcwd()
        #os.chdir('C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')
        
        #py.savefig('11 - Pobl May con CB '+'original.svg', bbox_inches='tight')
        os.chdir(elviejo)          
        
        
def plottingmanyevolutionsbins1(chosen='indeciso',cb='no',N=10,Ars=60,bins=1,rel=6):
        #Sale de: evolutions=plottingarguments(tipo=5,cb='no',Ars=60,N=10,rel=6,l=0,bins=1,chosen='indeciso')
        import numpy as np
        import pylab as py
        from loading import loadinggeneric
        if N==100:
            B=loadinggeneric('PARAPLOTEARindecisoevolcbno100rel6bines1ens100')
            # if rel==5:
            #     evolutions=loadinggeneric(chosen+'evolcb'+cb+'100','C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions\\')
            # elif rel==6:
            #     evolutions=loadinggeneric(chosen+'evolcb'+cb+'100rel6','C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions\\')                
        else:
            if rel==5:
                evolutions=loadinggeneric(chosen+'evolcb'+cb,'D:\\Doctorado\\Simulation_Functions\\')
            else:
                evolutions=loadinggeneric(chosen+'evolcb'+cb+'10rel6bines1ens100','D:\\Doctorado\\Simulation_Functions\\')
            
            newevols=list([list([0 for alpha in range(62)]) for i in range(max([len(evolutions[i]) for i in range(len(evolutions))]))])
            a=max([len(evolutions[i]) for i in range(len(evolutions))])
            for i in range(len(evolutions)):
                if len(evolutions[i])!=a:
                    evolutions[i]+=[evolutions[i][-1] for j in range(a-len(evolutions[i]))]
            
            for j in range(a):
                for k in range(61):
                    for i in range(len(evolutions)):
                        newevols[j][k]+=int(list(evolutions[i][j])[k])
                    newevols[j][k]/=float(N)
                
            B=np.transpose(newevols)
        fig=py.figure()  
        if N==10:
            py.imshow(B,cmap='gray_r',aspect='auto',vmax=50)
        else:
            py.imshow(B,cmap='gray_r',aspect='auto',vmax=100)
        # else:
        #     if rel==5:
        #         py.imshow(B,cmap='gray_r',aspect='auto',vmax=100)
        #     else:
        #         py.imshow(B,cmap='gray_r',aspect='auto',vmax=20)                
        py.ylabel(u'Argumentos',size=18)
        py.xlabel(u'Pasos Temporales',size=18)
        py.ylim([-0.5,60+0.5])
        py.xticks(size=16)
        length=len(np.arange(-Ars,Ars+1,5))
        length=np.linspace(-0.5,60+0.5,Ars/10+1)
        py.yticks(length,size=16)
        ax=py.gca()
        ax.yaxis.set_ticklabels(np.arange(-Ars/2,Ars/2+1,10))
        py.xlim([0,100])
        
        
        
        C=py.colorbar()    
        for m in C.ax.yaxis.get_ticklabels():
            m.set_size(16)
        py.xticks(range(0,101,20))
        ax.xaxis.set_ticklabels([0,2,4,6,8,10])

        if N==100:
            py.xlim([0,1000])          
            #py.get_current_fig_manager().window.showMaximized()
            py.xticks(range(0,1001,200))
            ax.xaxis.set_ticklabels([0,2,4,6,8,10])                   
        fig.set_size_inches(12,5)          
        py.savefig('D:\\Doctorado\\Paper Argumentos\\Review\\'+chosen+'evolnuevaPROBANDO'+str(N)+'CB='+cb+'.svg', bbox_inches='tight') 
                                            
plottingmanyevolutionsbins1(chosen='indeciso',cb='no',N=10,Ars=60,bins=1,rel=6)
plottingmanyevolutionsbins1(chosen='consenso1',cb='no',N=10,Ars=60,bins=1,rel=6)
plottingmanyevolutionsbins1(chosen='consenso2',cb='no',N=10,Ars=60,bins=1,rel=6)
import pylab as py
py.close('all')
                
def analyzingargsimphasediagram3reviewer2grueso(homo=0,cb='no'):
    import numpy as np
    import pylab as py
    import copy
    from loading import loadinggeneric
    import matplotlib.pyplot as plt
    import matplotlib as mpl    

    numens=1000
    homo=0
    #from saving import savinggeneric    
    #from newcollectdata import newcollectargsimdatareviewer2grueso
    #alldata=newcollectargsimdatareviewer(homo,'no')
    alldataraw=loadinggeneric('BarridoGruesoReviewerDatos')
    deltaswho=alldataraw[7]

    

    
    #savinggeneric(plotting,'conCBreviewer2grueso'+'homo'+str(homo),'D:\\Doctorado\\Simulation_Functions\\')        
    
    colors = [[0,120/255.0,255/255.0,150/255.0], [215/255.0,50/255.0,0/255.0,240/255.0], [0/255.0,155/255.0,0/255.0,220/255.0], [0/255.0,155/255.0,0/255.0,110/255.0],[0,0,0,0]]
    bounds = [0,1,2]

    cmap = mpl.colors.ListedColormap(colors)    
    
    factordebineado=1/3.0
        
    tipo='convergente'
    alldata=[[[0 for j in range(len(np.arange(0,10.1,factordebineado)))] for i in range(6,51,2)] for k in range(4)]
    for i in range(len(range(6,51,2))):
        counters=[0.0 for rrrr in range(len(np.arange(0,10.1,factordebineado)))]
        for j in range(len(deltaswho)):
            flag=0
            k=0
            while flag==0:
                if deltaswho[j]>=factordebineado*k and deltaswho[j]<factordebineado*k+factordebineado:
                    flag=1
                    if not np.isnan(alldataraw[0][i][j]):
                        alldata[0][i][k]+=alldataraw[0][i][j]
                        alldata[1][i][k]+=alldataraw[1][i][j]
                        alldata[2][i][k]+=alldataraw[2][i][j]
                        alldata[3][i][k]+=alldataraw[6][i][j]
                        counters[k]+=1.0        
                k+=1
                
                
        if 0.0 in counters:
            for l in range(len(counters)):
                if counters[l]==0.0:
                    alldata[0][i][l]=np.nan
                    alldata[1][i][l]=np.nan
                    alldata[2][i][l]=np.nan
                    alldata[3][i][l]=np.nan
                
                
        alldata[0][i]=list(np.array(alldata[0][i])/np.array(counters))
        alldata[1][i]=list(np.array(alldata[1][i])/np.array(counters))
        alldata[2][i]=list(np.array(alldata[2][i])/np.array(counters))
        alldata[3][i]=list(np.array(alldata[3][i])/np.array(counters))
    
    plotting=[alldata[0],alldata[1],alldata[2],alldata[3]]  
   
    for j in [4]:            
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
        py.ylim([1.5,22.5]) #arranca en 10  

            
        ax=py.gca()  
        py.xlim([-0.5,45.5]) #arranca en 10
        py.xticks(np.arange(0,46,15),size=16)               
        py.yticks(np.arange(2,23,20/4.0),size=16)                           
        ax.xaxis.set_ticklabels([0.2,0.8,1.4,2.0])      
        ax.yaxis.set_ticklabels(range(10,51,10)) #Cambiar ini por 4 y paso por 10 para arrancar en 4; ini por 6, paso por 12 para arrancar en 6.

#        else:
#            py.imshow(np.array(plotting[j]),vmax=1)#aspect='auto',vmin=0,vmax=1,extent=[0,1,1,0]) 
#            py.xlim([0,100])
#            py.ylim([0,100])
        py.xlabel(u'$N_A/N$',size=16)
        py.ylabel(u'M',size=16)
        C=py.colorbar()    
        for l in C.ax.yaxis.get_ticklabels():
            l.set_size(14)    
                           
                                                               
#        py.xlim([1,97]) #Si quiero plotear desde 4, arrancar en -1. Para hacerlo desde 6, es en 1, tics hasta 99.
        # py.ylim([2,47.5]) #arranca en 10
        # py.xlim([5,96.5]) #arranca en 10

#        else:
#            py.imshow(np.array(plotting[j]),vmax=1)#aspect='auto',vmin=0,vmax=1,extent=[0,1,1,0]) 
#            py.xlim([0,100])
#            py.ylim([0,100])

        #ax.locator_params(nbins=10) #nticks=nbins/2
#        py.minorticks_on()
        #ax.xaxis.set_ticklabels(range(6,103,12)) #Cambiar ini por 4 y paso por 10 para arrancar en 4; ini por 6, paso por 12 para arrancar en 6.
        #ax.yaxis.set_ticklabels(range(6,103,12))
  
        
        ax.tick_params(axis='y',which='minor',left='off')
        #if N==20:
        #    py.colorbar(ticks=range(0,21,4))
        #else:
        #    py.colorbar()
        import os
        elviejo=os.getcwd()
        os.chdir('D:\\Doctorado\\Simulation_Functions\\')
        #os.chdir('C:\\Users\\Fede Barrera\\Desktop\\Simulation_Functions\\')
        
        if cb=='no':
                if j==0:
                    #py.title('Probabilidad de Hallar Consenso Moderado',size=18)
                    py.savefig('01 - PCM sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==1:
                    #py.title('Probabilidad de Hallar Consenso Orientado',size=18)
                    py.savefig('02 - PCO sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==2:
                #py.title(u'Probabilidad de Hallar Bipolarización',size=18)   
                    py.savefig(u'03 - PBip sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==3:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'04 - Posc sin CB - Homo '+str(homo)+'.png', bbox_inches='tight')
                elif j==4:
                    #py.title(u'Probabilidad de Hallar Otros Estados',size=18)   
                    py.savefig(u'05 - Regiones sin CB Reviewer '+'- Homo '+str(homo)+'.svg', bbox_inches='tight')                             
                os.chdir(elviejo)
