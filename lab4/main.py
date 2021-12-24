import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def F(s, t):
    a = 7.23
    b = 4.9
    p0 = -a * s[0] + b * s[1]
    p1 = a * s[0] + 2 * b * s[2] - a * s[1] - b * s[1]
    p2 = a * s[1] + 3 * b * s[3] - 2 * b * s[2] - a * s[2]
    p3 = a * s[2] + 4 * b * s[4] - 3 * b * s[3] - a * s[3]
    p4 = a * s[3] + 4 * b * s[5] - 4 * b * s[4] - a * s[4]
    p5 = a * s[4] - 4 * b * s[5]

    # [dvdt, dudt]
    return [p0, p1, p2, p3, p4, p5]


def K(s):
    dx = (s[1] + 2 * s[2] + 3 * s[3] + 4 * (s[4] + s[5])) / 4
    dz = (s[3] + 2 * s[2] + 3 * s[1] + 4 * s[0]) / 4

    return dx, dz


def solve():
    t = np.linspace(0, 2)
    s0 = [1, 0, 0, 0, 0, 0]
    s = odeint(F, s0, t)
    graph_1(t, s)
    graph_2(t, s)


def graph_1(t, s):
    plt.plot(t, s[:, 0], color="#68EDD5",  linewidth=2.0, label="x(t)")
    plt.plot(t, s[:, 1], color="#ED7468",  linewidth=2.0, label="y(t)")
    plt.plot(t, s[:, 2], color="#EDC268",  linewidth=2.0, label="z(t)")
    plt.plot(t, s[:, 3], color="#D868ED",  linewidth=2.0, label="c(t)")
    plt.plot(t, s[:, 4], color="#6D9CF7",  linewidth=2.0, label="b(t)")
    plt.plot(t, s[:, 5], color="#F1F76D",  linewidth=2.0, label="n(t)")
    plt.show()


def graph_2(t, s):
    d = [K(x) for x in s]
    d = np.matrix(d)
    plt.plot(t, d[:, 0])
    plt.plot(t, d[:, 1])
    plt.show()


if __name__ == "__main__":
    solve()
