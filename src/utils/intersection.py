from scipy.optimize import brentq
import numpy as np


def bezier_intersect(p1, hp1, hp2, p2, a, axis):
    """axis=0 for x=a, axis=1 for y=a. Returns list of (t, other_coord)."""
    i, j = axis, 1 - axis

    A = -p1[i] + 3 * hp1[i] - 3 * hp2[i] + p2[i]
    B = 3 * p1[i] - 6 * hp1[i] + 3 * hp2[i]
    C = -3 * p1[i] + 3 * hp1[i]
    D = p1[i] - a

    results = []
    for t in np.roots([A, B, C, D]):
        if abs(t.imag) < 1e-6 and 0 <= t.real <= 1:
            t = t.real
            mt = 1 - t
            other = (
                mt**3 * p1[j]
                + 3 * mt**2 * t * hp1[j]
                + 3 * mt * t**2 * hp2[j]
                + t**3 * p2[j]
            )
            results.append((t, other))
    return results
