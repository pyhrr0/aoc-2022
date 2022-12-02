from typing import Tuple


def solve(input_data: str) -> Tuple[int, int]:
    elf1_symbols = ('A', 'B', 'C')
    elf2_symbols = ('X', 'Y', 'Z')
    scores = (0, 3, 6)

    score_1 = 0
    score_2 = 0

    for line in input_data.splitlines():
        elf1_move, elf2_symbol = line.split()
        elf1_score = elf1_symbols.index(elf1_move) + 1

        # Part 1
        elf2_score = elf2_symbols.index(elf2_symbol) + 1
        score_1 += elf2_score + scores[((elf2_score - elf1_score) + 1) % 3]

        # Part 2
        implied_score = ((elf1_score + elf2_symbols.index(elf2_symbol)) - 1) % 3
        score_2 += implied_score + scores[elf2_symbols.index(elf2_symbol)]

    return (score_1, score_2)


if __name__ == '__main__':
    example_input = (
        'A Y\n'
        'B X\n'
        'C Z\n')

    expected_score_1 = 15
    expected_score_2 = 12

    assert solve(example_input) == (expected_score_1, expected_score_2)
