import numpy as np

class MultiVector:
    def __init__(self, alg, components):
        self.alg = alg
        self.components = np.array(components, dtype=float)
        if len(components) != 2 ** alg.dim:
            raise ValueError("Incorrect number of coefficients for current spatial dimension.")
    
    def __repr__(self):
        return f"Multivector({self.components})"
    
    def __str__(self):
        terms = []
        for value, label in zip(self.components, self.alg.basis_labels):
            if value != 0:
                formatted_value = f"{abs(value):.3f}"
                rounded_value = round(value, 3)

                if label == "1": # Scalar component
                    terms.append(f"{value:.3f}")
                elif value == 1:
                    terms.append(f"+{label}" if terms else label)
                elif value == -1:
                    terms.append(f"-{label}")
                elif rounded_value == int(rounded_value):
                    terms.append(f"{'+' if value > 0 and terms else ''}{int(rounded_value)}{label}")
                else:
                    terms.append(f"{'+' if value > 0 and terms else ''}{value:.3f}{label}")
        return ''.join(terms)

    # Overload the various algebraic operations
    def __add__(self, other):
        if isinstance(other, MultiVector):
            return MultiVector(self.alg, self.components + other.components)
        elif isinstance(other, (int, float)):
            res_components = self.components.copy()
            res_components[0] += other
            return MultiVector(self.alg, res_components)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            res_components = self.components.copy()
            res_components[0] += other
            return MultiVector(self.alg, res_components)

    def __sub__(self, other):
        return MultiVector(self.alg, self.components - other.components)

    def __mul__(self, other):
        return MultiVector(self.alg, self.alg.product_from_table(self.components, other.components, product_type="g"))
    
    def __rmul__(self, const):
        return MultiVector(self.alg, const * self.components)

    def __xor__(self, other):
        return MultiVector(self.alg, self.alg.product_from_table(self.components, other.components, product_type="o"))
    
    def __or__(self, other):
        return MultiVector(self.alg, self.alg.product_from_table(self.components, other.components, product_type="i"))
