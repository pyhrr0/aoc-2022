from typing import Tuple


def solve(input_data: str) -> Tuple[int, int]:
    initial_state = dict()

    for line in input_data.splitlines():
        stack_offsets = (
            i for i, character in enumerate(line) if character == '[')

        for offset in stack_offsets:
            current_stack = (offset // 3) + 1
            if current_stack not in initial_state:
                initial_state[current_stack] = []

            initial_state[current_stack].append(line[offset + 1])

        if not line:
            stacks_1 = initial_state
            stacks_2 = initial_state.copy()

        if line[:4] == 'move':
            number_of_crates, source, destination = (
                int(character) for character in line if character.isnumeric())

            # Part 1
            current_load = stacks_1[source][:number_of_crates][::-1]
            stacks_1[source] = stacks_1[source][number_of_crates:]
            stacks_1[destination] = current_load + stacks_1[destination]

            # Part 2
            current_load = stacks_2[source][:number_of_crates]
            stacks_2[source] = stacks_2[source][number_of_crates:]
            stacks_2[destination] = current_load + stacks_2[destination]

    message_1 = ''.join((
        stacks_1[stack_id][0] for stack_id in sorted(stacks_1.keys())))

    message_2 = ''.join((
        stacks_2[stack_id][0] for stack_id in sorted(stacks_2.keys())))

    return (message_1, message_2)


if __name__ == '__main__':
    example_input = (
        '    [D]    \n'
        '[N] [C]    \n'
        '[Z] [M] [P]\n'
        ' 1   2   3 \n'
        '\n'
        'move 1 from 2 to 1\n'
        'move 3 from 1 to 3\n'
        'move 2 from 2 to 1\n'
        'move 1 from 1 to 2\n')

    expected_message_1 = 'CMZ'
    expected_message_2 = 'MCD'

    assert solve(example_input) == (expected_message_1, expected_message_2)
