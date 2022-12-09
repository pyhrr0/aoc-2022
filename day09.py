def solve(input_data: str, knot_count: int) -> int:
    rope = [[0, 0] for _ in range(knot_count)]

    tail_positions = set([tuple(rope[-1])])

    for line in input_data:
        direction, distance = line.split()

        # Part 1 & Part 2
        for _ in range(int(distance)):
            match direction:
                case 'U': rope[0][1] += 1
                case 'D': rope[0][1] -= 1
                case 'L': rope[0][0] -= 1
                case 'R': rope[0][0] += 1

            for knot_idx in range(1, knot_count):
                current_knot = rope[knot_idx]
                leading_knot = rope[knot_idx - 1]

                row_delta = leading_knot[0] - current_knot[0]
                row_delta_abs = abs(row_delta)

                column_delta = leading_knot[1] - current_knot[1]
                column_delta_abs = abs(column_delta)

                if row_delta_abs > 1 or column_delta_abs > 1:
                    if row_delta:
                        row_offset = row_delta // row_delta_abs
                        current_knot[0] += row_offset

                    if column_delta:
                        column_offset = column_delta // column_delta_abs
                        current_knot[1] += column_offset

                tail_positions.add(tuple(rope[-1]))

    return len(tail_positions)


if __name__ == '__main__':
    knot_count_1 = 2
    example_input_1 = ('R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2')

    knot_count_2 = 10
    example_input_2 = ('R 5', 'U 8', 'L 8', 'D 3', 'R 17', 'D 10', 'L 25', 'U 20')

    expected_sum_1 = 13
    expected_sum_2 = 36

    assert solve(example_input_1, knot_count_1) == expected_sum_1
    assert solve(example_input_2, knot_count_2) == expected_sum_2
