class Argument(object):
  
    """
    Representation of an argument.
    """
    def __init__(self, valence, impact=1.0):
        """
        Initialize an Argument instance, saves all parameters as attributes
        of the instance.        
        valence= +-1 (sign)
        impact= default 1 (we used from 1 to 30 for the simulations).
        """
        self.valence=valence
        self.impact=impact

    def getvalence(self):
        """
        Returns sign.
        """
        return self.valence
        
    def getimpact(self):
        """
        Returns weight.
        """
        return self.impact