a = 10
b = 20
print(a + b) 

import pandas as pd  

# Creating a simple table (DataFrame)
data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})  
# Show the DataFrame
data  

# import matplotlib.pyplot as plt
import seaborn as sns
scores = [5,8,6,9,7,6,5,10,8,9,6,8,8,6,5,6]
sns.histplot(scores, kde = True)

# plt.show()