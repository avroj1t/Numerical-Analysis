#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double f(double x, double y) {
    return x * x * sin(y);
}

double rk4(double x0, double y0, double h, double x_target) {
    double x = x0;
    double y = y0;
    
    cout << "x\t\t\t y" << endl;
    cout << fixed << setprecision(5);
    
    while (x <= x_target) {
        cout << x << "\t\t\t " << y << endl;
        
        double k1 = h * f(x, y);
        double k2 = h * f(x + h/2, y + k1/2);
        double k3 = h * f(x + h/2, y + k2/2);
        double k4 = h * f(x + h, y + k3);
        
        y = y + (k1 + 2*k2 + 2*k3 + k4)/6;
        x = x + h;
    }
    
    return y;
}

int main() {
    double x0 = 0.0;
    double y0 = 1.0;
    double h =0.001;
    double x_target = 1.0;
    
    double y_final = rk4(x0, y0, h, x_target);
    
    cout << "Final value of y at x = " << x_target << " is " << y_final << endl;
    
    return 0;
}
