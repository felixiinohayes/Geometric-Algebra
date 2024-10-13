#include <iostream>
#include <vector>
#include <bitset>

class MultiVector {
public:
    std::array<int, 8> components;
    std::bitset<3> blade;

    MultiVector(std::array<int, 8> values) : components(values) {
        if (values.size() != 8) {
            throw std::invalid_argument("Multivector must have 8 coefficients in 3D.");
        }
    }
};

struct BasisBlade
{
    std::bitset<3> bitmap;
    double sign;

    BasisBlade(std::bitset<3> bitmap, double sign) : bitmap(bitmap), sign(sign) {}
};

double reordering_sign(std::bitset<3>& a, std::bitset<3>& b) {
    a = a >> 1;
    int sum = 0;
    while (a != 0) {
        sum = sum + (a & b).count();
        a = a >> 1;
    }
    return ((sum & 1) == 0) ? 1.0 : -1.0;
}

BasisBlade outer_product(std::bitset<3>& a, std::bitset<3>& b) {
    if ((a & b).any()) return BasisBlade(std::bitset<3>(0), 0.0);

    std::bitset<3> bxor = a ^ b;
    double sign = reordering_sign(a, b);
    return BasisBlade(bxor, sign);
}

int main() {

    return 0;
}