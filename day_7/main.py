def find_positions_in_list(char_to_check:str, list_to_test:list) -> list:
    positions = list()
    for idx, char in enumerate(list_to_test):
        if char == char_to_check:
            positions.append(idx)
    return positions


if __name__ == "__main__":
    
    PART_ONE = True

    file_name = r"day_7/codes.txt"
    codes = ""
    with open(file_name, "r") as file:
        codes = file.readlines()

    start_position = find_positions_in_list('S', list(codes[0]))[0]
    split_positions_lines = [find_positions_in_list('^', list(line)) for line in codes]

    if PART_ONE:
        sum_of_splits = 0
        beams_dropping_current = set()
        beams_dropping_current.add(start_position)
        for line in split_positions_lines:
            for split_pos in line:
                if split_pos in beams_dropping_current:
                    sum_of_splits += 1
                    beams_dropping_current.remove(split_pos)
                    beams_dropping_current.add(split_pos+1)
                    beams_dropping_current.add(split_pos-1)
        print("Splits:", sum_of_splits)