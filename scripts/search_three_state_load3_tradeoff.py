#!/usr/bin/env python3
"""Enumerate the depth-3 endpoint/deletion relaxation for 3-state layers."""

from itertools import product


WORDS = tuple(range(8))


def bit(word, position):
    return (word >> (2 - position)) & 1


def support_after_delete(word, position):
    mask = 0
    for j in range(3):
        if j != position:
            mask |= 1 << bit(word, j)
    return mask


def main():
    maps = tuple(product(range(3), repeat=3))
    frontier = {}
    witness = {}

    for top in product(range(3), repeat=8):
        top_support = [0, 0, 0]
        for word, state in enumerate(top):
            top_support[state] |= 1 << bit(word, 0)
            top_support[state] |= 1 << bit(word, 1)
            top_support[state] |= 1 << bit(word, 2)

        r3_units = int(not (top_support[top[0]] & 2))
        r3_units += int(not (top_support[top[7]] & 1))
        if not r3_units:
            continue

        for d0 in maps:
            for d1 in maps:
                low_support = [0, 0, 0]
                successors = [[0] * 8 for _ in range(3)]
                for position in range(3):
                    for word in WORDS:
                        db = d1 if bit(word, position) else d0
                        state = db[top[word]]
                        successors[position][word] = state
                        low_support[state] |= support_after_delete(word, position)

                # Units are out of 16: 8 member assignments times 2 query bits.
                r2_units = []
                for position in range(3):
                    units = 0
                    for word in WORDS:
                        state = successors[position][word]
                        query_zero_rejected = not (low_support[state] & 1)
                        query_one_rejected = not (low_support[state] & 2)
                        units += query_zero_rejected + query_one_rejected
                    r2_units.append(units)

                key = (r3_units, min(r2_units), sum(r2_units))
                frontier[key] = frontier.get(key, 0) + 1
                witness.setdefault(key, (top, d0, d1, tuple(r2_units)))

    print("r3_units min_r2_units sum_r2_units count")
    for key in sorted(frontier):
        print(*key, frontier[key])

    print("pareto candidates")
    for key in sorted(frontier):
        r3, low, total = key
        dominated = any(
            r3b >= r3 and lowb >= low and totalb >= total and
            (r3b, lowb, totalb) != key
            for r3b, lowb, totalb in frontier
        )
        if not dominated:
            print(key, witness[key])


if __name__ == "__main__":
    main()
