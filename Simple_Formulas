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

clear()
