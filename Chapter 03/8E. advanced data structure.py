# OrderedDict -------------------------------------

from collections import OrderedDict

od = OrderedDict()
od["apple"] = 3
od["banana"] = 5
print(list(od.keys()))   # ['apple', 'banana']

# Example 2

workflow = OrderedDict()
workflow["load_data"] = "Step 1: Load CSV file"
workflow["clean_data"] = "Step 2: Remove nulls"
workflow["analyze"] = "Step 3: Run statistics"
workflow["report"] = "Step 4: Generate summary"

for step, desc in workflow.items():
    print(desc)


# You can explicitly move keys to the front or end, which is not possible with a plain dict.

workflow.move_to_end("clean_data", last=False)
print(list(workflow.keys()))

# frozenset -------------------------------------

fs = frozenset(["a", "b", "c"])
print("a" in fs)   # True
fs.add("d") # Error (immutable)

# namedtuple -------------------------------------

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)   # 10 20

# dataclass -------------------------------------
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    qty: int

item = Product("Book", 12.99, 5)
print(item.name, item.price)

# List of dictionaries -------------------------------------
products = [
    {"name": "Pen", "price": 1.5},
    {"name": "Notebook", "price": 3.0}
]
print(products[0]["name"])   # Pen

# Dictionary of lists -------------------------------------
grades = {
    "Alice": [85, 90, 92],
    "Bob": [78, 81, 85]
}
print(grades["Alice"])   # [85, 90, 92]