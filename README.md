# Polarizing crowds: consensus and bipolarization in a persuasive arguments model
These scripts correspond to the paper of the same name. They are all python scripts, but some have been cythonized for speed. They will be progressively clarified, so that anyone who wishes to run the simulations will be able to do so. Right now, the scripts are perfectly functional, but lack comments. Many scripts may be divided in the future, so that each function can be more easily accessed. 

The main script is newrunargsim.py, which has several functions designed to perform the simulations. 
explorargsim.py has parameter explorations which call upon some functions inside newrunargsim.py. 
newargumentphasediagram has many plotting functions, which were used to make the Figures of the paper.
All functions labeled as 2 and found with extension .pyx were compiled with cython to gain speed, and are used by some of the functions in newrunargsim.py. All of them have a counterpart without the number 2, which are the actual uncythonized scripts, and correspond to the main underlying functions:
Agent.py employs object-oriented programming for creating the agents used in the simulations, with some useful functions that retain arguments, calculate and update posture, calculate and update opinion, among others. 
Arguments.py also uses object-oriented programming, but for the arguments, which can have sign and weight.
interaction.py implements all interactions (some are unused in this paper, this script will be massively clarified in the future).
population.py creates a population of agents according to some specifications (like number of agents).

More descriptions for the rest of the functions will be added in the future, but those are the main scripts.

