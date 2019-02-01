import numpy as np
import matplotlib.pyplot as plt

PI = np.pi
S = "If Comrade Napoleon says it, it must be right."
A = [100, 200, 300]


def plot_sine(n=2):
    x = np.linspace(0, 2 * PI)
    y = np.sin(n * x / 2)

    fig, ax = plt.subplots(1, figsize=(6, 4))
    ax.plot(x, y)

    return fig, ax


def foo(arg):
    print(f'arg = {arg}')


class Foo:
    pass


if __name__ == '__main__':
    fig, ax = plot_sine()
    ax.set_title('Command Line Test')
    fig.savefig('test.png', dpi=400, bbox_inches='tight')
    fig.show()