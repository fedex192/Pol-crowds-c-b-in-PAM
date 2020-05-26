# Polarizing crowds: consensus and bipolarization in a persuasive arguments model
These scripts correspond to the paper of the same name. They are all python scripts, but some have been cythonized for speed. Most of them have been thoroughly commented, so that anyone who wishes to run the simulations will be able to do so. A couple are still being clarified, as detailed below. However, all the scripts are perfectly functional.

Please note that posture was referred to as "persuasion" in most of our codes. That name was changed later. We hope this will not be confusing (files that use this variable have this same note at the beginning of the file).

The main functions are found in the master directory:
- Agent.py employs object-oriented programming for creating the agents used in the simulations, with some useful functions that retain arguments, calculate and update posture, calculate and update opinion, among others. 
- Arguments.py also uses object-oriented programming, but for the arguments, which can have sign and weight.
- createlistofarguments.py makes a list of argument objects according to specifications (like total number of arguments, N_A).
- newinteraction.py implements all interactions.
- population.py creates a population of agents according to some specifications (like number of agents, N).
- getundecidedcounts.py is used for counting how many agents have each possible opinion ina population.
- getagentspersuasion.py returns the postures of all the agents of a population (note the name, where posture is called persuasion).
- getopinions.py returns a list of opinions of all the agents in a population.
- choosinginteractingagents.py is used for determining which agents will interact in a given step of the simulation.
- checkconvergence.py is used for checking if a system has already converged to the final state of opinions, or not.
- newrunargsim.py is the main file, and has the most important functions for performing the simulations. 
- plottingopinions.py is used for making the plots of the second column of Figure 3.
- plottingarguments.py is used for making the plots of the first column of Figure 3, and those of Figure 2 b) and c).
- newexplorargsim.py is used for parameter exploration; we explore N vs. N_A here.
- exploringM.py is used for parameter exploration; we explore M vs. N_A and M vs. N here.
- exploringDelta.py is used for parameter exploration; we explore N_A/N vs. M here.
- saving.py is used for saving results of explorations.
- runnewexplorargsim1.py is an example script used for running explorations in a paralellized fashion.
- PCBSimulation.py (used for making the plot of Figure 7 (a))
- argumentativeinteractioncontraryflux.py is a slightly modified version of argumentativeinteraction found in newinteraction.py, used by ContraryFluxSimulation.py
- ContraryFluxSimulation.py is used for making the plot of Figure 7 (b). 

List of functions that still need to be cleaned up:

- newcollectdata.py (used for loading and restructuring saved variables so that data can be analyzed and plotted).
- newargumentsphasediagram (used for making most of the plots and figures of the paper)

Expected date for finishing clean-up: in a couple of hours.

Inside the folder "Cythonized Functions" are scripts mainly used by newrunargsim.py, compiled with cython to gain speed. The files with extension ".pyx" are the uncompilled files, and are mainly copies of files of similar names found in the main directory (some of them end in number 2, others start with letter C, and some may also have a "new" added to the name, but the rest of the name is the same as some other file in the mentioned directory). The files with ".pyd" extension are the corresponding compiled files. There is also a setup.py file, which can be used to compile the ".pyx" files into the ".pyd" files. All files in this folder (except for setup.py) will not have the same thorough comments found in the main files, and they may contain other functions which were used for testing, and were later unused for the final simulations (having those compiled allowed for testing, and removing them was unnecesary, for it required recompilling the files). We suggest learning to cythonize and use this files if you wish to run the full parameter explorations, since it can take a very long time and many many cores simultaneously running for it to finish in a useful amount of time. The .pyd files will probably not work in other computers than the ones we used (compilation is computer-specific), so you will need to use the .pyx files along with setup.py. Please, contact the corresponding author if you need further directions (although a quick google search should be sufficient for learning how to cythonize files using setup.py).
