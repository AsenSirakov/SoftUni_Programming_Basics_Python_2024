import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iterations):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iterations:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iterations):
    mandel = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            real = xmin + x * (xmax - xmin) / (width - 1)
            imag = ymin + y * (ymax - ymin) / (height - 1)
            c = complex(real, imag)
            mandel[x, y] = mandelbrot(c, max_iterations)
    return mandel

def plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iterations):
    mandel = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iterations)
    plt.imshow(mandel.T, extent=(xmin, xmax, ymin, ymax), cmap='hot', origin='lower')
    plt.colorbar(label='Iterations')
    plt.title('Mandelbrot Set')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()

if __name__ == "__main__":
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5
    width, height = 1000, 1000
    max_iterations = 1000

    plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iterations)
