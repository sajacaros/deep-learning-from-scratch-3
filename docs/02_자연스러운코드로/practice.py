import sys

module_path = "../../"
sys.path.append(module_path)

import numpy as np
from dezero.main import Variable

x = Variable(np.array(1.0))
y = x + 3
print(x)
print(y)
