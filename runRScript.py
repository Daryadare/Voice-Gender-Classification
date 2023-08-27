import os
os.environ["R_HOME"] = r"C:\Program Files\R\R-4.3.1"
os.environ["PATH"] = r"C:\Program Files\R\R-4.3.1\bin\x64" + ";" + os.environ["PATH"]
import rpy2
import rpy2.robjects.packages as rpackages
from rpy2.robjects import StrVector


print(rpy2.__version__)

base = rpackages.importr('base')
utils = rpackages.importr("utils")
# select a mirror for R packages
utils.chooseCRANmirror(ind=1)

# R package names
packnames = ('seewave')

    # ('tuneR', 'seewave', 'fftw', 'caTools', 'warbleR',
    #          'mice', 'e1071', 'rpart', 'rpart-plot', 'e1071')

# Selectively install what needs to be installed.
names_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
if len(names_to_install) > 0:
    utils.install_packages(StrVector(names_to_install))

res = rpackages.r.source("C:/Users/User/Desktop/ml/audio/sound.R", encoding="utf-8")
print(res)

import numpy as np
decode = np.fromfile("data.bin",  dtype=np.int8)
print(len(decode), decode[:10])
