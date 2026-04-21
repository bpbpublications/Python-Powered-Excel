# This section/script offers a brief preview of what pandas can do;
# each topic is explained in detail in the following sections/code files.

import pandas as pd
# pd.__version__ 

import os
os.getcwd() # Excel_Python folder created for the book

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
data = pd.read_excel(os.path.join(data_path, 'employees.xlsx'))
print(data)

data.head()
data.tail(2)

data.shape
data.columns

data.info()

data.describe()
data.describe(include='all')



data['dept']
# or
data.dept

data['dept'].nunique() 
data['dept'].unique() 

data['dept'].value_counts()
data['dept'].value_counts(normalize = True)

data['left'].value_counts()

# In upcoming sections, you will learn in details about
# more analytics such as:

# See how many have left in each department
pd.crosstab(data["dept"], data["left"])
pd.crosstab(data["dept"], data["left"], margins=True)

pd.crosstab(data["dept"], data["left"], 
            margins=True, normalize=True)  # % by overall total

pd.crosstab(data["dept"], data["left"], 
            normalize='columns').round(2)  # % w.r.t. left variable

pd.crosstab(data["dept"], data["left"], 
            normalize='index').multiply(100).round(2) # # % w.r.t. dept variable


data.describe() # summary stats (count, mean, std, min, max)

# Do not worry, if you don't understand the code, for now just observe what pandas has to offer
    
# summary stats per department
data.groupby('dept').describe()            

# mean salary per dept, cast to integer
data.groupby('dept')['sal'].mean().astype(int)  

# mean salary per dept, rounded to nearest whole number
data.groupby('dept')['sal'].mean().round(0)     

# compute mean, min, and max salary per dept
data.groupby('dept')['sal'].aggregate(['mean', 'min', 'max'])  


# Observe name column
data["name"].head(3) # Looks clean but might have white space
data["name"].head(3).str.len()

# Make all employee names clean
data["name"].str.lower().str.strip().head(3).str.len() #white space removed

data["name"] = data["name"].str.lower().str.strip()

 # You can also plot with pandas (More on this in chapter 7)
 
# plot all numeric columns
data.plot()

# plot salary distribution (single column)
data['sal'].plot()

# bar chart of counts for 'left' categories
data['left'].value_counts().plot(kind='bar')

# bar chart: average salary per department
data.groupby("dept")["sal"].mean().plot(kind="bar")

# bar chart with title and y‑label: average salary per department
data.groupby("dept")["sal"].mean().plot(kind="bar", title="Avg Salary by Department", ylabel="Salary ($)")

# grouped bar chart: department vs left (counts)
pd.crosstab(data['dept'], data['left']).plot(kind='bar')

# stacked bar chart: department vs left (counts)
pd.crosstab(data['dept'], data['left']).plot(kind='bar', stacked=True)

# boxplot of salary by department (shows distribution and outliers)
data.boxplot(column='sal', by='dept')

# line plot of mean salary by department
data.groupby('dept')['sal'].mean().plot() 