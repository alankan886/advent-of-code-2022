from heapq import heappush, heappop

def first_part(calories):
    curr_calories, largest_calories = 0, 0
    for calorie in calories:
        if calorie == '\n':
            largest_calories = max(largest_calories, curr_calories)
            curr_calories = 0
            continue

        curr_calories += int(calorie.rstrip('\n'))
    
    return largest_calories


def second_part(calories):
    min_heap = []
    curr_calories = 0
    for calorie in calories:
        if calorie == '\n':
            heappush(min_heap, curr_calories)
            if len(min_heap) > 3:
                heappop(min_heap)
            curr_calories = 0
            continue

        curr_calories += int(calorie.rstrip('\n'))

    return sum(min_heap)


def main():
    with open('input.txt') as f:
        calories = f.readlines()
        print(first_part(calories))
        print(second_part(calories))


if __name__ == "__main__":
    main()