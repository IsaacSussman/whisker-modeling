import numpy as np
import scipy as sp
import matplotlib as mp
import matplotlib.pyplot as plt

class whisker:
    def __init__(self, arc_length: float, medulla_arc_length: float, youngs_modulus: float, base_d: float, tip_d: float, medulla_base_d: float, A: float, B: float):
        self.arc_length = arc_length
        self.medulla_arc_length = medulla_arc_length
        self.youngs_modulus = youngs_modulus

        self.base_d = base_d
        self.medulla_base_d = medulla_base_d
        self.tip_d = tip_d
        self.conicity = self.tip_d / self.base_d
        self.base_I = (np.pi * (self.base_d**4 - self.medulla_base_d**4))/64

        # Cesaro Variables - Curvature
        self.A = A
        self.B = B

    def diameter_by_conicity(self, s):
        return self.base_d*(1-((1 - self.conicity)/self.arc_length)*s)

    def diameter_simple(self, s):
        return self.base_d - s*((self.base_d - self.tip_d)/self.arc_length)
    
    def moment_of_inertia_WRONG(self, s):
        # This does not account for the different conicity of the medulla
        # Strictly copied from the thesis
        return self.base_I * (1-((1-self.conicity)/self.arc_length))
    

    def cartesian(self):
        pass

    def graph(self, samples):
        s = np.linspace(0,self.arc_length, samples)
        x = (np.cos(0.5 * s * (2*self.B + self.A*s)))
        y = np.sin(0.5 * s * (2*self.B + self.A*s))
        if self.A==self.B and self.B==0:
            x=np.linspace(0,0, samples)
            y=s

        ax = plt.figure().add_subplot()
        ax.plot(x, y, label = "Whisker")
        ax.legend()
        plt.show()
    
    def curvature(self, s):
        return self.A*s + self.B

    def applyTipForce(self, angle: float, magnitude: float):
        pass


