import itertools


def subsets(universe_size, size):
    return [
        frozenset(items)
        for items in itertools.combinations(range(universe_size), size)
    ]


def state_supports(true_sets, rejected_sets):
    supports = []
    universe = frozenset().union(*true_sets)
    for rejected in rejected_sets:
        supports.append(
            {
                true_set
                for true_set in true_sets
                if rejected <= universe - true_set
            }
        )
    return supports


def support_closure_obstructions(true_sets, supports):
    universe = frozenset().union(*true_sets)
    obstructions = []

    for x in universe:
        for y in universe:
            if x == y:
                continue

            for state, fiber in enumerate(supports):
                sources = {
                    true_set
                    for true_set in fiber
                    if x in true_set and y not in true_set
                }
                if not sources:
                    continue

                targets = {
                    frozenset((set(true_set) - {x}) | {y})
                    for true_set in sources
                }
                common_output_states = {
                    output_state
                    for output_state, output_fiber in enumerate(supports)
                    if targets <= output_fiber
                }
                if not common_output_states:
                    obstructions.append((x, y, state, sources, targets))

    return obstructions


def n2_four_state_example():
    universe_size = 4
    true_sets = subsets(universe_size, 2)
    rejected_sets = subsets(universe_size, 1)
    supports = state_supports(true_sets, rejected_sets)
    return support_closure_obstructions(true_sets, supports)


def n3_twelve_state_candidate():
    universe_size = 6
    true_sets = subsets(universe_size, 3)
    perfect_matching = {
        frozenset((0, 1)),
        frozenset((2, 3)),
        frozenset((4, 5)),
    }
    rejected_sets = [
        pair
        for pair in subsets(universe_size, 2)
        if pair not in perfect_matching
    ]
    supports = state_supports(true_sets, rejected_sets)
    return rejected_sets, support_closure_obstructions(true_sets, supports)


if __name__ == "__main__":
    print("n=2 four-state obstructions:", len(n2_four_state_example()))

    rejected_sets, obstructions = n3_twelve_state_candidate()
    print("n=3 twelve-state obstructions:", len(obstructions))
    if obstructions:
        x, y, state, sources, targets = obstructions[0]
        print("first label:", (x, y))
        print("input rejected set:", sorted(rejected_sets[state]))
        print("source sets:", sorted(map(sorted, sources)))
        print("target sets:", sorted(map(sorted, targets)))
