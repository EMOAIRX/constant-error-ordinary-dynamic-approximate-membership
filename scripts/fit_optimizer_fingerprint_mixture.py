#!/usr/bin/env python3
"""Fit an all-pivot optimizer profile by a nonnegative fingerprint mixture."""

from __future__ import annotations

import math
import os
import sys

import numpy as np

EXTRA = "/private/tmp/dynamic-amq-scipy"
if os.path.isdir(EXTRA):
    sys.path.insert(0, EXTRA)
from scipy.optimize import lsq_linear
from scipy.stats import poisson


P64 = np.asarray(
    [
        0.052124735934, 0.100324775846, 0.145048440294, 0.186676628459,
        0.225535189849, 0.261904647661, 0.296027915681, 0.328116478130,
        0.358355379992, 0.386907288036, 0.413915819425, 0.439508288358,
        0.463797986743, 0.486886089093, 0.508863252372, 0.529810966606,
        0.549802700681, 0.568904878883, 0.587177716805, 0.604675939838,
        0.621449403167, 0.637543628750, 0.653000272049, 0.667857529060,
        0.682150492424, 0.695911463925, 0.709170229526, 0.721954302093,
        0.734289136183, 0.746198318577, 0.757703737716, 0.768825734710,
        0.779583238228, 0.789993885231, 0.800074129254, 0.809839337690,
        0.819303879353, 0.828481203413, 0.837383910663, 0.846023817931,
        0.854412016384, 0.862558924330, 0.870474335072, 0.878167460298,
        0.885646969404, 0.892921025098, 0.899997315603, 0.906883083670,
        0.913585152627, 0.920109949567, 0.926463525774, 0.932651574376,
        0.938679445139, 0.944552156180, 0.950274402212, 0.955850558648,
        0.961284680490, 0.966580494170, 0.971741379310, 0.976770334929,
        0.981669919774, 0.986442145375, 0.991088271377, 0.995608358986,
    ]
)


def main() -> None:
    q = len(P64)
    # Treat block averages as midpoint samples; this is only a shape test.
    t = (np.arange(q) + 0.5) / q
    lambdas = np.geomspace(1e-3, 1e3, 800)
    basis = 2.0 * (1.0 - np.exp(-np.outer(t, lambdas)))
    endpoint = 2.0 * (1.0 - np.exp(-lambdas))

    # Enforce the half-error endpoint and unit size-biased mass by large
    # least-squares penalties.  A mass at lambda=infinity is also included.
    basis = np.c_[basis, 2.0 * np.ones(q)]
    endpoint = np.r_[endpoint, 2.0]
    augmented = np.r_[
        basis,
        1e4 * endpoint[None, :],
        1e4 * np.ones((1, len(endpoint))),
    ]
    target = np.r_[P64, 1e4, 1e4]
    result = lsq_linear(augmented, target, bounds=(0.0, np.inf), tol=1e-14)
    weights = result.x
    fitted = basis @ weights

    print(f"max_abs_error={np.max(np.abs(fitted - P64)):.12g}")
    print(f"endpoint={endpoint @ weights:.12f}")
    print(f"mass={weights.sum():.12f}")
    finite = weights[:-1]
    entropy_rate = float(np.sum(finite * poisson.entropy(lambdas) / lambdas / math.log(2.0)))
    print(f"poisson_shannon_rate={entropy_rate:.12f}")
    print(f"mass_lambda_below_0.1={finite[lambdas < 0.1].sum():.12f}")
    print(f"mass_lambda_above_10={finite[lambdas > 10].sum() + weights[-1]:.12f}")
    keep = np.flatnonzero(weights > 1e-5)
    top = keep[np.argsort(weights[keep])[-20:]]
    for index in top[np.argsort(weights[top])[::-1]]:
        label = "infinity" if index == len(lambdas) else f"{lambdas[index]:.9g}"
        print(f"lambda={label} weight={weights[index]:.12g}")


if __name__ == "__main__":
    main()
