import numpy as np
import matplotlib.pyplot as plt
from deprecated import deprecated

class whisker:
    counter = 0
    def __init__(self, arc_length: float, medulla_arc_length: float, youngs_modulus: float, base_d: float, tip_d: float, medulla_base_d: float, A: float, B: float):
        """Initializes with the inputted variables.

        Args:
            arc_length (float): Total arc length of the whisker
            medulla_arc_length (float): Arc length of the medulla
            youngs_modulus (float): stress:strain (https://en.wikipedia.org/wiki/Young%27s_modulus)
            base_d (float): diameter of the whisker at the base
            tip_d (float): diameter of the whisker at the 
            medulla_base_d (float): diameter of the whisker at the base
            A (float): Cesàro variable A
            B (float): Cesàro variable B

        **Initializes:**

        self.conicity (float): 
        
        tip_d/base_d

        self.base_I (float): 
        
        cross-sectional moment of inertia at the base

        """
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
    
    def setValues(self, arc_length: float, medulla_arc_length: float, youngs_modulus: float, base_d: float, tip_d: float, medulla_base_d: float, A: float, B: float):
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
        
        """Sets instance variables with the inputted parameters. If a parameter is None, leaves it unchanged.

        Args:
            arc_length (float, optional): Total arc length of the whisker. Defaults to None.
            medulla_arc_length (float, optional): Arc length of the medulla. Defaults to None.
            youngs_modulus (float, optional): stress:strain (https://en.wikipedia.org/wiki/Young%27s_modulus). Defaults to None.
            base_d (float, optional): diameter of the whisker at the base. Defaults to None.
            tip_d (float, optional): diameter of the whisker at the base. Defaults to None.
            medulla_base_d (float, optional): diameter of the whisker at the base. Defaults to None.
            A (float, optional): Cesàro variable A. Defaults to None.
            B (float, optional): Cesàro variable B. Defaults to None.

        ## Initializes:

        **self.conicity** : *float*
        
            tip_d/base_d

        **self.base_I** : *float*
        
            cross-sectional moment of inertia at the base

        """
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

    def diameter(self, s):
        """returns the diameter d at a distance s along the curve

        Args:
            s (float): The arc-distance along the curve that is being checked

        Returns:
            float: returns the diameter at s
        """
        return self.base_d*(1-((1 - self.conicity)/self.arc_length)*s)
    
    def moment_of_inertia(self, s: float):
        """returns the moment of inertia I at a distance s along the curve

        Args:
            s (float): The arc-distance along the curve that is being checked

        Returns:
            float: returns the moment of inertia at s
        """
        # May have slight innacuracies
        if (s > self.medulla_arc_length):
            return ((np.pi *self.base_d ** 4)/64) * (1-((1-self.conicity)/self.arc_length))
        return self.base_I * (1-((1-self.conicity)/self.arc_length))
    

    def __x(self, s):
        return np.cos(self.curvature(s))
        

    def __y(self, s):
        return np.sin(self.curvature(s))

    @deprecated(reason="This function has been deprecated, use `graph` instead.", version=0.2)
    def old_graph(self, samples=100,tip_force_magnitude=0,tip_force_direction=0, plot_flag = True):
        """DEPRECATED, USE `graph` INSTEAD

        plots a curve at the specified sample resolution with the specified force applied at the tip

        Args:
            samples (int, optional): number of samples along the curve to take. Defaults to 100.
            tip_force_magnitude (float, optional): magnitude of the tip force. Defaults to 0.
            tip_force_direction (float, optional): direction of the tip force in degrees. Defaults to 0. (MAY NOT WORK FOR VALUES OTHER THAN 0 AND 180)
            plot_flag (bool, optional): whether or not to plot the curve via pyplot
            
        Returns:
            NDarray of float64: returns the 3rd degree polyfit of the curve. SEE ALSO: https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
            tuple of float: returns the (x, y) position of the tip of the whisker
        """        
        s = 0
        phi = 0
        x=[0]
        y=[0]
        step = self.arc_length/samples
        for i in range(1,samples+1):
            s += step
            phi += self.curvature(s)*step + (step *(((self.arc_length - s) * tip_force_magnitude)/(self.youngs_modulus*self.moment_of_inertia(s)))) * ((-tip_force_direction+90)/90)
            x.append(x[i-1]+np.cos(phi)*step)
            y.append(y[i-1]+np.sin(phi)*step)
        """x = -np.cos(self.curvature(s)) +1
        y = np.sin(self.curvature(s))

        print(x)
        
        if self.A==self.B and self.B==0:
            x=np.linspace(0,0, samples)
            y=s"""
        """ax = plt.figure().add_subplot()
        ax.plot(y, x, label = "Whisker")
        ax.legend()
        plt.plot(ax)
        plt.show()"""
        plt.xlim(-self.arc_length, self.arc_length)
        plt.ylim(0, self.arc_length)
        if plot_flag:
            plt.plot(y,x,label="Whisker "+str(whisker.counter))
        return np.polyfit(x,y,3), x[-1], y[-1]
        
    def graph(self, samples=100, tip_force_magnitude=0.0,tip_force_direction=0.0, distributed_magnitude=0.0,distributed_direction=0.0, distributed_function = None, plot_flag=True):
        """plots a curve at the specified sample resolution with the specified force applied at the tip

        Args:
            samples (int, optional): number of samples along the curve to take. Defaults to 100.
            tip_force_magnitude (float, optional): magnitude of the tip force. Defaults to 0.
            tip_force_direction (float, optional): direction of the tip force as the coefficient of π. Defaults to 0.
            distributed_magnitude (float, optional): magnitude of the distributed force. Defaults to 0.
            distributed_direction (float, optional): direction of the distributed force as the coefficient of π. Defaults to 0.
            distributed_function (function, optional): magnitude along curve, overrides `distributed_magnitude` if set. Defaults to `None`. 
            plot_flag (bool, optional): whether or not to plot the curve via pyplot


        Returns:
            NDarray of float64: returns the 3rd degree polyfit of the curve. SEE ALSO: https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
            tuple of float: returns the (x, y) position of the tip of the whisker
        """  
        s = 0
        curvature = self.curvature(0)
        phi = 0
        x=[0]
        y=[0]
        step = self.arc_length/samples
        for i in range(1,samples+1):
            old = curvature
            print(distributed_magnitude if not distributed_function else distributed_function(s, self.arc_length))
            curvature += step*((tip_force_magnitude*np.sin(phi+tip_force_direction) + (distributed_magnitude if not distributed_function else distributed_function(s, self.arc_length))*(1-s)*np.sin(phi+distributed_direction))/((1+(self.conicity-1)*s)**4) - ((4*(self.conicity-1))/(1+(self.conicity-1)*s))*(curvature - self.A * s - self.B) + self.A)
            phi += curvature * step 
            s += step
            x.append(x[i-1]+np.cos(phi)*step)
            y.append(y[i-1]+np.sin(phi)*step)
        plt.xlim(-self.arc_length, self.arc_length)
        plt.ylim(0, self.arc_length)
        if plot_flag:
            plt.plot(y,x,label="Whisker "+str(whisker.counter))
        return np.polyfit(x,y,3), x[-1], y[-1]

        
    def display(self):
        "runs matplotlib.pyplot.show(). displays all graphed curves."
        plt.show()

    def curvature(self, s: float):
        """returns the curvature κ at a distance s along the curve

        Args:
            s (float): The arc-distance along the curve that is being checked

        Returns:
            float: A*s + B - returns the curvature at s
        """        
        return self.A*s + self.B


