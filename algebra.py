

class Algebra:
    def __init__(self, dim=3):
        self.dim = dim
        self.n_blades = 2 ** self.dim
        self.blades = list(range(self.n_blades))
        self.gtable = self.create_gtable()
    
    def create_gtable(self):
        table = {}
        for i in self.blades:
            for j in self.blades:
                bm_result, sign = self.gp_basis_blade(i, j)
                table[(i, j)] = (bm_result, sign)
        return table
    
    def gp_basis_blade(self, a, b):
        bitmap = a ^ b
        sign = self.reordering_sign(a, b)
        return bitmap, sign

    def reordering_sign(self, a: int, b: int) -> int:
        a = a >> 1
        total = 0
        while a != 0:
            total += (a & b).bit_count()
            a = a >> 1
        return (1 if ((total & 1) == 0) else -1)

    def gp(self, a, b):
        output_components = [0] * (2 ** self.dim)

        # Perform element-wise multiplication
        for a_idx, a_comp in enumerate(a):
            if a_comp == 0: continue
            for b_idx, b_comp in enumerate(b):
                if b_comp == 0: continue

                blade, sign = self.gp_basis_blade(a_idx, b_idx)

                output_components[blade] += a_comp * b_comp * sign
        return output_components
