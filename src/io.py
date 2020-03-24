# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
from __future__ import print_function, division, absolute_import

import h5py
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as wg
from IPython.display import display
import pandas as pd


filename = 'data/concat_31Hz.h5'
f = h5py.File(filename, 'r')
list(f.keys())

pvc7 = f['data']

# ### take a look at the imaging data
# def imaging(f):
#     a = pvc7[f]
#     plt.imshow(a, cmap='hot', interpolation='nearest')

# f_slide=wg.IntSlider(min = 0, max=255255, value=0, description = 'Frame:')
# wg.interact(imaging, f=f_slide)

### import stimulus data
stim = pd.read_csv("stimulus.csv")
# stim


# def read_neuron(id, param_1=default_1):
#    """Describe what the arguments of the function mean and what the function returns"""
#    body_of_the_function