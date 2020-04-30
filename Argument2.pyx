cdef class Argument(object):
   
    cdef public double valence
    cdef public double impact
   
    """
    Representation of an argument.
    """
    def __init__(self, valence, impact=1.0):
        """
        Initialize an Argument instance, saves all parameters as attributes
        of the instance.        
        valence= +-1
        impact= default 1.
        """
        self.valence=valence
        self.impact=impact

    cpdef double getvalence(self):
        """
        Returns valence.
        """
        return self.valence
        
    cpdef double getimpact(self):
        """
        Returns impact.
        """
        return self.impact
    
#class ArgumentsList(object):
#    """
#    Representation of an argument.
#    """
#    def __init__(self, positive=10, negative=10):
#        """
#        Initializes an Argument List, that can be used for one run of the simulations.
#        Saves all parameters as attributes of the instance.        
#        opinion: Integer, possible values: 1, -1, 0.        
#        persuasion: a double between -Cmax and Cmax.
#        Ct: a double between 0 and Cmax; it determines changes in opinion.
#        """
#        self.positive=positive
#        self.negative=negative