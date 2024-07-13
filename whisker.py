import numpy as np
import matplotlib.pyplot as plt

class whisker:
    counter = 0
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
    
    def setValues(self, arc_length: float = None, medulla_arc_length: float = None, youngs_modulus: float = None, base_d: float = None, tip_d: float = None, medulla_base_d: float = None, A: float = None, B: float = None):
        self.arc_length = arc_length if arc_length else self.arc_length
        self.medulla_arc_length = medulla_arc_length if medulla_arc_length else self.medulla_arc_length
        self.youngs_modulus = youngs_modulus if youngs_modulus else self.youngs_modulus

        self.base_d = base_d if base_d else self.base_d
        self.medulla_base_d = medulla_base_d if medulla_base_d else self.medulla_base_d
        self.tip_d = tip_d if tip_d else self.tip_d
        self.conicity = self.tip_d / self.base_d
        self.base_I = (np.pi * (self.base_d**4 - self.medulla_base_d**4))/64

        # Cesaro Variables - Curvature
        self.A = A if A else self.A
        self.B = B if B else self.B

    def diameter_by_conicity(self, s):
        return self.base_d*(1-((1 - self.conicity)/self.arc_length)*s)

    def diameter_simple(self, s):
        return self.base_d - s*((self.base_d - self.tip_d)/self.arc_length)
    
    def moment_of_inertia_WRONG(self, s):
        # This does not account for the different conicity of the medulla
        # Strictly copied from the thesis
        if (s > self.medulla_arc_length):
            return ((np.pi *self.base_d ** 4)/64) * (1-((1-self.conicity)/self.arc_length))
        return self.base_I * (1-((1-self.conicity)/self.arc_length))
    

    def cartesian(self):
        pass

    def __x(self, s):
        return np.cos(self.curvature(s))
        

    def __y(self, s):
        return np.sin(self.curvature(s))

    def graph(self, samples=100,tip_force_magnitude=0,tip_force_direction=0, highlight = False):
        s = 0
        phi = 0
        x=[0]
        y=[0]
        step = self.arc_length/samples
        for i in range(1,samples+1):
            s += step
            phi += self.curvature(s)*step + (step *(((self.arc_length - s) * tip_force_magnitude)/(self.youngs_modulus*self.moment_of_inertia_WRONG(s)))) * ((-tip_force_direction+90)/90)
            x.append(x[i-1]+np.cos(phi)*step)
            y.append(y[i-1]+np.sin(phi)*step)
        plt.xlim(-self.arc_length, self.arc_length)
        plt.ylim(0, self.arc_length)
        plt.plot(y,x,label="Whisker "+str(whisker.counter))
        return np.polyfit(x,y,3)
        
        
        
    def display(self):
        plt.show()

    def curvature(self, s):
        return self.A*s + self.B

    def applyTipForce(self, angle: float, magnitude: float):
        pass


