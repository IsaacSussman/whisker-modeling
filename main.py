import whisker
import numpy as np
import csv
from typing import Final


def main():
    CSV_FILENAME: Final[str] = "HartmanLuoCatData.csv"

    w = whisker.whisker(55.097, 44.097, 4, 55/20.0, 0.1, 55.0/40, 0.00093152, -0.005938)
    coefficients = w.graph()
    w.graph(1000, 0.01)
    w.display()
    print(str(coefficients[0])+"x^3 + " + str(coefficients[1])+"x^2 + " + str(coefficients[2]) +"x + " + str(coefficients[3]))
    
    for i in range(1,50,1):
        w.setValues(youngs_modulus=i)
        w.graph(1000, tip_force_magnitude=0.001)
    w.display()
    
    whisker_data = []
    with open(CSV_FILENAME) as csvfile:
        spamreader = csv.reader(csvfile, quoting = csv.QUOTE_NONNUMERIC)
        for line in spamreader:
            whisker_data.append(line)

    for r in whisker_data[1:]:
        w.setValues(arc_length=r[3],A=r[13],B=r[14], base_d=0.05 * r[3], medulla_arc_length = r[3] * 0.8, medulla_base_d=0.025 * r[3])
        w.medulla_base_d = w.base_d * 0.5
        w.conicity = w.tip_d / w.base_d
        w.base_I = (np.pi * (w.base_d**4 - w.medulla_base_d**4))/64
        w.graph(100)
    w.display()

if __name__ == "__main__":
    main()

