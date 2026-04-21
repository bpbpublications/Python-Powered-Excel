# You can create a set by using curly braces {} or set() function.

numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3}

product_id = {'g1001', 'g1002', 'g1002'}
print(product_id) # {'g1001', 'g1002'} # Keeps unique element only

# elements are unordered
s1 = {23, 15, 37, 86, 45, 24, 83, 41}; s1    

# Adding element(s) to set using add() or update() method -------------

product_id.add('g1003') 
print(product_id) 

product_id.update(['g1004']) # less efficient for single item
print(product_id) 

product_id.update(['g1005', 'g1006'])
print(product_id) 


# use add() method to add single value to a set.
# use update() method to add sequence values to a set.

# Set specific methods --------------------

customer_id_jan = {'101', '102', '103', '104'}
customer_id_feb = {'102', '104', '105', '106'}

# Union

all_customers = customer_id_jan.union(customer_id_feb)
# or
all_customers = customer_id_jan | customer_id_feb
print(f'Customers who bought our product in Jan & Feb:\n\n{all_customers}')

common_customers = customer_id_jan.intersection(customer_id_feb)
# or
common_customers = customer_id_jan & customer_id_feb
print(f'Repeat Customers_Jan & Feb:\n\n{common_customers}')

lost_customers = customer_id_jan.difference(customer_id_feb)
# or
lost_customers = customer_id_jan - customer_id_feb
print(f'Churned Jan Customers:\n\n{lost_customers}')

sym_diff = customer_id_jan.symmetric_difference(customer_id_feb)
# or
sym_diff = customer_id_jan ^ customer_id_feb
print(f'Customers who bought in Jan or Feb, but not both: \n\n{sym_diff}')