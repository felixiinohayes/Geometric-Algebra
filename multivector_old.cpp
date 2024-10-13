class Vector
{
public:
    double e1,e2,e3;

    Vector(double e1=0.0, double e2=0.0, double e3=0.0) : e1(e1), e2(e2), e3(e3) {}

    Vector operator+(const Vector& v) const {
        return Vector(e1 + v.e1, e2 + v.e2, e3 + v.e3);
    }
    Vector operator-(const Vector& v) const {
        return Vector(e1 - v.e1, e2 - v.e2, e3 - v.e3);
    }
    double dot(const Vector& v) const {
        return (e1*v.e1 + e2*v.e2 + e3*v.e3);
    }
    Vector dot(const Bivector& b) const {
        return (b.e23*e1 - b.e13*e2, b.e13*e3 - b.e12*e1, b.e12*e2 - b.e23*e3);
    }
    Bivector wedge(const Vector& v) const {
        return Bivector(e1*v.e2-e2*v.e1, e1*v.e3-e3*v.e1, e2*v.e3-e3*v.e2);
    }
    Trivector wedge(const Bivector& b) const {
        return Trivector(e1*b.e23 + e2*b.e13 + e3*b.e12);
    }
};

class Bivector
{
public:
    double e12,e13,e23;

    Bivector(double e12=0.0, double e23=0.0, double e31=0.0) : e12(e12), e13(e13), e23(e23) {}

    Bivector operator+(const Bivector& b) const {
        return Bivector(e12 + b.e12, e13 + b.e13, e23 + b.e23);
    }
    Bivector operator-(const Bivector& b) const {
        return Bivector(e12 - b.e12, e13 - b.e13, e23 - b.e23);
    }
    double dot(const Bivector& b) const {
        return e12 * b.e12 + e13 * b.e13 + e23 * b.e23;
    }
    Vector dot(const Vector& v) const {
        return (e23*v.e1 - e13*v.e2, e13*v.e3 - e12*v.e1, e12*v.e2 - e23*v.e3);
    }
    Trivector wedge(const Bivector& b) const {
        return Trivector((e12 * b.e23 - e23 * b.e12) + (e13 * b.e12 - e12 * b.e13) + (e23 * b.e13 - e13 * b.e23));
    }
    Trivector wedge(const Vector& b) const {
        return Trivector(e23*b.e1 + e13*b.e2 + e12*b.e3);
    }

};

class Trivector
{
public:
    double e123;

    Trivector(double e123=0.0) : e123(e123) {}

    Trivector operator+(const Trivector& t) const {
        return Trivector(e123 + t.e123);
    }
    Trivector operator-(const Trivector& t) const {
        return Trivector(e123 - t.e123);
    }
    Bivector dot(const Vector& v) const {
        return Bivector(e123 * v.e1, e123 * v.e2, e123 * v.e3);
    }
    Vector dot(const Bivector& b) const {
        return Vector(e123 * b.e23, e123 * b.e13, e123 * b.e12);
    }
    Trivector wedge(const Vector& v) const {
        return Trivector(0.0); // Wedge of trivector and vector results in zero in 3D
    }
    Trivector wedge(const Bivector& b) const {
        return Trivector(0.0); // Wedge of trivector and bivector results in zero in 3D
    }
};

class Multivector
{
private:
    double scalar;
    Vector vector;
    Bivector bivector;
    Trivector trivector;
public:
    Multivector(double scalar, Vector vector, Bivector bivector, Trivector trivector) {

    }
};