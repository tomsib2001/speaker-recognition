# -*- coding: utf-8 -*-
from __future__ import division #division en flottants par défaut
import numpy as np
import matplotlib.pyplot as plt

def plot(x, y, w, b):
    x1max = np.max(x[:, 0]) + 2
    x2max = np.max(x[:, 1]) + 2
    x1min = np.min(x[:, 0]) - 2
    x2min = np.min(x[:, 1]) - 2

    s1 = [x[i] for i in xrange(len(x)) if y[i] == 1]
    s2 = [x[i] for i in xrange(len(x)) if y[i] == -1]
    s11 = [s1[i][0] for i in xrange(len(s1))]
    s12 = [s1[i][1] for i in xrange(len(s1))]
    s21 = [s2[i][0] for i in xrange(len(s2))]
    s22 = [s2[i][1] for i in xrange(len(s2))]

    if (w[1] <> 0):
        l1 = [x1min, x1max]
        l2 = [-(b + w[0]*x1min)/w[1], -(b + w[0]*x1max)/w[1]]
    else:
        l1 = [-b/w[0], -b/w[0]]
        l2 = [x2min, x2max]

    plt.plot(s11, s12, 'ro', s21, s22, 'bx', l1, l2, 'g-')
    
    plt.axis([x1min, x1max, x2min, x2max])
    plt.show()
