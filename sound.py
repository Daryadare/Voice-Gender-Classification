import os
import pandas as pd
from specan3 import funcR
os.environ["R_HOME"] = r"C:\Program Files\R\R-4.3.1"
os.environ["PATH"] = r"C:\Program Files\R\R-4.3.1\bin\x64" + ";" + os.environ["PATH"]

from rpy2.robjects.packages import STAP
from rpy2.robjects import pandas2ri

# Automatic conversion to pandas DataFrame
pandas2ri.activate()

audiocsv = pd.read_csv('./AudioDataR2.csv')
# print(audiocsv)
audiorpy2 = pandas2ri.py2rpy(audiocsv)
# print(audiorpy2)

specan3 = STAP(funcR, "specan3")
# print(specan3)

res = specan3.specan3(audiorpy2)
print(res)
