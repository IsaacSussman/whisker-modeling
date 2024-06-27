import numpy as np
import pandas as pd
import scipy as sp
import matplotlib as mp

import whisker

def main():
    w = whisker.whisker(55.097, 44.097, 3, 55/20.0, 0.1, 55.0/40, 0.00093152, -0.005938)
    w.graph(1000)    
    w.graph(1000,0.001)
    w.graph(1000,0.002)
    w.graph(1000,0.003)
    w.graph(1000,0.004)
    w.graph(1000,0.005)
    w.graph(1000,0.006)
    w.graph(1000,0.007)
    w.graph(1000,0.008)
    w.graph(1000,0.009)
    w.graph(1000,0.01)    
    w.display()

if __name__ == "__main__":
    main()