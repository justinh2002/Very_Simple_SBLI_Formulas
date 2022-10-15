import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import scipy.integrate as integrate
import scipy.special as special
import math
from scipy import signal
import matplotlib as mlab



 def dispthickness(rho, rho_inf, u,u_inf,BLthickness):
    BLdisp = integrate.quad(lambda x: 1- (rho*u)/(rho_inf*u_inf), 0, BLthickness)
    return BLdisp
    
    
def chokedmdot(A_t,p_o,T_o):
    chokedmdot = (p_o*A_t/np.sqrt(T_o))*np.sqrt(1.4/287)
    return chokedmdot


def Schmucker(M0,M1,M2,M3,M4):
    qlist = []
    M = np.array([M0,M1,M2,M3,M4])
    for i in range(len(M)):
        qval = (1.88*M[i]-1)**(-0.64)
        qlist.append(qval)
    
    return qlist

   
   
import argparse
# ===== the following applies in case we are running this in script mode =====
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Some SBLI formulas.')
    parser.add_argument("-formula", "--formula",
                        choices=['DispThickness', 'chokedmdot', 'Schmucker'],
                        default='chokedmdot', help="Calculates this  (default: %(default)s).")
    args = parser.parse_args()

 
    if args.formula == "DispThickness":
        dispthickness(np.array(input('Enter list of densities: ')), float(input('Freestream density:'),np.array(input('Enter list of velocities: ')),float(input('Freestream velocity:') )))
 
    if args.formula == "chokedmdot":
        chokedmdot(float(input('Area of sonic region:'),float(input('Spressure in stagnation chamber:'),float(input('temperature in stagnation chamber:'))

    if args.formula == "Schmucker":
        Schmucker(float(input('M0:'),float(input('M1:'),float(input('M2:'),float(input('M3:'),float(input('M4:'))  #input Mach numbers
#clear()
