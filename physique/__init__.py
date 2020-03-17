# -*- coding: utf-8 -*-
"""
Module Python 3 pour les sciences physiques au lycée.

@author: David Thérincourt
"""

import numpy as np
from scipy.stats import linregress
from scipy.optimize import curve_fit

def ajustement_affine(x, y):
    """
    Modélisation d'une fonction affine y = a*x + b
    x : liste ou tableau Numpy.
    y : liste ou tableau Numpy de même dimension que x.
    """
    a, b, _, _, _ = linregress(x,y)
    return a, b

def exp1(x, A, tau, x0=0):        
    """
    Fonction exponenetielle croissante y = A*(1-exp(-(x-x0)/tau))
    x   : liste ou tableau Numpy.
    A   : valeur à l'infini de y
    tau : constante de temps
    x0  : retard
    """          
    return A*(1-np.exp(-(x-x0)/tau))    

def ajustement_exp1(x, y, A0=1, tau0=1, X0=0) :
    """
    Modélisation d'une série de points (x,y) par une fonction
    exponentielle croissante du type y = A*(1-exp(-(x-xo)/tau))
    x : liste ou tableau Numpy.
    y : liste ou tableau Numpy de même dimension que x.
    A0, tau0 et X0 : optionnels
    Retourne (A, tau, x0)
    """
    (A,tau,x0), pcov = curve_fit(exp1,x,y, p0=[A0, tau0, X0])
    return A, tau, x0