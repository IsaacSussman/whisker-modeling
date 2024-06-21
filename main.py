import numpy as np
import pandas as pd
import scipy as sp
import matplotlib as mp

import whisker

def main():
    w = whisker.whisker(1, 0, 0, 1, 0, 0, np.pi, 0)
    w.graph(1000)

if __name__ == "__main__":
    main()