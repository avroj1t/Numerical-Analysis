import math
import matplotlib.pyplot as plt

def derivative(x, y):
    return x + y / x - y

def adam_bashforth(x, y, h, n):
    y_pred = y + h / 24 * (9 * derivative(x, y) + 19 * derivative(x + h, y) - 5 * derivative(x + h, y) + derivative(x + 2 * h, y))
    y_corr = y + h / 24 * (9 * derivative(x + h, y_pred) + 19 * derivative(x + h, y_pred) - 5 * derivative(x + h, y) + derivative(x + 2 * h, y_pred))
    
    x += h
    y = y_corr
    
    return x, y

def main():
    x = 1.0
    y = 1.0
    h = 0.1
    n = 10

    x_values = [x]
    y_values = [y]

    for i in range(n):
        x, y = adam_bashforth(x, y, h, n)
        x_values.append(x)
        y_values.append(y)
        print(f"x = {x}, y = {y}")

    # Plotting the graph
    plt.plot(x_values, y_values, marker='o')
    plt.title("Adam-Bashforth Method")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
