import numpy as np
import pandas as pd
import scipy as sp
import matplotlib as mp

import whisker

def main():
    w = whisker.whisker(55.097, 44.097, 3, 55/20.0, 0.1, 55.0/40, 0.00093152, -0.005938)
    w.graph(1000)    
    w.graph(1000,0.001)    
    w.display()

if __name__ == "__main__":
    main()