
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
    Modélistion d'un fonction affine.
    x et y sont des listes ou tableaux Numpy de même taille
    Retourne le coef. directeur a et l'ordonnée à l'origine b
    """
    a, b, _, _, _ = linregress(x,y)
    return a, b

def exp1(x, A, tau, x0=0):        
    """
    Fonction exponenetielle croissante du type
    y = A*(1-exp(-(x-xo)/tau))
    """          
    return A*(1-np.exp(-(x-x0)/tau))    

def ajustement_exp1(x, y, A0=1, tau0=1, X0=1) :
    """
    Modélisation d'une série de points (x,y) 
    par une fonction exponentielle croissante du type y = A*(1-exp(-(x-xo)/tau))
    Retourne les paramètres A, tau et xo
    """
    (A,tau,x0), pcov = curve_fit(exp1,x,y, p0=[A0, tau0, X0])
    
    return A, tau, x0