import algebra
import multivector as mv
import numpy as np

alg = algebra.Algebra(dim=3)
e1 = mv.MultiVector(alg, np.array([0,1,0,0,0,0,0,0]))
e2 = mv.MultiVector(alg, np.array([0,0,1,0,0,0,0,0]))
e12 = mv.MultiVector(alg, np.array([0,0,0,1,0,0,0,0]))
e3 = mv.MultiVector(alg, np.array([0,0,0,0,1,0,0,0]))
e13 = mv.MultiVector(alg, np.array([0,0,0,0,0,1,0,0]))
e23 = mv.MultiVector(alg, np.array([0,0,0,0,0,0,1,0]))
e123 = mv.MultiVector(alg, np.array([0,0,0,0,0,0,0,1]))