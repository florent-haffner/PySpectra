import pandas as pd
import numpy as np
import spc

# Load data
f=spc.File('sample_spectra/VIAVI/JDSU_Phar_Rotate_S06_1_20171009_1540.spc')


df_spc, dict_spc=ReadFromDir('sample_spectra/VIAVI')

msc=MSC()
msc.fit(df_spc)
B=msc.fit_transform(df_spc)
Spec= ReadSpectra('sample_spectra/VIAVI/JDSU_Phar_Rotate_S06_1_20171009_1540.spc')