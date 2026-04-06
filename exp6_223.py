import itertools

def generate_sample_space(elements, r):
    print("Elements:", elements)
    print("Outcome length:", r)

    # Permutations (order matters)
    permutations = list(itertools.permutations(elements, r))
    print("\nPermutations Sample Space:")
    for p in permutations:
        print(p)
    print("Total permutations:", len(permutations))

    # Combinations (order does not matter)
    combinations = list(itertools.combinations(elements, r))
    print("\nCombinations Sample Space:")
    for c in combinations:
        print(c)
    print("Total combinations:", len(combinations))


# Example experiment
elements = ['A', 'B', 'C', 'D']
r = 2

generate_sample_space(elements, r)