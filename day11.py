import math
from types import SimpleNamespace
from typing import List


def parse(input_data: str) -> List[SimpleNamespace]:
    monkeys = []

    for block in example_input.split('\n\n'):
        monkey = SimpleNamespace(inspections=0)

        for line in block.splitlines():
            match line.split(': '):
                case ['  Starting items', items]:
                    monkey.items = list(map(int, items.split(', ')))
                case ['  Operation', operation]:
                    monkey.operation = operation.split(' = ')[1]
                case ['  Test', test]:
                    monkey.worry_divisor = int(test.split()[-1])
                case ['    If true', branch]:
                    monkey.branch_a = int(branch.split()[-1])
                case ['    If false', branch]:
                    monkey.branch_b = int(branch.split()[-1])

        monkeys.append(monkey)

    return monkeys


def solve(input_data: str, part: int) -> int:
    monkeys = parse(input_data)
    worry_reducer = math.prod(monkey.worry_divisor for monkey in monkeys)

    rounds = 20 if part == 1 else 10000

    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                old = item
                item = eval(monkey.operation)

                if part == 1:
                    item //= 3 # Part 1
                else:
                    item %= worry_reducer # Part 2

                recipient = monkeys[monkey.branch_b]
                if item % monkey.worry_divisor == 0:
                    recipient = monkeys[monkey.branch_a]
                recipient.items.append(item)

                monkey.inspections += 1
            monkey.items.clear()

    monkey_business = math.prod(
        sorted([monkey.inspections for monkey in monkeys])[-2:])

    return monkey_business


if __name__ == "__main__":
    example_input = (
        'Monkey 0:\n'
        '  Starting items: 79, 98\n'
        '  Operation: new = old * 19\n'
        '  Test: divisible by 23\n'
        '    If true: throw to monkey 2\n'
        '    If false: throw to monkey 3\n'
        '\n'
        'Monkey 1:\n'
        '  Starting items: 54, 65, 75, 74\n'
        '  Operation: new = old + 6\n'
        '  Test: divisible by 19\n'
        '    If true: throw to monkey 2\n'
        '    If false: throw to monkey 0\n'
        '\n'
        'Monkey 2:\n'
        '  Starting items: 79, 60, 97\n'
        '  Operation: new = old * old\n'
        '  Test: divisible by 13\n'
        '    If true: throw to monkey 1\n'
        '    If false: throw to monkey 3\n'
        '\n'
        'Monkey 3:\n'
        '  Starting items: 74\n'
        '  Operation: new = old + 3\n'
        '  Test: divisible by 17\n'
        '    If true: throw to monkey 0\n'
        '    If false: throw to monkey 1\n')

    expected_amount_1 = 10605
    expected_amount_2 = 2713310158

    assert solve(example_input, part=1) == expected_amount_1
    assert solve(example_input, part=2) == expected_amount_2
