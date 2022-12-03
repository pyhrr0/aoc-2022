import string
from typing import Tuple


def solve(input_data: str) -> Tuple[int, int]:
    sum_1 = 0
    sum_2 = 0
    rucksack_group = []

    for line in input_data.splitlines():
        chunk_len = len(line) // 2
        compartment_a, compartment_b = line[:chunk_len], line[chunk_len:]

        # Part 1
        for item_type in compartment_a:
            if item_type in compartment_b:
                sum_1 += string.ascii_letters.index(item_type) + 1
                break

        # Part 2
        rucksack_group.append(line)
        if len(rucksack_group) == 3:
            largest_rucksack_idx = rucksack_group.index(max(rucksack_group))
            idx_a, idx_b = (
                (largest_rucksack_idx % 3) - 1, (largest_rucksack_idx % 3) - 2)

            for item_type in rucksack_group[largest_rucksack_idx]:
                rucksacks = (rucksack_group[idx_a], rucksack_group[idx_b])
                if all(item_type in rucksack for rucksack in rucksacks):
                    sum_2 += string.ascii_letters.index(item_type) + 1
                    rucksack_group.clear()
                    break

    return (sum_1, sum_2)


if __name__ == '__main__':
    example_input = (
        'vJrwpWtwJgWrhcsFMMfFFhFp\n'
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n'
        'PmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n'
        'ttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw\n')

    expected_sum_1 = 157
    expected_sum_2 = 70

    assert solve(example_input) == (expected_sum_1, expected_sum_2)
