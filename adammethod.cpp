#include <iostream>
#include <cmath>

using namespace std;

double derivative(double x, double y) {
    return x + y/x - y;
}

void adam_bashforth(double& x, double& y, double h, int n) {
    double y_pred, y_corr;

    y_pred = y + h / 24 * (9 * derivative(x, y) + 19 * derivative(x + h, y) - 5 * derivative(x + h, y_pred) + derivative(x + 2 * h, y_pred));

    y_corr = y + h / 24 * (9 * derivative(x + h, y_corr) + 19 * derivative(x + h, y_pred) - 5 * derivative(x + h, y) + derivative(x + 2 * h, y_pred));

    x += h;
    y = y_corr;
}

int main() {
    double x = 1.0, y = 1.0;
    double h = 0.1;
    int n = 10;

    for (int i = 0; i < n; i++) {
        adam_bashforth(x, y, h, n);
        cout << "x = " << x << ", y = " << y << endl;
    }

    return 0;
}
