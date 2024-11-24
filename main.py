import multivector as mv
import algebra

alg = algebra.Algebra(dim=2)

a = mv.MultiVector(alg, [0,1,0,0])
b = mv.MultiVector(alg, [0,0,1,0])

print(a*b)
print(a^b)
print(a)