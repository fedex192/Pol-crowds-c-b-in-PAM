'''This batch script is used to run the explorations of parameters. Depending on the one to explore, different commands should be used.
This is just an example. Using this is useful for using different cores of a processor, for paralellization of the simulation (procedure
sometimes known as "embarrasingly parallel". '''

#First, choose the proper directory.

import os
#os.chdir('C:\\Users\\Guillermo Lemarchand\\Desktop\\Simulation_Functions') 
#os.chdir('C:\\Users\\Fede\\Desktop\\Simulation_Functions\\') 
os.chdir('D:\\Doctorado\\Simulation_Functions\\')

#now, execute the exploration file with the exploration function one wishes to use. In this case, we execute the file
#with the exploration of N vs. N_A

execfile('newexplorargsim.py')

M=6

for NA in [10,20,30,40,50]: #you can run this on a console, change these values, then run it again in another console, for paralellization.
    print(NA) #for keeping track
    newexplorargsimwithconvergence(homo=0,allargs=NA,Nini=10,Nfin=101,cb='no',numofrelevargs=M,numens=1000,opsys='w')
    
#We suggest making several copies of this file with different names, changing the values of the exploration, and running them on different
#consoles, for paralellization and easily keeping track of how different explorations are progressing.

