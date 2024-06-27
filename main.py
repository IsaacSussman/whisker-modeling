import numpy as np
import pandas as pd
import scipy as sp
import matplotlib as mp

import whisker

def main():
    w = whisker.whisker(1, 0, 1, 1, 1, 0.1, np.pi, 0)
    w.graph(1000)    
    w.graph(1000,0.01)    

if __name__ == "__main__":
    main()