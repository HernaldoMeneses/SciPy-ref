''''
    Scipy is a collection of mathmatical algorithms and convenience function built on the Numpy extension of Python.
    Providing high-level commands and classes for manipulating and visualizing data.
'''

##Is all begining here and this way...
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

#1.1.1- SciPy Organization
'''
    Scipy is organized into subpackages covering diferrent scintific computing domains.
    following the key summarized
'''

SciPY_Organization = {
    'cluster':'Cluestering algorihms',
    'constants':'Physical and mathematical constants',
    'fftpack':'Fast Fourier Transform routines',
    'integrate':'Integration and ordinaty differential equation solvers',
    'interpolate':'Interpolation and smoothing splines',
    'io':'Input and Output',
    'linalg':'Linear algebra',
    'ndimage':'N-dimensional image processing',
    'odr':'Orthogonal distance regression',
    'optimize':'Optimization and root-finding routines',
    'signal':'Signal processing',
    'sparse':'Sparse matrices and associeted routines',
    'spatial':'Spatial data structures and algorithms',
    'special':'Special functions',
    'stats':'Statistical distibuitions and functions',
    'weave':'C/C++ integration',
}

'''
    Find documentation
    http://docs.scipy.org/
'''

import pandas as pd
# Criar DataFrame
df = pd.DataFrame(list(SciPY_Organization.items()), columns=['Subpackage', 'Description'])

# Exibir DataFrame
print(df)

#Simple Ex
from scipy import linalg, optimize

'''
    Because of their ubiquitousness, some of the functions in these subpackages are also made available in the scipy namespace to ease ther use in interactive sessions and programs.
    Before looking at the sub-packages individually, we will first look at some of these common functions in basic array functions from numpy
'''

#1.1.2 Finding Documentation
#pag.8/1229
#file:///L:/Linear_/Base-TI/scipy-ref.pdf