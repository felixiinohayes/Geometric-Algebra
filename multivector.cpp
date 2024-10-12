#include"multivector.h"

MultiVector MultiVector::operator+(const MultiVector& other) {
    return MultiVector(scalar + other.scalar, e1 + other.e1, e2 + other.e2, e12 + other.e12);
}
MultiVector MultiVector::operator-(const MultiVector& other) {
    return MultiVector(scalar - other.scalar, e1 - other.e1, e2 - other.e2, e12 - other.e12);
}
MultiVector MultiVector::operator*(const MultiVector& other) {
    MultiVector output;
    output.scalar = scalar * other.scalar + e1 * other.e1 + e2 * other.e2 - e12 * other.e12;
    output.e1 = scalar * other.e1 + e1 * other.scalar + e2 * other.e12 - e12 * other.e2;
    output.e2 = scalar * other.e2 + e2 * other.scalar + e12 * other.e1 - e1 * other.e12;
    output.e12 = scalar * other.e12 + e12 * other.scalar + e1 * other.e2 - e2 * other.e1;
    return output;
}

MultiVector MultiVector::operator*(const double& other_scalar) {
    return MultiVector(scalar * other_scalar, e1 * other_scalar, e2 * other_scalar, e12 * other_scalar);
}

MultiVector MultiVector::inverse() {
    MultiVector reversed_self(*this);
    double denominator =  (*this * reversed_self).scalar;
    if (denominator==0) throw std::runtime_error("Cannot invert a MultiVector with zero magnitude");
    return reversed_self * (1 / denominator);
}

MultiVector MultiVector::rotate(const double& theta) {
    MultiVector rotor;
    rotor.scalar = std::cos(theta/2);
    rotor.e12 = std::sin(theta/2);
    MultiVector rotated_vector = rotor * (*this) * rotor.inverse(); 
    return rotated_vector;
} 

void MultiVector::display() {
    bool first = true;
    if (scalar != 0.0) {
        std::cout << scalar;
        first = false;
    }
    if (e1 != 0.0) {
        if (!first) std::cout << " + ";
        std::cout << e1 << "e1";
        first = false;
    }
    if (e2 != 0.0) {
        if (!first) std::cout << " + ";
        std::cout << e2 << "e2";
        first = false;
    }
    if (e12 != 0.0) {
        if (!first) std::cout << " + ";
        std::cout << e12 << "e12";
        first = false;
    }
    std::cout << std::endl;
}

int main()
{
    MultiVector a;
    a.e1 = 1.0;
    MultiVector c = a.rotate(2);
    c.display();

}