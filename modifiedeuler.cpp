#include <iostream>
#include <cmath>
#include <functional>

void modifiedEuler(double y0, double x0, double xEnd, double h, std::function<double(double, double)> f) {
    double y = y0;
    double x = x0;

    while (x < xEnd) {
        double k1 = f(x, y);
        double k2 = f(x + h, y + h * k1);
        
        y = y + (h / 2) * (k1 + k2);
        x = x + h;

        std::cout << "x: " << x << ", y: " << y << std::endl;
    }
}

int main() {
    auto f = [](double x, double y) { return std::sin(2 * x); };
    
    double y0 = 0.0;
    double x0 = 0.0;
    double xEnd = 1.0;
    double h = 0.1;
    
    modifiedEuler(y0, x0, xEnd, h, f);
    
    return 0;
}
