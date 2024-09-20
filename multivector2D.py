from dataclasses import dataclass
import math

@dataclass
class Multivector2D:
    scalar: float = 0.0
    e1: float = 0.0
    e2: float = 0.0
    e12: float = 0.0

    def __add__(self, other):
        return Multivector2D(
            self.scalar + other.scalar,
            self.e1 + other.e1,
            self.e2 + other.e2,
            self.e12 + other.e12
        )

    def __sub__(self, other):
        return Multivector2D(
            self.scalar - other.scalar,
            self.e1 - other.e1,
            self.e2 - other.e2,
            self.e12 - other.e12
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # Scalar multiplication
            return Multivector2D(
                self.scalar * other,
                self.e1 * other,
                self.e2 * other,
                self.e12 * other
            )
        elif isinstance(other, Multivector2D):
            # Geometric product
            return self.geometric_product(other)
        else:
            raise NotImplementedError(f"Multiplication with type {type(other)} not supported.")

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __neg__(self):
        return self * -1

    def geometric_product(self, other):
        # Unpack self components
        a, b, c, d = self.scalar, self.e1, self.e2, self.e12
        # Unpack other components
        a_p, b_p, c_p, d_p = other.scalar, other.e1, other.e2, other.e12

        # Compute the geometric product
        # Using GA multiplication rules:
        # e1*e1 = 1, e2*e2 = 1, e1*e2 = e12, e2*e1 = -e12, e12*e1 = e2, e12*e2 = -e1, e12*e12 = -1

        # Scalar part
        scalar = a * a_p + b * b_p + c * c_p - d * d_p

        # Vector part
        e1_component = a * b_p + b * a_p + c * d_p - d * c_p
        e2_component = a * c_p + c * a_p + d * b_p - b * d_p

        # Bivector part
        e12_component = a * d_p + d * a_p + b * c_p - c * b_p

        return Multivector2D(
            scalar=scalar,
            e1=e1_component,
            e2=e2_component,
            e12=e12_component
        )

    def reverse(self):
        """
        Reversion operation: reverses the order of basis vectors in each blade.
        In 2D:
            reverse(e12) = -e12
        """
        return Multivector2D(
            scalar=self.scalar,
            e1=self.e1,
            e2=self.e2,
            e12=-self.e12
        )

    def magnitude(self):
        """
        Compute the magnitude (norm) of the multivector.
        For vectors: sqrt(e1^2 + e2^2)
        Scalars and bivectors contribute differently.
        """
        return (self.scalar**2 + self.e1**2 + self.e2**2 - self.e12**2) ** 0.5

    def inverse(self):
        """
        Compute the inverse of the multivector.
        M^{-1} = reverse(M) / (M * reverse(M)).scalar
        """
        reversed_self = self.reverse()
        denominator = (self * reversed_self).scalar
        if denominator == 0:
            raise ZeroDivisionError("Cannot invert a multivector with zero magnitude.")
        return reversed_self * (1 / denominator)

    def __repr__(self):
        components = []
        if self.scalar:
            components.append(f"{self.scalar}")
        if self.e1:
            components.append(f"{self.e1}e1")
        if self.e2:
            components.append(f"{self.e2}e2")
        if self.e12:
            components.append(f"{self.e12}e12")
        return " + ".join(components) if components else "0"

    
def create_rotor2D(theta):
    """
    Create a rotor for rotating vectors in the e1-e2 plane by angle theta.
    """
    return Multivector2D(
        scalar=math.cos(theta / 2),
        e12=-math.sin(theta / 2)
    )

def create_rotorND(theta):
    """
    Create a rotor for rotating vectors in the e1-e2 plane by angle theta.
    """
    B = 
    return Multivector2D(
        scalar=math.cos(theta / 2),
        e12=-math.sin(theta / 2)
    )

def rotate_vector(vector, theta):
    """
    Rotate a vector by angle theta using a rotor.
    """
    rotor = create_rotor2D(theta)
    rotor_inv = rotor.inverse()
    return rotor * vector * rotor_inv

def reflect_vector(vector, normal):
    """
    Reflect a vector in the hyperplane perpendicular to the normal vector
    """
    return -normal * vector * normal

a = Multivector2D(e1=1)
b = Multivector2D(e1=1)

print("Vector a:", a)
print("Vector b:", b)

print(reflect_vector(a,b))
