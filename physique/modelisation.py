import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.optimize import curve_fit

from physique.utils import pround_str, reduire
from physique.fonctions import *



class Modele():
    def __init__(self, function, xlim, popt, pcov, infos_dic):
        self._function = function
        self._xmin, self._xmax = xlim
        self._popt = popt
        self._pcov = pcov
        self._infos_dic = infos_dic
        self._nb_pts = 200
        self._nb_round = 5
        self._plot_label = None
        self._plot_label_latex = self._infos_dic['plot_label_latex']
        self._x = None
        self._y = None
        self._update_label()
        self._update_xy()

    def _results_format(self, params, latex):
        values = self.params()
        if latex==True:
            egale = r"$=$"
        else:
            egale = "="
        str = ''
        for i in range(len(values)):
            str = str + params[i] + egale + pround_str(values[i], self._nb_round) + "  "
        return str[:-2]


    def _update_label(self):
        if self._plot_label_latex == True:
            expression = self._infos_dic['expression_latex']
            resultats = self._results_format(self._infos_dic['popt_names_latex'], True)
            self._plot_label =  expression + '\n' + resultats
        else:
            expression = self._infos_dic['expression_text']
            resultats = self._results_format(self._infos_dic['popt_names_text'], False)
            self._plot_label = expression + '\n' + resultats
        
    def _update_xy(self):
        self._x = np.linspace(self._xmin, self._xmax, self._nb_pts)
        self._y = self._function(self._x, *self._popt)
     
    def get_xmin(self):
        return self._xmin

    def set_xmin(self, min):
        if min < self._xmax:
            self._xmin = min
            self._update_xy()
        
    def get_xmax(self):
        return self._xmax
        
    def set_xmax(self, max):
        if max > self._xmin:
            self._xmax = max
            self._update_xy()
            
    def get_nb_pts(self):
        return self._nb_pts
        
    def set_nb_pts(self, nb):
        self._nb_pts = nb
        self._update_xy()

    def get_nb_round(self):
        return self._nb_round
    
    def set_nb_round(self, nb):
        self._nb_round = nb
        self._update_label()

    def get_label_latex(self):
        return self._plot_label_latex
    
    def set_label_latex(self, val:bool):
        self._plot_label_latex = val
        self._update_label()

    def params(self):
        return self._popt
    
    def pcov(self):
        return self._pcov
    
    def xy(self):
        return self._x, self._y
    
    #def perror(self):
    #    return np.sqrt(np.diag(self._pcov))
    
    def __str__(self):
        methode = "Method   : " + self._infos_dic['method']
        fonction = self._infos_dic['function']
        expression = self._infos_dic['expression_text']
        resultats = self._results_format(self._infos_dic['popt_names_text'], False)
        return methode + '\n' + fonction + '\n' + expression + '\n' + resultats
        
    def plot(self, *args, **kargs):
        ax = plt.gca()
        if 'label' in kargs.keys():
            line = ax.plot(self._x, self._y, *args, **kargs)
        else:
            line = ax.plot(self._x, self._y, *args, label=self._plot_label, **kargs)
        return line[0]
    




    
###########################################################
#              FONCTIONS CLASSIQUES                       #
###########################################################
    
# Ajustement suivant une fonction linéaire
def ajustement_lineaire(x, y, borne_inf=None, borne_sup=None, k0=1):
    
    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(lineaire, x, y, p0=[k0])  
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'function'        : 'Modélisation suivant une fonction linéaire',
        'expression_text' : 'y = k*x',
        'expression_latex': r"$y=k\cdot x$",
        'popt_names_text' : ['k'],
        'popt_names_latex': ['$k$'],
        'plot_label_latex': True
        }
    return Modele(lineaire, xlim, popt, pcov, infos_dic)


# Ajustement suivant une fonction affine
def ajustement_affine(x, y, borne_inf=None, borne_sup=None, a0=1, b0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(affine, x, y, p0=[a0, b0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'function'        : 'Modélisation suivant une fonction affine',
        'expression_text' : 'y = a*x + b',
        'expression_latex': r'$y=a\cdot x + b$',
        'popt_names_text' : ['a', 'b'],
        'popt_names_latex': ['$a$', '$b$'],
        'plot_label_latex': True
        }
    return Modele(affine, xlim, popt, pcov, infos_dic)



# Ajustement suivant une fonction parabolique
def ajustement_parabolique(x, y, borne_inf=None, borne_sup=None, a0=1, b0=1, c0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(parabole, x, y, p0=[a0, b0, c0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'function'        : 'Modélisation suivant une fonction parabolique',
        'expression_text' : 'y = a*x^2 + b*x + c',
        'expression_latex': r"$y=a\cdot x^2+b\cdot x+c$",
        'popt_names_text' : ['a', 'b', 'c'],
        'popt_names_latex': ['$a$', '$b$', '$c$'],
        'plot_label_latex': True
        }
    return Modele(parabole, xlim, popt, pcov, infos_dic)




# Ajustement suivant une fonction exponentielle croissante
def ajustement_exponentielle_croissante(x, y, borne_inf=None, borne_sup=None, A0=1, tau0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(exponentielle_croissante, x, y, p0=[A0, tau0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'function'        : 'Modélisation suivant une fonction exponentielle croissante',
        'expression_text' : 'y = A*(1-exp(-x/tau))',
        'expression_latex': r'$y=A\cdot(1-e^{-x/\tau})$',
        'popt_names_text' : ['A', 'tau'],
        'popt_names_latex': ['$A$', r'$\tau$'],
        'plot_label_latex': True
        }
    return Modele(exponentielle_croissante, xlim, popt, pcov, infos_dic)


def ajustement_exponentielle_decroissante(x, y, borne_inf=None, borne_sup=None, A0=1, tau0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(exponentielle_decroissante, x, y, p0=[A0, tau0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'function'        : 'Modélisation suivant une fonction exponentielle décroissante',
        'expression_text' : 'y = A*exp(-x/tau)',
        'expression_latex': r'$y=A\cdot e^{-x/\tau}$',
        'popt_names_text' : ['A', 'tau'],
        'popt_names_latex': ['$A$', r'$\tau$'],
        'plot_label_latex': True
        }
    return Modele(exponentielle_decroissante, xlim, popt, pcov, infos_dic)


def ajustement_exponentielle2_croissante(x, y, borne_inf=None, borne_sup=None, A0=1, k0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(exponentielle2_croissante, x, y, p0=[A0, k0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'function'        : 'Modélisation suivant une fonction exponentielle croissante',
        'expression_text' : 'y = A*(1-exp(-k*x))',
        'expression_latex': r'$y=A\cdot(1-e^{-k\cdot x})$',
        'popt_names_text' : ['A', 'k'],
        'popt_names_latex': ['$A$', '$k$'],
        'plot_label_latex': True
        }
    return Modele(exponentielle2_croissante, xlim, popt, pcov, infos_dic)


def ajustement_exponentielle2_decroissante(x, y, borne_inf=None, borne_sup=None, A0=1, k0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(exponentielle2_decroissante, x, y, p0=[A0, k0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'function'        : 'Modélisation suivant une fonction exponentielle décroissante',
        'expression_text' : 'y = A*exp(-k*x)',
        'expression_latex': r'$y=A\cdot e^{-k\cdot x}$',
        'popt_names_text' : ['A', 'k'],
        'popt_names_latex': ['$A$', '$k$'],
        'plot_label_latex': True
        }
    return Modele(exponentielle2_decroissante, xlim, popt, pcov, infos_dic)



def ajustement_puissance(x, y, borne_inf=None, borne_sup=None, A0=1, n0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(puissance, x, y, p0=[A0, n0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'function'        : 'Modélisation suivant une fonction puissance',
        'expression_text' : 'y = A*x^n',
        'expression_latex': r'$y=A\cdot x^n$',
        'popt_names_text' : ['A', 'n'],
        'popt_names_latex': ['$A$', '$n$'],
        'plot_label_latex': True
        }
    return Modele(puissance, xlim, popt, pcov, infos_dic)


###########################################################
#                       FILTRES                           #
###########################################################



