#ifndef MULTIVECTOR
#define MULTIVECTOR

#include<iostream>
#include<cmath>

class Multivector
{
public:
    double scalar;
    double e1;
    double e2;
    double e12;

    // Constructors
    Multivector() : scalar(0.0), e1(0.0), e2(0.0), e12(0.0) {};
    Multivector(double scalar, double e1, double e2, double e12) : scalar(scalar), e1(e1), e2(e2), e12(e12) {};

    Multivector operator+(const Multivector& other);
    Multivector operator-(const Multivector& other);
    Multivector operator*(const Multivector& other);
    Multivector operator*(double scalar);

    void display();

};

#endif