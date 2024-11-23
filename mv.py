DIMENSION = 3


class MultiVector:
    def __init__(self, components):
        self.components = components
        if len(components) != 2 ** DIMENSION:
            raise ValueError("Incorrect number of coefficients for current spatial dimension.")
    
    def __repr__(self):
        return f"Multivector({self.components})"

    def __mul__(self, other):
        return gp(self, other)


class BasisBlade:
    def __init__(self, bitmap: int, sign: int):
        self.bitmap = bitmap
        self.sign = sign


def gp(a: MultiVector, b: MultiVector):
    output_components = [0] * (2 ** DIMENSION)

    # Perform element-wise multiplication
    for a_idx, a_comp in enumerate(a.components):
        if a_comp == 0: continue
        for b_idx, b_comp in enumerate(b.components):
            if b_comp == 0: continue

            blade = gp_basis_blade(BasisBlade(a_idx, 1), BasisBlade(b_idx, 1))

            output_components[blade.bitmap] += a_comp * b_comp * blade.sign
    return MultiVector(output_components)

# Computes the sign after reordering the basis vectors into canonical order
def reordering_sign(a: int, b: int) -> int:
    a = a >> 1
    total = 0
    while a != 0:
        total += (a & b).bit_count()
        a = a >> 1
    return (1 if ((total & 1) == 0) else -1)

def gp_basis_blade(a: BasisBlade, b: BasisBlade):
    bxor = a.bitmap ^ b.bitmap
    sign = reordering_sign(a.bitmap, b.bitmap)
    return BasisBlade(bxor, sign)
