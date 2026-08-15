#!/usr/bin/env python3
"""Rational interval certificate for the full integer (q,Q) family.

The analytic reductions leave 28 exact parameter pairs.  This verifier
certifies every remaining competitor above (q,Q)=(3,6), and certifies the
three tail-floor base cases used by the proof.
"""

from fractions import Fraction
from math import factorial

from verify_two_subblock_modulus_sharp_converse import (
    decimal,
    exp_negative_bounds,
    log_bounds,
    LN2_HIGH,
    LN2_LOW,
)


PAIRS = [
    (1, 1), (1, 2), (1, 3),
    (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
    (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
    (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
    (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
    (6, 3), (6, 4),
]

# Decimal centers are used only to choose rational boxes.  Every assertion
# below is evaluated with Fraction arithmetic.
CENTERS = {
    (1,1):(0.69314718056,0.40938389085),(1,2):(1.14619322062,0.45463931414),(1,3):(1.32581907529,0.44777804543),
    (2,1):(1.42673947668,0.44713990227),(2,2):(1.81621131724,0.46394262512),(2,3):(2.11860543504,0.47944291521),(2,4):(2.24314337812,0.47565332470),(2,5):(2.28141043637,0.46788738975),
    (3,1):(1.77356358748,0.43537443627),(3,2):(2.28512267886,0.47001993196),(3,3):(2.47019762301,0.46494335445),(3,4):(2.58782787765,0.46202855252),(3,5):(2.63445009437,0.45735082396),(3,6):(2.64801769402,0.45332084286),(3,7):(2.65099377907,0.45072433276),(3,8):(2.65153628862,0.44928206053),
    (4,2):(2.44471302759,0.45302474796),(4,3):(2.64965336607,0.45251713917),(4,4):(2.71071595786,0.44420006022),(4,5):(2.73783115813,0.43890663428),(4,6):(2.74739119981,0.43563076319),
    (5,2):(2.49093540472,0.43949657471),(5,3):(2.69590827467,0.44000923505),(5,4):(2.75124002499,0.43265974234),(5,5):(2.76368869679,0.42688341663),(5,6):(2.76777340504,0.42373037064),
    (6,3):(2.70662392926,0.43263873613),(6,4):(2.75941635384,0.42591287054),
}


def add(x, y, q, Q):
    return ((x[0] + y[0]) % Q, (x[1] + y[1]) % q, (x[2] + y[2]) % q)


def subtract(x, y, q, Q):
    return ((x[0] - y[0]) % Q, (x[1] - y[1]) % q, (x[2] - y[2]) % q)


def profile(q, Q):
    increments = ((1 % Q, 0, 0), (1 % Q, 1 % q, 0), (0, 0, 0), (0, 0, 1 % q))
    reachable = {(0, 0, 0)}
    walk = {(0, 0, 0): 1}
    states, rejection = [], []
    for load in range(Q + 2 * q + 5):
        states.append(len(reachable))
        rejected = 4 if load == 0 else sum(
            multiplicity * sum(subtract(s, v, q, Q) not in previous for v in increments)
            for s, multiplicity in walk.items()
        )
        rejection.append(Fraction(rejected, 4 ** (load + 1)))
        if load and len(reachable) == len(previous):
            assert rejected == 0
            return states, rejection
        previous = reachable
        reachable = {add(s, v, q, Q) for s in reachable for v in increments}
        next_walk = {}
        for s, multiplicity in walk.items():
            for v in increments:
                t = add(s, v, q, Q)
                next_walk[t] = next_walk.get(t, 0) + multiplicity
        walk = next_walk
    raise AssertionError("sumset did not stabilize")


def poisson_bounds(rejection, lam):
    p = sum(rejection[c] * lam**c / factorial(c) for c in range(len(rejection)))
    e_low, e_high = exp_negative_bounds(lam)
    return e_low * p, e_high * p


def ogf(states, z):
    k = len(states) - 1
    return sum(states[c] * z**c for c in range(k)) + states[-1] * z**k / (1-z)


def mean(states, z):
    k = len(states) - 1
    numerator = sum(c * states[c] * z**c for c in range(k))
    numerator += states[-1] * (k*z**k/(1-z) + z**(k+1)/(1-z)**2)
    return numerator / ogf(states, z)


def lower_rate(states, lam_high, z_low, z_high):
    log_a_low, _ = log_bounds(ogf(states, z_low))
    _, log_z_high = log_bounds(z_high)
    return (log_a_low / lam_high - log_z_high) / LN2_HIGH


def upper_rate(states, lam_low, z):
    _, log_a_high = log_bounds(ogf(states, z))
    log_z_low, _ = log_bounds(z)
    return (log_a_high / lam_low - log_z_low) / LN2_LOW


def rational_box(center, radius_text):
    center_fraction = Fraction(str(center))
    radius = decimal(radius_text)
    return center_fraction - radius, center_fraction + radius


def exact_composition_floor_states(k):
    # Exact four-symbol compositions through loads < k, frozen thereafter.
    prefix = [(c+1)*(c+2)*(c+3)//6 for c in range(k)]
    return prefix + [prefix[-1]]


def independent_count(c, q):
    return sum(min(a+1,q)*min(c-a+1,q) for a in range(c+1))


def horizontal_floor_states(q, cutoff):
    prefix = [independent_count(c,q) for c in range(cutoff)]
    return prefix + [prefix[-1]]


def vertical_exact_state(c, Q):
    return len({(a % Q, u, v) for a in range(c+1) for u in range(a+1) for v in range(c-a+1)})


def vertical_floor_states(Q, cutoff):
    prefix = [vertical_exact_state(c,Q) for c in range(cutoff)]
    return prefix + [prefix[-1]]


def binary_uncoupled_rejection_bounds(q, lam):
    # exp(-lam/2) sum_{t<q} (lam/4)^t/t!
    p = sum((lam/4)**t/factorial(t) for t in range(q))
    e_low,e_high = exp_negative_bounds(lam/2)
    return e_low*p,e_high*p


def infinite_q_rejection_bounds(Q, lam):
    # 1/2 exp(-lam/4) + 1/2 exp(-lam/2) sum_{t<Q}(lam/4)^t/t!.
    e1_low,e1_high = exp_negative_bounds(lam/4)
    e2_low,e2_high = exp_negative_bounds(lam/2)
    p = sum((lam/4)**t/factorial(t) for t in range(Q))
    return (e1_low+e2_low*p)/2,(e1_high+e2_high*p)/2


def certify_floor(states, rejection_bounds, lam_center, z_center, winner_upper):
    lam_low,lam_high = rational_box(lam_center,"0.00000000003")
    z_low,z_high = rational_box(z_center,"0.00000000008")
    assert rejection_bounds(lam_low)[0] > Fraction(1,2)
    assert rejection_bounds(lam_high)[1] < Fraction(1,2)
    assert mean(states,z_low) < lam_low
    assert mean(states,z_high) > lam_high
    value = lower_rate(states,lam_high,z_low,z_high)
    assert value > winner_upper
    return value


def main():
    winner_states,winner_rejection = profile(3,6)
    wl,wh = rational_box(CENTERS[(3,6)][0],"0.00000000003")
    assert poisson_bounds(winner_rejection,wl)[0] > Fraction(1,2)
    assert poisson_bounds(winner_rejection,wh)[1] < Fraction(1,2)
    winner_upper = upper_rate(winner_states,wl,Fraction(str(CENTERS[(3,6)][1])))

    for pair in PAIRS:
        if pair == (3,6): continue
        states,rejection = profile(*pair)
        lam_low,lam_high = rational_box(CENTERS[pair][0],"0.00000000003")
        z_low,z_high = rational_box(CENTERS[pair][1],"0.00000000008")
        assert poisson_bounds(rejection,lam_low)[0] > Fraction(1,2)
        assert poisson_bounds(rejection,lam_high)[1] < Fraction(1,2)
        assert mean(states,z_low) < lam_low
        assert mean(states,z_high) > lam_high
        assert lower_rate(states,lam_high,z_low,z_high) > winner_upper

    # min(q,Q)>=6: exact four-composition prefix through load 5.
    floor66 = exact_composition_floor_states(6)
    # Grant impossible exact-composition rejection forever: lambda=4 ln 2.
    lam_low,lam_high = rational_box(4*0.6931471805599453,"0.00000000004")
    z_low,z_high = rational_box(0.445486958780,"0.0000000001")
    assert mean(floor66,z_low)<lam_low and mean(floor66,z_high)>lam_high
    assert lower_rate(floor66,lam_high,z_low,z_high)>winner_upper

    # Horizontal tails q<=5.  The first excluded Q values are 4,6,9,7,7.
    horizontal = {
      1:(4,1.3862943611198906,0.48030248744),
      2:(6,2.292386441241165,0.46302155570),
      3:(9,2.651638150570379,0.45004638029),
      4:(7,2.750882493096711,0.43162744660),
      5:(7,2.769593828861186,0.43075835200),
    }
    for q,(cutoff,lam,z) in horizontal.items():
        states=horizontal_floor_states(q,cutoff)
        certify_floor(states,lambda x,q=q:binary_uncoupled_rejection_bounds(q,x),lam,z,winner_upper)

    # Vertical tails Q<=5. First excluded q values are 4,6,7,7,6.
    vertical = {
      1:(4,1.924847300238413,0.4737080650),
      2:(6,2.502820701761675,0.4635904200),
      3:(7,2.709212213967896,0.4380508400),
      4:(7,2.761603186844337,0.4342886900),
      5:(6,2.771087971410293,0.4403502600),
    }
    for Q,(cutoff,lam,z) in vertical.items():
        states=vertical_floor_states(Q,cutoff)
        certify_floor(states,lambda x,Q=Q:infinite_q_rejection_bounds(Q,x),lam,z,winner_upper)

    print("Q=6,q=3 upper",float(winner_upper))
    print("PASS")


if __name__ == "__main__": main()
