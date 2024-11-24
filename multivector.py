
DIMENSION = 3

class MultiVector:
    def __init__(self, alg, components):
        self.alg = alg
        self.components = components
        if len(components) != 2 ** alg.dim:
            raise ValueError("Incorrect number of coefficients for current spatial dimension.")
    
    def __repr__(self):
        return f"Multivector({self.components})"

    def __mul__(self, other):
        result_components = self.alg.gp(self.components, other.components)
        return MultiVector(self.alg, result_components)

    
