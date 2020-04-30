import os
#os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
#os.chdir('C:\\Users\\Fede\\Desktop\\Simulation_Functions\\') 
os.chdir('D:\\Doctorado\\Simulation_Functions\\')

execfile('newexplorargsim.py')

for M in [42]:
    print(M)    
    newexplorargsimwithconvergencereviewer2(M,'no',0,1000,'w')

