import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.optimize import curve_fit

from physique.utils import pround_str, reduire
from physique.fonctions import *



class Modele():
    def __init__(self, function, xlim, popt, pcov, infos_dic):
        self._function = function
        self._xmin = xlim[0]
        self._xmax = xlim[1]
        self._popt = popt
        self._pcov = pcov
        self._infos_dic = infos_dic
        self._nb_pts = 200
        self._nb_round = 5
        self._plot_label_latex = self._infos_dic['plot_label_latex']
        self._plot_label = None
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
    
    def set_label_latex(self, val):
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
        'popt_names_latex': [r'$k$'],
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
        'expression_latex': r'$y=a \cdot x + b$',
        'popt_names_text' : ['a', 'b'],
        'popt_names_latex': [r'$a$', r'$b$'],
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
        'popt_names_latex': [r'$a$', r'$b$', r'$c$'],
        'plot_label_latex': True
        }

    return Modele(parabole, xlim, popt, pcov, infos_dic)




# # Ajustement suivant une fonction exponentielle croissante
# def ajustement_exponentielle_croissante(x, y, borne_inf=None, borne_sup=None, p0:"list"=[1,1]):
    
#     global n
    
#     x, y, inf, sup = reduire(x, y, borne_inf, borne_sup)

#     (A,tau), pcov  = curve_fit(exponentielle_croissante, x, y, p0=p0)
    
#     text = "y = A*(1-exp(-x/tau))" + "\n" + "A=" + pround_str(A,n) + "  tau=" + pround_str(tau,n)
#     latex = r"$y=A\cdot(1-e^{-x/\tau})$"+ "\n" + r"$A=$" + pround_str(A,n) + r"  $\tau=$" + pround_str(tau,n)

#     return Modele((x, y), (inf, sup), "scipy.optimize.curve_fit", exponentielle_croissante, (A,tau), pcov, (text, latex))


# # Ajustement suivant une fonction exponentielle croissante translatée
# def ajustement_exponentielle_croissante_x0(x, y, borne_inf=None, borne_sup=None, p0:"list"=[1,1,1]):
    
#     global n
    
#     x, y, inf, sup = reduire(x, y, borne_inf, borne_sup)

#     (A,tau,x0), pcov  = curve_fit(exponentielle_croissante_x0, x, y, p0=p0)
    
#     text = "y = A*(1-exp(-(x-x0)/tau))" + "\n" + "A=" + pround_str(A,n) + "  tau=" + pround_str(tau,n)+ "  x0=" + pround_str(x0,n)
#     latex = r"$y=A\cdot(1-e^{-(x-x_0)/\tau})$"+ "\n" + r"$A=$" + pround_str(A,n) + r"  $\tau=$" + pround_str(tau,n) + r"  $x_0=$" + pround_str(x0,n)

#     return Modele((x, y), (inf, sup), "scipy.optimize.curve_fit", exponentielle_croissante_x0, (A,tau,x0), pcov, (text, latex))




# # Ajustement suivant une fonction exponentielle décroissante
# def ajustement_exponentielle_decroissante(x, y, borne_inf=None, borne_sup=None, p0:"list"=[1,1]):
    
#     global n
    
#     x, y, inf, sup = reduire(x, y, borne_inf, borne_sup)

#     (A,tau), pcov  = curve_fit(exponentielle_decroissante, x, y, p0=p0)
    
#     text = "y = A*exp(-x/tau)" + "\n" + "A=" + pround_str(A,n) + "  tau=" + pround_str(tau,n)
#     latex = r"$y=A\cdot e^{-x/\tau}$"+ "\n" + r"$A=$" + pround_str(A,n) + r"  $\tau=$" + pround_str(tau,n)

#     return Modele((x, y), (inf, sup), "scipy.optimize.curve_fit", exponentielle_decroissante, (A,tau), pcov, (text, latex))


# # # Ajustement suivant une fonction exponentielle décroissante translatée
# # def ajustement_exponentielle_decroissante_x0(x, y, borne_inf=None, borne_sup=None, A_p0:"float"=1, tau_p0:"float"=1, x0_p0:"float"=0):

# #     global n
# #     x, y, borne_inf, borne_sup= reduire(x, y, borne_inf, borne_sup)
# #     (A,tau,x0), pcov  = curve_fit(exponentielle_decroissante_x0, x, y, p0=[A_p0, tau_p0, x0_p0])

# #     text = "y = A*exp(-(x-x0)/tau)" + "\n" + "A=" + pround_str(A,n) + "  tau=" + pround_str(tau,n)+ "  x0=" + pround_str(x0,n)
# #     latex = r"$y=A\cdot e^{-(x-x_0)/\tau}$"+ "\n" + r"$A=$" + pround_str(A,n) + r"  $\tau=$" + pround_str(tau,n) + r"  $x_0=$" + pround_str(x0,n)

# #     return Modele(x, y, borne_inf, borne_sup, exponentielle_decroissante_x0, (A,tau,x0), pcov, (text, latex))



# # Ajustement suivant une fonction exponentielle 2 croissante
# def ajustement_exponentielle2_croissante(x, y, borne_inf=None, borne_sup=None, p0:"list"=[1,1]):
    
#     global n
#     x, y, inf, sup = reduire(x, y, borne_inf, borne_sup)

#     (A,k), pcov  = curve_fit(exponentielle2_croissante, x, y, p0=p0)
    
#     text = "y = A*(1-exp(-k*x))" + "\n" + "A=" + pround_str(A,n) + "  k=" + pround_str(k,n)
#     latex = r"$y=A\cdot(1-e^{-k\cdot x})$"+ "\n" + r"$A=$" + pround_str(A,n) + r"  $k=$" + pround_str(k,n)

#     return Modele((x, y), (inf, sup), "scipy.optimize.curve_fit", exponentielle2_croissante, (A,k), pcov, (text, latex))


# # Ajustement suivant une fonction exponentielle croissante translatée
# def ajustement_exponentielle2_croissante_x0(x, y, borne_inf=None, borne_sup=None, p0:"list"=[1,1,1]):
    
#     global n
    
#     x, y, inf, sup = reduire(x, y, borne_inf, borne_sup)

#     (A,k,x0), pcov  = curve_fit(exponentielle2_croissante_x0, x, y, p0=p0)
    
#     text = "y = A*(1-exp(-k*(x-x0)))" + "\n" + "A=" + pround_str(A,n) + "  k=" + pround_str(k,n)+ "  x0=" + pround_str(x0,n)
#     latex = r"$y=A\cdot(1-e^{-k\dot(x-x_0)})$"+ "\n" + r"$A=$" + pround_str(A,n) + r"  $k=$" + pround_str(k,n) + r"  $x_0=$" + pround_str(x0,n)

#     return Modele((x, y), (inf, sup), "scipy.optimize.curve_fit", exponentielle2_croissante_x0, (A,k,x0), pcov, (text, latex))




# # Ajustement suivant une fonction exponentielle décroissante
# def ajustement_exponentielle2_decroissante(x, y, borne_inf=None, borne_sup=None, p0:"list"=[1,1]):
    
#     global n
    
#     x, y, inf, sup = reduire(x, y, borne_inf, borne_sup)

#     (A,k), pcov  = curve_fit(exponentielle2_decroissante, x, y, p0=p0)
    
#     text = "y = A*exp(-k*x)" + "\n" + "A=" + pround_str(A,n) + "  k=" + pround_str(k,n)
#     latex = r"$y=A\cdot e^{-k\cdot x}$"+ "\n" + r"$A=$" + pround_str(A,n) + r"  $k=$" + pround_str(k,n)

#     return Modele((x, y), (inf, sup), "scipy.optimize.curve_fit", exponentielle2_decroissante, (A,k), pcov, (text, latex))