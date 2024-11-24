

class Algebra:
    def __init__(self, dim=3):
        self.dim = dim
        self.n_blades = 2 ** self.dim
        self.blades = list(range(self.n_blades))
        self.gtable = self.create_table(self.gp_basis_blade)
        self.otable = self.create_table(self.op_basis_blade)
        self.itable = self.create_table(self.ip_basis_blade)
    
    def create_table(self, func):
        table = {}
        for i in self.blades:
            for j in self.blades:
                bm_result, sign = func(i, j)
                table[(i, j)] = (bm_result, sign)
        return table

    def gp_basis_blade(self, a, b):
        bitmap = a ^ b
        sign = self.reordering_sign(a, b)
        return bitmap, sign

    def op_basis_blade(self, a, b):
        if (a & b):
            return 0, 0
            
        bitmap = a ^ b
        sign = self.reordering_sign(a, b)
        return bitmap, sign
    
    def ip_basis_blade(self, a, b):
        if not (a & b):
            return 0, 0
        
        bitmap = a & b
        sign = self.reordering_sign(a, b)
        return bitmap, sign

    def reordering_sign(self, a: int, b: int) -> int:
        a = a >> 1
        total = 0
        while a != 0:
            total += (a & b).bit_count()
            a = a >> 1
        return (1 if ((total & 1) == 0) else -1)

    def gp_op(self, a, b, outer):
        output_components = [0] * self.n_blades

        for a_idx, a_comp in enumerate(a):
            if a_comp == 0: continue
            for b_idx, b_comp in enumerate(b):
                if b_comp == 0: continue

                # Lookup multiplication result in table
                if outer:
                    blade, sign = self.otable[(a_idx, b_idx)]
                else:
                    blade, sign = self.gtable[(a_idx, b_idx)]

                # Add the contribution to that component
                output_components[blade] += a_comp * b_comp * sign
        return output_components