def calc_score(rounds, rules):
    total_score = 0
    for round in rounds:
        elf, me = round.strip("\n").split(" ")
        total_score += rules[elf][me]
    
    return total_score

def main():
    first_part_rules = {
        "A": {"X": 4, "Y": 8, "Z": 3},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 7, "Y": 2, "Z": 6}
    }
    second_part_rules = {
        "A": {"X": 3, "Y": 4, "Z": 8},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 2, "Y": 6, "Z": 7}
    }
    with open('input.txt') as f:
        rounds = f.readlines()
        print(calc_score(rounds, first_part_rules))
        print(calc_score(rounds, second_part_rules))


if __name__ == "__main__":
    main()