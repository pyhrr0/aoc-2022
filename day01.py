from typing import Tuple


def solve(input_data: str) -> Tuple[int, int]:
    current_accumulative = 0
    elf_calories = []

    for line in input_data.splitlines():
        if line.strip():
            current_accumulative += int(line)
            continue

        elf_calories.append(current_accumulative)
        current_accumulative = 0

    # Part 1
    highest_amount_of_calories = max(elf_calories)

    # Part 2
    backup_amount = sum(sorted(elf_calories[:3], reverse=True))

    return (highest_amount_of_calories, backup_amount)


if __name__ == "__main__":
    example_input = (
        '1000\n'
        '2000\n'
        '3000\n'
        '\n'
        '4000\n'
        '\n'
        '5000\n'
        '6000\n'
        '\n'
        '7000\n'
        '8000\n'
        '9000\n'
        '\n'
        '10000\n')

    expected_amount_1 = 24000
    expected_amount_2 = 21000

    assert solve(example_input) == (expected_amount_1, expected_amount_2)
