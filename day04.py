from typing import Tuple


def solve(input_data: str) -> Tuple[int, int]:
    sum_1 = 0
    sum_2 = 0

    for line in input_data.splitlines():
        pair_a, pair_b = (pair.split('-') for pair in line.split(','))
        range_a, range_b = (set(
            range(int(pair[0]), int(pair[1]) + 1)) for pair in (pair_a, pair_b))

        # Part 1
        if range_a.issubset(range_b) or range_b.issubset(range_a):
            sum_1 += 1

        # Part 2
        if range_a.intersection(range_b) or range_b.intersection(range_a):
            sum_2 += 1

    return (sum_1, sum_2)


if __name__ == '__main__':
    example_input = (
        '2-4,6-8\n'
        '2-3,4-5\n'
        '5-7,7-9\n'
        '2-8,3-7\n'
        '6-6,4-6\n'
        '2-6,4-8\n')

    expected_sum_1 = 2
    expected_sum_2 = 4

    assert solve(example_input) == (expected_sum_1, expected_sum_2)
