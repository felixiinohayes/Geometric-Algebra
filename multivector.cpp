#include"multivector.h"

Multivector Multivector::operator+(const Multivector& other) {
    return Multivector(scalar + other.scalar, e1 + other.e1, e2 + other.e2, e12 + other.e12);
}
Multivector Multivector::operator-(const Multivector& other) {
    return Multivector(scalar - other.scalar, e1 - other.e1, e2 - other.e2, e12 - other.e12);
}
Multivector Multivector::operator*(const Multivector& other) {
    Multivector output;
    output.scalar = scalar * other.scalar + e1 * other.e1 + e2 * other.e2 - e12 * other.e12;
    output.e1 = scalar * other.e1 + e1 * other.scalar + e2 * other.e12 - e12 * other.e2;
    output.e2 = scalar * other.e2 + e2 * other.scalar + e12 * other.e1 - e1 * other.e12;
    output.e12 = scalar * other.e12 + e12 * other.scalar + e1 * other.e2 - e2 * other.e1;
    return output;
}

void Multivector::display() {
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
    Multivector a;
    Multivector b;
    a.e1 = 1.0;
    b.e2 = 1.0;
    Multivector c = a * b;

    c.display();

}