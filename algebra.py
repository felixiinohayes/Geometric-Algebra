import multivector as mv

class Algebra:
    def __init__(self, signature):
        self.signature = signature
        self.dim = len(signature)
        self.n_blades = 2 ** self.dim
        self.blades = list(range(self.n_blades))

        self.gtable = self.create_table(self.gp_basis_blade)
        self.otable = self.create_table(self.op_basis_blade)
        self.itable = self.create_table(self.ip_basis_blade)
        self.basis_labels = self.create_basis_labels()
    
    def create_table(self, func):
        table = {}
        for i in self.blades:
            for j in self.blades:
                bm_result, sign = func(i, j)
                table[(i, j)] = (bm_result, sign)
        return table
    
    def create_basis_labels(self):
        labels = []
        for i in range(1, self.n_blades):
            label = ["e"]
            for bit in range(self.dim):
                if i & (1 << bit):
                    label.append(str(bit))
            labels.append(''.join(label))
        return labels

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

    def product_from_table(self, a, b, product_type):
        output_components = [0] * self.n_blades

        for a_idx, a_comp in enumerate(a):
            if a_comp == 0: continue
            for b_idx, b_comp in enumerate(b):
                if b_comp == 0: continue

                # Lookup multiplication result in table
                if product_type == "o":
                    blade, sign = self.otable[(a_idx, b_idx)]
                elif product_type == "g":
                    blade, sign = self.gtable[(a_idx, b_idx)]
                elif product_type == "i":
                    blade, sign = self.itable[(a_idx, b_idx)]

                # Add the contribution to that component
                output_components[blade] += a_comp * b_comp * sign
        return output_components