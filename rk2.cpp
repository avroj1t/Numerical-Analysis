#include <iostream>
#include <cmath>
#include <limits>

double dydx(double x, double y) {
    return std::log(x * y);
}

void rungeKutta2(double x0, double y0, double x, double h) {
    double k1, k2;
    double y = y0;
    double x_curr = x0;

    while (x_curr < x) {
        if (x_curr + h > x) {
            h = x - x_curr;
        }

        k1 = h * dydx(x_curr, y);
        k2 = h * dydx(x_curr + h / 2, y + k1 / 2);

        y = y + k2;
        x_curr = x_curr + h;

        if (std::isinf(y) || std::isnan(y)) {
            std::cout << "Numerical instability detected at x = " << x_curr << std::endl;
            break;
        }

        std::cout << "x = " << x_curr << ", y = " << y << std::endl;
    }
}

int main() {
    double x0 = 1.0;
    double y0 = 1.0;
    double x = 2.0;
    double h = 0.01;

    rungeKutta2(x0, y0, x, h);

    return 0;
}
