from utils_extra.utils import sayHello
import math
import json

a = json.dumps({"name": "Arif", "age": 32, "city": "Hyderabad"})
print(a)
print(type(a))

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")

b = json.loads(a)
print(b)
print(type(b))

import math

a = math.sqrt(16)
print(f"The squareroot of 16 is {a}")
print(type(a))

#module import
from utils_extra.utils import *

printlog()

sayHello("arif")