def is_pos_valid(matrix, pos_x, pos_y):
    x_bound = len(matrix[0])
    y_bound = len(matrix)
    return -1 <pos_x < x_bound and -1 < pos_y < y_bound

def get_neighboors_sum(matrix, pos_x, pos_y) -> int:
    def is_not_neighboor(x, pos_x, y, pos_y):
        return x == pos_x and y == pos_y
    
    neighboor_sum = 0
    for x in range(pos_x-1, pos_x+2):
        for y in range(pos_y-1, pos_y+2):
            x = x
            y = y
            if is_not_neighboor(x, pos_x, y, pos_y):
                continue
            if is_pos_valid(matrix, x, y):
                neighboor_sum += matrix[x][y]
    return neighboor_sum

def get_neighboor_matrix(matrix:list[list]):
    sum_matrix = list()
    for x in range(len(matrix)):
        sum_row = list()
        for y in range(len(matrix[x])):
            sum_pos = get_neighboors_sum(matrix, x, y)
            sum_row.append(sum_pos)
        sum_matrix.append(sum_row)
    return sum_matrix

def get_masked_matrix(matrix, mask_matrix):
    new_matrix = list()
    for x in range(len(matrix)):
        new_row = list()
        for y in range(len(matrix[0])):
            if mask_matrix[x][y] == 1:
                new_row.append(matrix[x][y])
            else:
                new_row.append(0)
        new_matrix.append(new_row)
    return new_matrix

def get_less_than_4_matrix(matrix):
    new_matrix = list()
    for y in matrix:
        new_row = list()
        for value in y:
            test = 1 if value < 4 else 0
            new_row.append(test)
        new_matrix.append(new_row)
    return new_matrix        


if __name__ == "__main__":
    
    file_name = r"day_4/codes.txt"
    codes = ""
    with open(file_name, "r") as file:
        codes = file.readlines()
    
    paper_matrix = list()
    for line in codes:
        row = list()
        line = line.replace("\n", "")
        for char in line:
            value = 1 if char == "@" else 0
            row.append(value)
        paper_matrix.append(row)
    

    print("=========== Matrix ===========")
    for i in paper_matrix:
        print(i)
    print("\n")

    neighboor_matrix = get_neighboor_matrix(paper_matrix)
    print("========== SUMatrix ==========")
    for i in neighboor_matrix:
        print(i)
    print("\n")

    less_than_4_sum_matrix = get_less_than_4_matrix(neighboor_matrix)
    print("======== Less4_Matrix ========")
    for row in less_than_4_sum_matrix:
        print(row)
    print("\n")

    masked_matrix = get_masked_matrix(less_than_4_sum_matrix, paper_matrix)
    print("======== Masked_Matrix ========")
    for i in masked_matrix:
        print(i)
    print("\n")

    valid_positions = 0
    for row in masked_matrix:
        for pos in row:
            if pos == 1:
                valid_positions += 1
    
    print(f"Valid SUM: {valid_positions}")


