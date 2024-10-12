#ifndef multivector.h
#define multivector.h

#include<iostream>
#include<cmath>

class MultiVector
{
public:
    double scalar;
    double e1;
    double e2;
    double e3;
    double e12;
    double e13;
    double e23;

    // Constructors
    MultiVector() : scalar(0.0), e1(0.0), e2(0.0), e12(0.0) {};
    MultiVector(double scalar, double e1, double e2, double e12) : scalar(scalar), e1(e1), e2(e2), e12(e12) {};
    MultiVector(const MultiVector& x) : scalar(x.scalar), e1(x.e1), e2(x.e2), e12(x.e12) {};

    MultiVector operator+(const MultiVector& other);
    MultiVector operator-(const MultiVector& other);
    MultiVector operator*(const MultiVector& other);
    MultiVector operator*(const double& other_scalar);

    MultiVector inverse();
    MultiVector rotate(const double& theta);
    void display();

};

#endif