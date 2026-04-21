# Basic import ________________________________________________

import math

# Calling different methods from 'math' module
math.sqrt(16) # 4.0
math.log(10) # 2.302585092994046
math.sin(2)# 0.9092974268256817

sqrt(16) # NameError: name 'sqrt' is not defined

# Import specific parts ________________________________________

from math import sqrt, log

# Calling method names directly

sqrt(16) # 4.0
log(10)# 2.302585092994046

# This method is the standard and accepted practice 
# for large libraries which has many submodules
# For example

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Wildcard import (Not recommended) ___________________________

from math import *

sqrt(16) # 4.0
log(10)# 2.302585092994046

# Importing a module with an alias _____________________________


import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)	 # 1D Array: [1 2 3 4 5]


import pandas as pd  

data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}) 
data
