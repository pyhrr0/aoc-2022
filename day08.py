import math
from typing import Tuple


def solve(input_data: str) -> Tuple[int, int]:
    grid = [list(map(int, line)) for line in example_input.splitlines()]

    visible_locations = 0
    scenic_scores = []

    for row_idx, row in enumerate(grid):
        for column_idx, current_height in enumerate(row):
            row_len = len(row) - 1
            column = [row[column_idx] for row in grid]

            # Part 1
            if row_idx in (0, row_len) or column_idx in (0, row_len)           \
                or all(current_height > tree for tree in row[:column_idx])     \
                or all(current_height > tree for tree in row[column_idx + 1:]) \
                or all(current_height > tree for tree in column[:row_idx + 1]) \
                or all(current_height > tree for tree in column[row_idx:]):
                visible_locations += 1

            # Part 2
            lines_of_sight = (
                column[:row_idx], reversed(column[row_idx + 1:]),
                reversed(row[:column_idx]), row[column_idx + 1:])

            scenic_score = []
            for line_of_sight in lines_of_sight:
                distance = 0
                for tree in line_of_sight:
                    distance += 1
                    if tree >= current_height:
                        break
                scenic_score.append(distance)
            scenic_scores.append(math.prod(scenic_score))

    return (visible_locations, max(scenic_scores))


if __name__ == '__main__':
    example_input = (
        '30373\n'
        '25512\n'
        '65332\n'
        '33549\n'
        '35390\n')

    expected_sum_1 = 21
    expected_sum_2 = 8

    assert solve(example_input) == (expected_sum_1, expected_sum_2)
