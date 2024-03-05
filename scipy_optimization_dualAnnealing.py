# Can only return one minima. If a function has multiple minima with same obj function value,
# It randomly returns the optimized values of inputs
import numpy as np
from scipy.optimize import dual_annealing
import math

def objFunc(x):
    return x[0]**4 + x[2]*math.sin(x[1])

#func = lambda x: np.sum(x*x - 10*np.cos(2*np.pi*x)) + 10*np.size(x)



lBound = [-5.12, -15.12, 1.999]
uBound = [5.12,  15.12, 2.001]

optProblem = dual_annealing(objFunc, bounds=list(zip(lBound, uBound)))

print('Optimized solution : ',optProblem.x)
print('Objective function value : ',optProblem.fun)
print('Termination message : ',optProblem.message)