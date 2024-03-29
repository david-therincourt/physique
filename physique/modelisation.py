import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import scipy.stats as sstats
from scipy.optimize import curve_fit

from physique.utils import pround, reduire
from physique.fonctions import *



class Modele():
    def __init__(self, xy_data, function, xlim, popt, pcov, infos_dic):
        self._xdata, self._ydata = xy_data
        self._function = function
        self._xmin, self._xmax = xlim
        self._popt = popt
        self._pcov = pcov
        self._infos_dic = infos_dic
        self._nb_pts = 200
        self._nb_round = 3
        self._plot_label = None
        self._plot_label_type = self._infos_dic['plot_label_type']
        self._print_error = True
        self._niv_confiance = 0.95
        self._x = None
        self._y = None
        self._update_label()
        self._update_xy()

    def _results_format(self, params, latex):
        values = self.params()
        errors = self.perror()
        if latex==True:
            egale = r"$=$"
        else:
            egale = "="
        str = ''
        if self._print_error==False:
            for i in range(len(values)):
                str = str + params[i] + egale + pround(values[i], self._nb_round) + "  "
        else:
            for i in range(len(values)):
                str = str + params[i] + egale + pround(values[i], self._nb_round) + " \xb1" + pround(errors[i],2) + " | "
        return str[:-3]


    def _update_label(self):
        if self._plot_label_type == "text":
            expression = self._infos_dic['expression_text']
            resultats = self._results_format(self._infos_dic['popt_names_text'], False)
            self._plot_label = expression + '\n' + resultats
        elif self._plot_label_type == "latex":
            expression = self._infos_dic['expression_latex']
            resultats = self._results_format(self._infos_dic['popt_names_latex'], True)
            self._plot_label =  expression + '\n' + resultats
        elif self._plot_label_type == "name":
            expression = self._infos_dic['expression_name']
            #resultats = self._results_format(self._infos_dic['popt_names_text'], False)
            self._plot_label = expression
        
        
    def _update_xy(self):
        if self._infos_dic['xlogspace'] == True:
            self._x = np.logspace(np.log10(self._xmin), np.log10(self._xmax), self._nb_pts)
            self._y = self._function(self._x, *self._popt)
        else:
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

    def get_print_error(self):
        return self._print_error
    
    def set_print_error(self, val:bool):
        self._print_error = val
        self._update_label()

    def get_niveau_confiance(self):
        return self._niv_confiance
    
    def set_niveau_confiance(self, val:float):
        self._niv_confiance = val
        self._update_label()

    def get_plot_label_type(self):
        return self._plot_label_type
    
    def set_plot_label_type(self, val:bool):
        self._plot_label_type = val
        self._update_label()

    def params(self):
        return self._popt
    
    def pcov(self):
        return self._pcov
    
    def xy(self):
        return self._x, self._y
    
    def perror(self):
        u = np.sqrt(np.diag(self._pcov))
        n, p = len(self._xdata), len(self._popt)
        ts = sstats.t.ppf(1-(1-self._niv_confiance)/2, n-p)
        return ts*u

    
    def __str__(self):
        methode = "Method   : " + self._infos_dic['method']
        fonction = self._infos_dic['expression_name']
        expression = self._infos_dic['expression_text']
        resultats = self._results_format(self._infos_dic['popt_names_text'], False)
        confiance = "Avec un intervalle de confiance de " + str(int(self._niv_confiance*100)) + "%"
        return methode + '\n' + fonction + '\n' + expression + '\n' + resultats + '\n' + confiance
        
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
def ajustement_lineaire(x, y, borne_inf=None, borne_sup=None, a0=1):
    
    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(lineaire, x, y, p0=[a0])  
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : 'Fonction linéaire',
        'expression_text' : 'y = a*x',
        'expression_latex': r"$y=a\cdot x$",
        'popt_names_text' : ['a'],
        'popt_names_latex': ['$a$'],
        'plot_label_type' : 'latex',
        'xlogspace'       : False
        }
    return Modele((x,y),lineaire, xlim, popt, pcov, infos_dic)


# Ajustement suivant une fonction affine
def ajustement_affine(x, y, borne_inf=None, borne_sup=None, a0=1, b0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(affine, x, y, p0=[a0, b0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : 'Fonction affine',
        'expression_text' : 'y = a*x + b',
        'expression_latex': r'$y=a\cdot x + b$',
        'popt_names_text' : ['a', 'b'],
        'popt_names_latex': ['$a$', '$b$'],
        'plot_label_type' : 'latex',
        'xlogspace'       : False
        }
    return Modele((x,y), affine, xlim, popt, pcov, infos_dic)



# Ajustement suivant une fonction parabolique
def ajustement_parabolique(x, y, borne_inf=None, borne_sup=None, a0=1, b0=1, c0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(parabole, x, y, p0=[a0, b0, c0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : 'Fonction parabolique',
        'expression_text' : 'y = a*x^2 + b*x + c',
        'expression_latex': r"$y=a\cdot x^2+b\cdot x+c$",
        'popt_names_text' : ['a', 'b', 'c'],
        'popt_names_latex': ['$a$', '$b$', '$c$'],
        'plot_label_type' : 'latex',
        'xlogspace'       : False
        }
    return Modele((x,y),parabole, xlim, popt, pcov, infos_dic)




# Ajustement suivant une fonction exponentielle croissante
def ajustement_exponentielle_croissante(x, y, borne_inf=None, borne_sup=None, A0=1, tau0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(exponentielle_croissante, x, y, p0=[A0, tau0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : 'Fonction exponentielle croissante',
        'expression_text' : 'y = A*(1-exp(-x/tau))',
        'expression_latex': r'$y=A\cdot(1-e^{-x/\tau})$',
        'popt_names_text' : ['A', 'tau'],
        'popt_names_latex': ['$A$', r'$\tau$'],
        'plot_label_type' : 'latex',
        'xlogspace'       : False
        }
    return Modele((x,y),exponentielle_croissante, xlim, popt, pcov, infos_dic)


def ajustement_exponentielle_decroissante(x, y, borne_inf=None, borne_sup=None, A0=1, tau0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(exponentielle_decroissante, x, y, p0=[A0, tau0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : 'Fonction exponentielle décroissante',
        'expression_text' : 'y = A*exp(-x/tau)',
        'expression_latex': r'$y=A\cdot e^{-x/\tau}$',
        'popt_names_text' : ['A', 'tau'],
        'popt_names_latex': ['$A$', r'$\tau$'],
        'plot_label_type' : 'latex',
        'xlogspace'       : False
        }
    return Modele(exponentielle_decroissante, xlim, popt, pcov, infos_dic)


def ajustement_exponentielle2_croissante(x, y, borne_inf=None, borne_sup=None, A0=1, k0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(exponentielle2_croissante, x, y, p0=[A0, k0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : 'Fonction exponentielle croissante',
        'expression_text' : 'y = A*(1-exp(-k*x))',
        'expression_latex': r'$y=A\cdot(1-e^{-k\cdot x})$',
        'popt_names_text' : ['A', 'k'],
        'popt_names_latex': ['$A$', '$k$'],
        'plot_label_type' : 'latex',
        'xlogspace'       : False
        }
    return Modele((x,y),exponentielle2_croissante, xlim, popt, pcov, infos_dic)


def ajustement_exponentielle2_decroissante(x, y, borne_inf=None, borne_sup=None, A0=1, k0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(exponentielle2_decroissante, x, y, p0=[A0, k0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : 'Fonction exponentielle décroissante',
        'expression_text' : 'y = A*exp(-k*x)',
        'expression_latex': r'$y=A\cdot e^{-k\cdot x}$',
        'popt_names_text' : ['A', 'k'],
        'popt_names_latex': ['$A$', '$k$'],
        'plot_label_type' : 'latex',
        'xlogspace'       : False
        }
    return Modele((x,y),exponentielle2_decroissante, xlim, popt, pcov, infos_dic)



def ajustement_puissance(x, y, borne_inf=None, borne_sup=None, A0=1, n0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(puissance, x, y, p0=[A0, n0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : 'Fonction puissance',
        'expression_text' : 'y = A*x^n',
        'expression_latex': r'$y=A\cdot x^n$',
        'popt_names_text' : ['A', 'n'],
        'popt_names_latex': ['$A$', '$n$'],
        'plot_label_type' : 'latex',
        'xlogspace'       : False
        }
    return Modele((x,y),puissance, xlim, popt, pcov, infos_dic)


###########################################################
#              REPONSE ORDRE 1  - PASSE BAS               #
###########################################################
def ajustement_ordre1_passe_bas_transmittance(x, y, borne_inf=None, borne_sup=None, T0=1, f0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre1_passe_bas_transmittance, x, y, p0=[T0, f0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Transmittance - Passe bas d'ordre 1",
        'expression_text' : 'T = T0/sqrt(1+(f/f0)^2)',
        'expression_latex': r"$T = \dfrac{T_0}{\sqrt{1+(\dfrac{f}{f_0})^2}}$",
        'popt_names_text' : ['T0', 'f0'],
        'popt_names_latex': ['$T_0$', '$f_0$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre1_passe_bas_transmittance, xlim, popt, pcov, infos_dic)


def ajustement_ordre1_passe_bas_gain(x, y, borne_inf=None, borne_sup=None, G0=0, f0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre1_passe_bas_gain, x, y, p0=[G0, f0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Gain passe bas d'ordre 1",
        'expression_text' : 'G = G0 - 20*log(sqrt(1+(f/f0)^2))',
        'expression_latex': r"$G = G_0 - 20\cdot\log(\sqrt{1+(\dfrac{f}{f_0})^2})$",
        'popt_names_text' : ['G0', 'f0'],
        'popt_names_latex': ['$G_0$', '$f_0$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre1_passe_bas_gain, xlim, popt, pcov, infos_dic)



def ajustement_ordre1_passe_bas_dephasage(x, y, borne_inf=None, borne_sup=None, f0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre1_passe_bas_dephasage, x, y, p0=[f0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Déphasage passe bas d'ordre 1",
        'expression_text' : 'phi = -arctan(f/f0)',
        'expression_latex': r"$\varphi = -\arctan(\dfrac{f}{f_0})$",
        'popt_names_text' : ['f0'],
        'popt_names_latex': ['$f_0$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre1_passe_bas_dephasage, xlim, popt, pcov, infos_dic)


###########################################################
#              REPONSE ORDRE 1  - PASSE HAUT              #
###########################################################

def ajustement_ordre1_passe_haut_transmittance(x, y, borne_inf=None, borne_sup=None, T0=1, f0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre1_passe_haut_transmittance, x, y, p0=[T0, f0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Transmittance - Passe haut d'ordre 1",
        'expression_text' : 'T = T0*(f/f0)/sqrt(1+(f/f0)^2)',
        'expression_latex': r"$T = \dfrac{T_0\cdot\dfrac{f}{f_0}}{\sqrt{1+(\dfrac{f}{f_0})^2}}$",
        'popt_names_text' : ['T0', 'f0'],
        'popt_names_latex': ['$T_0$', '$f_0$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre1_passe_haut_transmittance, xlim, popt, pcov, infos_dic)


def ajustement_ordre1_passe_haut_gain(x, y, borne_inf=None, borne_sup=None, G0=0, f0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre1_passe_haut_gain, x, y, p0=[G0, f0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Gain passe haut d'ordre 1",
        'expression_text' : 'G = G0 + 20*log(f/f0) - 20*log(sqrt(1+(f/f0)^2))',
        'expression_latex': r"$G = G_0 + 20\cdot\log(\dfrac{f}{f_0})- 20\cdot\log(\sqrt{1+(\dfrac{f}{f_0})^2})$",
        'popt_names_text' : ['G0', 'f0'],
        'popt_names_latex': ['$G_0$', '$f_0$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre1_passe_haut_gain, xlim, popt, pcov, infos_dic)



def ajustement_ordre1_passe_haut_dephasage(x, y, borne_inf=None, borne_sup=None, f0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre1_passe_haut_dephasage, x, y, p0=[f0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Déphasage passe haut d'ordre 1",
        'expression_text' : 'phi = 90 - arctan(f/f0)',
        'expression_latex': r"$\varphi = 90 -\arctan(\dfrac{f}{f_0})$",
        'popt_names_text' : ['f0'],
        'popt_names_latex': ['$f_0$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre1_passe_haut_dephasage, xlim, popt, pcov, infos_dic)



###########################################################
#              REPONSE ORDRE 2  - PASSE BAS               #
###########################################################
def ajustement_ordre2_passe_bas_transmittance(x, y, borne_inf=None, borne_sup=None, T0=1, f0=1, m0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre2_passe_bas_transmittance, x, y, p0=[T0, f0, m0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Transmittance - Passe bas d'ordre 2",
        'expression_text' : "T = T0/sqrt((1-(f/f0)^2)^2+(2*m*f/f0)^2)",
        'expression_latex': r"$T = \dfrac{T_0}{\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2}}$",
        'popt_names_text' : ['T0', 'f0', 'm'],
        'popt_names_latex': ['$T_0$', '$f_0$', '$m$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre2_passe_bas_transmittance, xlim, popt, pcov, infos_dic)


def ajustement_ordre2_passe_bas_gain(x, y, borne_inf=None, borne_sup=None, G0=0, f0=1, m0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre2_passe_bas_gain, x, y, p0=[G0, f0, m0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Gain - Passe bas d'ordre 2",
        'expression_text' : 'G = G0 + 20*log((f/f0)^2) - 20*log(sqrt((1-(f/f0)^2)^2+(2*m*f/f0)^2))',
        'expression_latex': r"$G = G_0 - 20\cdot\log(\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2})$",
        'popt_names_text' : ['G0', 'f0', 'm'],
        'popt_names_latex': ['$G_0$', '$f_0$', '$m$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre2_passe_bas_gain, xlim, popt, pcov, infos_dic)



def ajustement_ordre2_passe_bas_dephasage(x, y, borne_inf=None, borne_sup=None, f0=1, m0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre2_passe_bas_dephasage, x, y, p0=[f0, m0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Déphasage - Passe bas d'ordre 2",
        'expression_text' : 'phi = 180 - arctan((2*m*f/f0)/(1-(f/f0)^2))',
        'expression_latex': r"$\varphi = -\arctan(\dfrac{2m\dfrac{f}{f_0}}{1-\dfrac{f^2}{f_0^2}})$",
        'popt_names_text' : ['f0', 'm'],
        'popt_names_latex': ['$f_0$', '$m$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre2_passe_bas_dephasage, xlim, popt, pcov, infos_dic)


###########################################################
#              REPONSE ORDRE 2  - PASSE HAUT              #
###########################################################
def ajustement_ordre2_passe_haut_transmittance(x, y, borne_inf=None, borne_sup=None, T0=1, f0=1, m0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre2_passe_haut_transmittance, x, y, p0=[T0, f0, m0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Transmittance - Passe haut d'ordre 2",
        'expression_text' : "T = T0*(f/f0)^2/sqrt((1-(f/f0)^2)^2+(2*m*f/f0)^2)",
        'expression_latex': r"$T = \dfrac{T_0\cdot\dfrac{f^2}{f_0^2}}{\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2}}$",
        'popt_names_text' : ['T0', 'f0', 'm'],
        'popt_names_latex': ['$T_0$', '$f_0$', '$m$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre2_passe_haut_transmittance, xlim, popt, pcov, infos_dic)


def ajustement_ordre2_passe_haut_gain(x, y, borne_inf=None, borne_sup=None, G0=0, f0=1, m0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre2_passe_haut_gain, x, y, p0=[G0, f0, m0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Gain - Passe haut d'ordre 2",
        'expression_text' : 'G = G0 + 20*log((f/f0)^2) - 20*log(sqrt((1-(f/f0)^2)^2+(2*m*f/f0)^2))',
        'expression_latex': r"$G = G_0 + 20\cdot\log(\dfrac{f^2}{f_0^2})- 20\cdot\log(\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2})$",
        'popt_names_text' : ['G0', 'f0', 'm'],
        'popt_names_latex': ['$G_0$', '$f_0$', '$m$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre2_passe_haut_gain, xlim, popt, pcov, infos_dic)



def ajustement_ordre2_passe_haut_dephasage(x, y, borne_inf=None, borne_sup=None, f0=1, m0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre2_passe_haut_dephasage, x, y, p0=[f0, m0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Déphasage - Passe haut d'ordre 2",
        'expression_text' : 'phi = 180 - arctan((2*m*f/f0)/(1-(f/f0)^2))',
        'expression_latex': r"$\varphi = 180 -\arctan(\dfrac{2m\dfrac{f}{f_0}}{1-\dfrac{f^2}{f_0^2}})$",
        'popt_names_text' : ['f0', 'm'],
        'popt_names_latex': ['$f_0$', '$m$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre2_passe_haut_dephasage, xlim, popt, pcov, infos_dic)


###########################################################
#              REPONSE ORDRE 2  - PASSE BANDE             #
###########################################################
def ajustement_ordre2_passe_bande_transmittance(x, y, borne_inf=None, borne_sup=None, T0=1, f0=1, m0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre2_passe_bande_transmittance, x, y, p0=[T0, f0, m0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Transmittance - Passe bande d'ordre 2",
        'expression_text' : "T = T0*2*m*(f/f0)/sqrt((1-(f/f0)^2)^2+(2*m*f/f0)^2)",
        'expression_latex': r"$T = T_0\cdot\dfrac{2m\cdot\dfrac{f}{f_0}}{\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2}}$",
        'popt_names_text' : ['T0', 'f0', 'm'],
        'popt_names_latex': ['$T_0$', '$f_0$', '$m$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre2_passe_bande_transmittance, xlim, popt, pcov, infos_dic)


def ajustement_ordre2_passe_bande_gain(x, y, borne_inf=None, borne_sup=None, G0=0, f0=1, m0=1):

    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre2_passe_bande_gain, x, y, p0=[G0, f0, m0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Gain - Passe bande d'ordre 2",
        'expression_text' : 'G = G0 + 20*log(2*m*f/f0) - 20*log(sqrt((1-(f/f0)^2)^2+(2*m*f/f0)^2))',
        'expression_latex': r"$G = G_0 + 20\cdot\log(2m\dfrac{f}{f_0})- 20\cdot\log(\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2})$",
        'popt_names_text' : ['G0', 'f0', 'm'],
        'popt_names_latex': ['$G_0$', '$f_0$', '$m$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre2_passe_bande_gain, xlim, popt, pcov, infos_dic)



def ajustement_ordre2_passe_bande_dephasage(x, y, borne_inf=None, borne_sup=None, f0=1, m0=1):
    # Problème décalage pour f=f0
    x, y, xlim = reduire(x, y, borne_inf, borne_sup)
    popt, pcov  = curve_fit(ordre2_passe_bande_dephasage, x, y, p0=[f0, m0])
    infos_dic = {
        'method'          : 'scipy.optimize.curve_fit',
        'expression_name' : "Déphasage - Passe bande d'ordre 2",
        'expression_text' : 'phi = 90 - arctan((2*m*f/f0)/(1-(f/f0)^2)) [-180 si f>f0]',
        'expression_latex': r"$\varphi = 90 -\arctan(\dfrac{2m\dfrac{f}{f_0}}{1-\dfrac{f^2}{f_0^2}}) [-180~si~f>f_0]$",
        'popt_names_text' : ['f0', 'm'],
        'popt_names_latex': ['$f_0$', '$m$'],
        'plot_label_type' : 'name',
        'xlogspace'       : True 
        }
    return Modele((x,y),ordre2_passe_bande_dephasage, xlim, popt, pcov, infos_dic)