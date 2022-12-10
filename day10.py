from typing import Tuple


def solve(input_data: str) -> Tuple[int, int]:
    cycle_count = 0
    register_x = 1

    signal_strengths = []
    pixels = []

    for line in input_data:
        cycle_cost = 0
        value = None

        match line.split():
            case ['noop']:
                cycle_cost += 1
            case ['addx', argument]:
                cycle_cost += 2
                value = int(argument)

        for _ in range(cycle_cost):
            cycle_count += 1

            # Part 1
            if (cycle_count - 20) % 40 == 0:
                signal_strengths.append(cycle_count * register_x)

            # Part 2
            crt_position = ((cycle_count - 1) % 40)
            if abs(crt_position - register_x) <= 1:
                pixels.append('#')
            else:
                pixels.append('.')

        if value:
            register_x += value

    return (sum(signal_strengths), tuple(pixels))


if __name__ == '__main__':
    example_input = (
        'addx 15', 'addx -11', 'addx 6', 'addx -3', 'addx 5', 'addx -1', 'addx -8',
        'addx 13', 'addx 4', 'noop', 'addx -1', 'addx 5', 'addx -1', 'addx 5',
        'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx -35', 'addx 1',
        'addx 24', 'addx -19', 'addx 1', 'addx 16', 'addx -11', 'noop', 'noop',
        'addx 21', 'addx -15', 'noop', 'noop', 'addx -3', 'addx 9', 'addx 1',
        'addx -3', 'addx 8', 'addx 1', 'addx 5', 'noop', 'noop', 'noop', 'noop',
        'noop', 'addx -36', 'noop', 'addx 1', 'addx 7', 'noop', 'noop', 'noop',
        'addx 2', 'addx 6', 'noop', 'noop', 'noop', 'noop', 'noop', 'addx 1',
        'noop', 'noop', 'addx 7', 'addx 1', 'noop', 'addx -13', 'addx 13',
        'addx 7', 'noop', 'addx 1', 'addx -33', 'noop', 'noop', 'noop', 'addx 2',
        'noop', 'noop', 'noop', 'addx 8', 'noop', 'addx -1', 'addx 2', 'addx 1',
        'noop', 'addx 17', 'addx -9', 'addx 1', 'addx 1', 'addx -3', 'addx 11',
        'noop', 'noop', 'addx 1', 'noop', 'addx 1', 'noop', 'noop', 'addx -13',
        'addx -19', 'addx 1', 'addx 3', 'addx 26', 'addx -30', 'addx 12',
        'addx -1', 'addx 3', 'addx 1', 'noop', 'noop', 'noop', 'addx -9',
        'addx 18', 'addx 1', 'addx 2', 'noop', 'noop', 'addx 9', 'noop', 'noop',
        'noop', 'addx -1', 'addx 2', 'addx -37', 'addx 1', 'addx 3', 'noop',
        'addx 15', 'addx -21', 'addx 22', 'addx -6', 'addx 1', 'noop', 'addx 2',
        'addx 1', 'noop', 'addx -10', 'noop', 'noop', 'addx 20', 'addx 1',
        'addx 2', 'addx 2', 'addx -6', 'addx -11', 'noop', 'noop', 'noop')

    expected_sum = 13140
    expected_pixels = tuple(
        '##..##..##..##..##..##..##..##..##..##..'
        '###...###...###...###...###...###...###.'
        '####....####....####....####....####....'
        '#####.....#####.....#####.....#####.....'
        '######......######......######......####'
        '#######.......#######.......#######.....')

    assert solve(example_input) == (expected_sum, expected_pixels)
