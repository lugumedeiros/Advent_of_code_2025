def find_positions_in_list(char_to_check:str, list_to_test:list) -> list:
    positions = list()
    for idx, char in enumerate(list_to_test):
        if char == char_to_check:
            positions.append(idx)
    return positions

class PathWay:
    memory = dict()

    def get_max_number_trail(self, main_trail:int, trail_lines:list[list], trail_lines_start:int=0):
        coordenates = f"{main_trail}-{trail_lines_start}"
        from_memory = self.memory.get(coordenates)
        if from_memory is not None:
            return from_memory
        
        for line_idx in range(trail_lines_start, len(trail_lines)):
            line = trail_lines[line_idx]
            for char in line:
                if char == main_trail:
                    left = self.get_max_number_trail(main_trail+1, trail_lines, line_idx+1)
                    right = self.get_max_number_trail(main_trail-1, trail_lines, line_idx+1)
                    result = left + right
                    self.memory[coordenates] = result
                    return result
        self.memory[coordenates] = 1
        return 1


if __name__ == "__main__":
    
    PART_ONE = False

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
    
    else:
        path_finder = PathWay()
        sum_paths = path_finder.get_max_number_trail(start_position, split_positions_lines)
        print("possible paths:", sum_paths)