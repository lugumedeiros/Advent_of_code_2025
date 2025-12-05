class Dial:
    def __init__(self, start_pos:int=50):
        self.pos = start_pos
        self.count = 0

    def rotate(self, rotation_value:int) -> None:
        def is_remainder_greater_than_start_to_zero(start:int, distance:int, is_going_pos:bool):
            partial_distance = distance % 100
            if is_going_pos:
                to_zero = 100 - start
            else:
                to_zero = start
            return partial_distance >= to_zero

        if rotation_value == 0:
            return

        is_going_positive = rotation_value > 0
        start = self.pos
        end = (start + rotation_value) % 100
        distance = abs(rotation_value)
        distance_rotations = distance//100

        if start == 0:
            self._increase_zero_counter(distance_rotations)
        else:
            if is_remainder_greater_than_start_to_zero(start, distance, is_going_positive):
                    self._increase_zero_counter(1)
            self._increase_zero_counter(distance_rotations)
        self.pos = end

    def _increase_zero_counter(self, rotations:int) -> None:
        self.count += rotations

if __name__ == "__main__":
    dial = Dial()
    
    file_name = r"day_1/codes.txt"
    codes = list()
    with open(file_name, "r") as file:
        codes = file.readlines()
    
    for line in codes:
        line = line.strip()
        x = dial.pos
        if 'R' in line:
            dial_value = int(line.replace('R', ''))
        else:
            dial_value = -int(line.replace('L', ''))
        
        dial.rotate(dial_value)
        print(f"Rotation: {dial_value}\t- Start at {x} end at {dial.pos}, zero_count:{dial.count}")
        

