import heapq
import string


def height(character: str) -> int:
    match character:
        case 'S': return string.ascii_lowercase.index('a')
        case 'E': return string.ascii_lowercase.index('z')
        case _: return string.ascii_lowercase.index(character)


def solve(input_data: str, part: int) -> int:
    row_len = 8

    locations = input_data.replace('\n', '')
    start_idx = locations.find('S')
    end_idx = locations.find('E')

    if part == 1:
        heap = [(0, start_idx)]
        condition = lambda current_height, adjacent_hight: \
            adjacent_height <= current_height + 1
    else:
        condition = lambda current_height, adjacent_hight: \
            adjacent_height >= current_height - 1
        heap = [(0, end_idx)]

    visited = [False for _ in range(len(locations))]
    lowest_cost = None

    while True:
        steps, current_location_idx = heapq.heappop(heap)
        current_height = height(locations[current_location_idx])

        if visited[current_location_idx]:
            continue

        if (current_location_idx == end_idx and part == 1) \
           or (current_height == 0 and part == 2):
            lowest_cost = steps
            break

        for offset in (-row_len, row_len, -1, 1):
            next_location_idx = current_location_idx + offset

            if not (0 <= next_location_idx <= len(locations) - 1):
                continue

            adjacent_height = height(locations[next_location_idx])

            if condition(current_height, adjacent_height):
                heapq.heappush(heap, (steps + 1, next_location_idx))

        visited[current_location_idx] = True

    return lowest_cost


if __name__ == '__main__':
    example_input = (
        'Sabqponm\n'
        'abcryxxl\n'
        'accszExk\n'
        'acctuvwj\n'
        'abdefghi\n')

    expected_amount_1 = 31
    expected_amount_2 = 29

    assert solve(example_input, part=1) == expected_amount_1
    assert solve(example_input, part=2) == expected_amount_2
