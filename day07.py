import collections
from typing import Tuple


def solve(input_data: str) -> Tuple[int, int]:
    directory_stack = []
    directory_sizes = collections.defaultdict(int)

    for line in input_data.splitlines():
        match line.split():
            case ['$', 'cd', '..']:
                directory_stack.pop()
            case ['$', 'cd', '/']:
                directory_stack.clear()
            case ['$', 'cd', target_dir]:
                directory_stack.append(target_dir)
            case [size, _] if size.isnumeric():
                for offset in range(len(directory_stack) + 1):
                    directory_path = '/' + '/'.join(directory_stack[:offset])
                    directory_sizes[directory_path] += int(size)

    # Part 1
    limit = 100000
    sum_1 = sum(size for size in directory_sizes.values() if size <= limit)

    # Part 2
    total = 70000000
    unused = total - directory_sizes['/']
    required = 30000000 - unused
    sum_2 = min((size for size in directory_sizes.values() if size >= required))

    return (sum_1, sum_2)


if __name__ == '__main__':
    example_input = (
        '$ cd /\n'
        '$ ls\n'
        'dir a\n'
        '14848514 b.txt\n'
        '8504156 c.dat\n'
        'dir d\n$ cd a\n'
        '$ ls\n'
        'dir e\n'
        '29116 f\n'
        '2557 g\n'
        '62596 h.lst\n'
        '$ cd e\n'
        '$ ls\n'
        '584 i\n'
        '$ cd ..\n'
        '$ cd ..\n'
        '$ cd d\n'
        '$ ls\n'
        '4060174 j\n'
        '8033020 d.log\n'
        '5626152 d.ext\n'
        '7214296 k\n')

    expected_sum_1 = 95437
    expected_sum_2 = 24933642

    assert solve(example_input) == (expected_sum_1, expected_sum_2)
