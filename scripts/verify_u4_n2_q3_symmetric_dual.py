"""Verify the five-orbit U=4,n=2,q=3 transition-dual certificate.

Requires scipy/HiGHS.  The objective is integer-valued; optimum 116 certifies
the normalized dual value 116/180 = 29/45.
"""

from __future__ import annotations

import os
import sys

import numpy as np

EXTRA = "/private/tmp/dynamic-amq-scipy"
if os.path.isdir(EXTRA):
    sys.path.insert(0, EXTRA)

from finite_u_column_generation import PricingMILP, build_histories


def descriptor(pricing: PricingMILP, node: int, query: int):
    operations = []
    while node:
        record = pricing.nodes[node]
        kind = "I" if record.operation < pricing.u else "D"
        operations.append((kind, record.operation % pricing.u))
        node = record.parent
    operations.reverse()
    operations.append(("Q", query))
    rename = {}
    result = []
    for kind, key in operations:
        if key not in rename:
            rename[key] = len(rename)
        result.append((kind, rename[key]))
    return tuple(result)


def main() -> None:
    pricing = PricingMILP(4, 3, build_histories(4, 2, 3))
    orbit_weight = {
        (("Q", 0),): 3,
        (("I", 0), ("I", 1), ("Q", 2)): 5,
        (("I", 0), ("D", 0), ("Q", 1)): 1,
        (("I", 0), ("D", 0), ("I", 1), ("Q", 0)): 1,
        (("I", 0), ("D", 0), ("I", 1), ("Q", 2)): 1,
    }
    weights = np.asarray(
        [orbit_weight.get(descriptor(pricing, node, query), 0)
         for node, query in pricing.fp],
        dtype=float,
    )
    assert int(weights.sum()) == 180
    optimum, _, _ = pricing.price(weights)
    print(f"total_weight={int(weights.sum())}")
    print(f"integer_optimum={optimum:.12g}")
    print(f"normalized={optimum / weights.sum():.12g}")
    if abs(optimum - 116) > 1e-8:
        raise SystemExit("FAIL: expected exact integer optimum 116")
    print("PASS")


if __name__ == "__main__":
    main()
