
# How to retrieve data set:

https://portal.nersc.gov/project/crcns/download/pvc-7. 
First, make sure you are have an account at at crcns.org. If you do not, you can request one https://crcns.org/request-account/fg_base_view_p3.
Download all the files in the same directory as the notebook.



## load in data set into notebook - sample code (included in the sample notebook)
With Anaconda:

conda install h5py

import h5py
filename = 'data/concat_31Hz.h5'
f = h5py.File(filename, 'r')
list(f.keys())

pvc7 = f['data']


import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as wg
from IPython.display import display
import pandas as pd

### take a look at the imaging data
def imaging(f):
    a = pvc7[f]
    plt.imshow(a, cmap='hot', interpolation='nearest')

f_slide=wg.IntSlider(min = 0, max=255255, value=0, description = 'Frame:')
wg.interact(imaging, f=f_slide)

### import stimulus data
stim = pd.read_csv("stimulus.csv")
stim