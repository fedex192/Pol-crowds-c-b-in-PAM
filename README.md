# Polarizing crowds: consensus and bipolarization in a persuasive arguments model
These scripts correspond to the paper of the same name. They are all python scripts, but some have been cythonized for speed. They will be progressively clarified, so that anyone who wishes to run the simulations will be able to do so. Right now, the scripts are perfectly functional, but lack comments. Many scripts may be divided in the future, so that each function can be more easily accessed. 

The main script is newrunargsim.py, which has several functions designed to perform the simulations. 
explorargsim.py has parameter explorations which call upon some functions inside newrunargsim.py. 
newargumentphasediagram has many plotting functions, which were used to make the Figures of the paper.

Inside the folder "Cythonized Functions" are scripts mainly used by newrunargsim.py, compiled with cython to gain speed. The files with extension ".pyx" are the uncompilled files, and are mainly copies of files of similar names found in the main directory (some of them end in number 2, others start with letter C, and some may also have a "new" added to the name, but the rest of the name is the same as some other file in the mentioned directory). The files with ".pyd" extension are the corresponding compiled files. There is also a setup.py file, which can be used to compile the ".pyx" files into the ".pyd" files. All files in this folder (except for setup.py) will not have the same thorough comments found in the main files, and they may contain other functions which were used for testing, and were later unused for the final simulations (having those compiled allowed for testing, and removing them was unnecesary, for it required recompilling the files). 

The main underlying functions are found in the master directory:
Agent.py employs object-oriented programming for creating the agents used in the simulations, with some useful functions that retain arguments, calculate and update posture, calculate and update opinion, among others. 
Arguments.py also uses object-oriented programming, but for the arguments, which can have sign and weight.
interaction.py implements all interactions (some are unused in this paper, this script will be massively clarified in the future).
population.py creates a population of agents according to some specifications (like number of agents).

More descriptions for the rest of the functions will be added in the future, but those are the main scripts.

List of functions already cleaned:

Agent.py
Argument.py
createlistofarguments.py
population.py
getundecidedcounts.py
getagentspersuasion.py
getopinions.py
newinteraction.py
choosinginteractingagents.py
newrunargsim.py
checkconvergence.py
plottingopinions.py
plottingarguments.py

Expected date for finishing clean-up: before the end of may, possibly before monday the 25th.
