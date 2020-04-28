
# How to retrieve data set:


First, make sure you are have an account at at crcns.org. If you do not, you can request one https://crcns.org/request-account/fg_base_view_p3.  

Download all the data files in the same directory at the same level as the notebook.
https://portal.nersc.gov/project/crcns/download/pvc-7.   

Sample notebook is in the top level of the repository and is named "pvc7_test_cl5th.ipynb"  
  
Only the following files were used in the sample notebook:  

    - concat_31Hz.h5  
    
    - stimulus.csv  
    


## load in data set into notebook - sample code (included in the sample notebook)

- With Anaconda:  

conda install h5py # if you haven't installed h5py yet.   

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
