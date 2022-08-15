
#Bessel's identity
#(10)

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

x=float(input("Enter the x: "))
n=int(input("Enter the n: "))
LHS= jn(n,x)
RHS= np.sqrt(2/((np.pi)*x))*(np.cos(x))
print("LHS: ",LHS)
print("RHS: ",RHS)
