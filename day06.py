from typing import Tuple


def solve(input_data: str) -> Tuple[int, int]:
    sequence_size_1 = 4
    sequence_size_2 = 14

    markers_1 = []
    markers_2 = []

    for line in input_data.splitlines():
        # Part 1
        for offset in range(len(line)):
            current_sequence = set(line[offset:offset + sequence_size_1])
            if len(current_sequence) == sequence_size_1:
                markers_1.append(offset + sequence_size_1)
                break

        # Part 2
        for offset in range(len(line)):
            current_sequence = set(line[offset:offset + sequence_size_2])
            if len(current_sequence) == sequence_size_2:
                markers_2.append(offset + sequence_size_2)
                break

    return (tuple(markers_1), tuple(markers_2))


if __name__ == '__main__':
    example_input = (
        'mjqjpqmgbljsphdztnvjfqwrcgsmlb\n'
        'bvwbjplbgvbhsrlpgdmjqwftvncz\n'
        'nppdvjthqldpwncqszvftbrmjlhg\n'
        'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg\n'
        'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw\n')

    expected_markers_1 = (7, 5, 6, 10, 11)
    expected_markers_2 = (19, 23, 23, 29, 26)

    assert solve(example_input) == (expected_markers_1, expected_markers_2)
