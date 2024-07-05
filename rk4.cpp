#include <iostream>
#include <cmath>

using namespace std;

// Function to compute the derivative f(x) = sin(|x-1|)
double f(double x) {
  return sin(abs(x-1));
}

// RK4 function to solve the differential equation
void rk4(double x0, double y0, double h, int n, double* x, double* y) {
  double k1[2], k2[2], k3[2], k4[2];

  for (int i=0; i<n; i++) {
    k1[0] = f(x0);         // f(x0)
    k1[1] = y0;            // y0

    k2[0] = f(x0 + 0.5*h); // f(x0 + 0.5*h)
    k2[1] = y0 + 0.5*h*k1[0]; // y0 + 0.5*h*f(x0)

    k3[0] = f(x0 + 0.5*h); // f(x0 + 0.5*h)
    k3[1] = y0 + 0.5*h*k2[0]; // y0 + 0.5*h*f(x0 + 0.5*h)

    k4[0] = f(x0 + h);      // f(x0 + h)
    k4[1] = y0 + h*k3[0];   // y0 + h*f(x0 + 0.5*h)

    x[i+1] = x0 + h;        // x[i+1] = x0 + h
    y[i+1] = y0 + (h/6.0)*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1]); // y[i+1] = y0 + (h/6.0)*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
    x0 = x[i+1];            // x0 = x[i+1]
    y0 = y[i+1];            // y0 = y[i+1]
  }
}

int main() {
  double x0 = 0.0;         // initial x value
  double y0 = 1.0;         // initial y value
  double h = 0.01;         // step size
  int n = 1000;           // number of steps
  double* x = new double[n+1]; // array to store x values
  double* y = new double[n+1]; // array to store y values

  // Initialize x and y arrays
  x[0] = x0;
  y[0] = y0;

  // Solve the differential equation using RK4
  rk4(x0, y0, h, n, x, y);

  // Print the results
  for (int i=0; i<=n; i++) {
    cout << x[i] << " " << y[i] << endl;
  }

  delete[] x;
  delete[] y;

  return 0;
}
