import multivector as mv
import algebra

alg = algebra.Algebra()

a = mv.MultiVector(alg, [0,0,0,0,0,0,0,1])
b = mv.MultiVector(alg, [0,0,0,0,0,0,0,1])

print(a*b)