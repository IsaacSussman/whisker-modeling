import numpy as np
import pandas as pd
import scipy as sp
import matplotlib as mp
import csv

import whisker

def main():
    CSV_FILENAME = "Unified BS.csv"
    w = whisker.whisker(55.097, 44.097, 4, 55/20.0, 0.1, 55.0/40, 0.00093152, -0.005938)
    for i in range(0,int((55/20.0)*100+5),5):
        w.medulla_base_d = i/100
        w.graph(1000, tip_force_magnitude=0.001)
    w.display()
    
    whisker_data = []
    with open(CSV_FILENAME) as csvfile:
        spamreader = csv.reader(csvfile, quoting = csv.QUOTE_NONNUMERIC)
        for line in spamreader:
            whisker_data.append(line)
    for r in whisker_data[1:10]:
        w.arc_length = r[3]
        w.A = r[13]
        w.B = r[14]
        w.base_d = 0.05 * w.arc_length
        w.medulla_arc_length = w.arc_length * 0.8
        w.medulla_base_d = w.base_d * 0.5
        w.conicity = w.tip_d / w.base_d
        w.base_I = (np.pi * (w.base_d**4 - w.medulla_base_d**4))/64
        w.graph(100, tip_force_magnitude=0.001)
        
    w.display()



    w.display()

if __name__ == "__main__":
    main()