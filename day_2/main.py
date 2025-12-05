class PatternFinder:
    memory = dict()

    def get_factors(self, value:int) -> list:
        assert value>=2
        
        factor_mem = self.memory.get(value)
        if factor_mem is not None:
            return factor_mem
        
        factor_list = list()

        for i in range(2, value+1):
            if value / i == value // i:
                factor_list.append(i)
        self.memory[value] = factor_list
        return factor_list

    def has_pattern(self, value:str|list, is_first_challenge:bool=False) -> bool:
        if len(value) <= 1:
            return False, 0
        
        factor_list = self.get_factors(len(value))
        
        if is_first_challenge:
            if len(value) // 2 != len(value) / 2:
                return False, 0
            factor_list = [2]

        for factor in factor_list:
            id_pieces = list()
            current_piece = 0
            for _ in range(factor):
                temp_piece = value[current_piece : current_piece + len(value) // factor]
                id_pieces.append("".join(temp_piece))
                current_piece += len(value) // factor
            
            temp_result = True
            first_piece = id_pieces[0]
            next_pieces = id_pieces[1:]
            for next_piece in next_pieces:
                if first_piece != next_piece:
                    temp_result = False
                    break
            if temp_result:
                return True, int(first_piece)
        return False, 0

if __name__ == "__main__":
    patternFinder = PatternFinder()
    
    file_name = r"day_2/codes.txt"
    codes = ""
    with open(file_name, "r") as file:
        codes = file.readline()
    
    code_list = list()
    invalid_count = 0
    invalid_sum = 0
    for code_pair in codes.split(","):
        left = code_pair.split("-")[0]
        right = code_pair.split("-")[1]
        for i in range(int(left), int(right) +1):
            test_result, pattern = patternFinder.has_pattern(list(str(i)))
            if test_result:
                invalid_count += 1
                invalid_sum += i
                print(f"{i}? {test_result}, patter={pattern}")
    print(f"result = {invalid_count}, sum = {invalid_sum}")

        