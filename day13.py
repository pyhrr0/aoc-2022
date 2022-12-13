from functools import cmp_to_key
from typing import List, Tuple, Union


def is_sorted(left: Union[int, List[int]], right: Union[int, List[int]]) -> int:
    if all(isinstance(item, int) for item in (left, right)):
        if left < right: return 1
        if left > right: return -1
        return 0
    else:
        left = list([left]) if isinstance(left, int) else left
        right = list([right]) if isinstance(right, int) else right

        if len(left) == 0 and len(right) != 0: return 1
        if len(right) == 0 and len(left) != 0: return -1
        if len(left) == 0 and len(right) == 0: return 0

        if (return_value := is_sorted(left[0], right[0])) != 0:
            return return_value
        else:
            return is_sorted(left[1:], right[1:])


def solve(input_data: str) -> Tuple[int, int]:
    pairs = [[eval(p) for p in pair.split()] for pair in input_data.split('\n\n')]

    index_sum = 0

    # Part 1
    for idx, (left, right) in enumerate(pairs):
        if is_sorted(left, right) == 1:
            index_sum += idx + 1

    # Part 2
    packets = [eval(line) for line in input_data.split('\n') if line]
    markers = ([[2]], [[6]])
    packets.extend(markers)
    packets.sort(key=cmp_to_key(is_sorted), reverse=True)

    decoder_key = (
        (packets.index(markers[0]) + 1) * (packets.index(markers[1]) + 1))

    return index_sum, decoder_key


if __name__ == '__main__':
    example_input = (
        '[1,1,3,1,1]\n'
        '[1,1,5,1,1]\n'
        '\n'
        '[[1],[2,3,4]]\n'
        '[[1],4]\n'
        '\n'
        '[9]\n'
        '[[8,7,6]]\n'
        '\n'
        '[[4,4],4,4]\n'
        '[[4,4],4,4,4]\n'
        '\n'
        '[7,7,7,7]\n'
        '[7,7,7]\n'
        '\n'
        '[]\n'
        '[3]\n'
        '\n'
        '[[[]]]\n'
        '[[]]\n'
        '\n'
        '[1,[2,[3,[4,[5,6,7]]]],8,9]\n'
        '[1,[2,[3,[4,[5,6,0]]]],8,9]\n')

    expected_sum = 13
    expected_key = 140

    assert solve(example_input) == (expected_sum, expected_key)
