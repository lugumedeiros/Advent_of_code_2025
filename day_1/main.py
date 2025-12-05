class Dial:
    def __init__(self):
        self.pos = 50
        self.count = 0

    def rotate(self, rotation_value:int) -> None:
        if rotation_value == 0:
            return

        is_going_right = rotation_value > 0
        start = self.pos
        end = (start + rotation_value) % 100
        distance = abs(rotation_value)

        if start == 0:
            self._increase_zero_counter(distance//100)
        else:
            partial_distance = distance % 100
            if is_going_right:
                if (partial_distance >= 100 - start):
                    self._increase_zero_counter(1)
            else:
                if (partial_distance >= start):
                    self._increase_zero_counter(1)
            self._increase_zero_counter(distance // 100)
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
        print(f"{dial_value}: start at {x} end at {dial.pos}, zero_pass:{dial.count}")
        

