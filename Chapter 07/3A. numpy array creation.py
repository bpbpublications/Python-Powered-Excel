# see if more examples are there in numpy.py
import numpy as np

# 1-D array
sales = np.array([1500, 2200, 1850, 2400.])

type(sales)
print(sales)
len(sales)      # 4
sales.ndim      # 1
sales.dtype     # dtype('float64')


# 2-D array
sales_qtr = np.array([[1500, 1700, 1600], 
                      [2200, 2100, 2300]])

type(sales_qtr)
print(sales_qtr)
len(sales_qtr)      # 2
sales_qtr.ndim      # 2
sales_qtr.dtype # dtype('int32')


# Create an array of 5 zeros 
np.zeros(5)

# Create an array of 3 ones
np.ones(3)

# Create a 5X5 identity matrix (1s on the main diagonal))
np.eye(5)

# Create a 5×5 matrix with 1s on the diagonal just above the main diagonal
np.eye(5, k=1)

# Create a 2X3 matrix with 1 at principle diagnoal n 0 elsewhere
np.eye(2,3)

# Create an array with values from 0 to 4
np.arange(5)

# Create an array with values from 1 to 5 (inclusive range like Excel ROW/SEQUENCE)
np.arange(1, 6)

# Evenly spaced numbers between 0 and 1 (inclusive), like Excel's SEQUENCE with steps
np.linspace(0, 1, 5)

# Generate 100 values from a standard normal distribution (mean=0, std=1)
np.random.randn(100)

# Get the mean of normally distributed values
np.random.randn(100).mean()

# Get the standard deviation of normally distributed values
np.random.randn(100).std()

# Generate 5000 values from a normal distribution with mean=70 and std=10
np.random.normal(loc=70, scale=10, size=5000)

# Simulate values with mean=70, std=10 using standard normal and scaling
(np.random.randn(1000) * 10) + 70

# Generate 5 random floats between 0 and 1 (uniform distribution)
np.random.rand(5)

# Random integer between 0 and 4 (upper limit excluded)
np.random.randint(5)

# Random integer between 5 and 11 (upper limit excluded)
np.random.randint(5, 12)

# 20 Random integers between 5 and 11 (upper limit excluded)
np.random.randint(5, 12, 20)

# Randomly choose 3 items from the list
np.random.choice([10, 20, 30, 40], size=3)

# Fix the random seed to get reproducible results
np.random.seed(42)
np.random.randint(1, 100, 3)

ids = ['a01', 'a02', 'a03', 'a04', 'a05'] # a list
np.random.choice(ids, size=3) # Randomly select 3 values from the list