from math import sqrt

class Position:
    def __init__(self, x:int, y:int, z:int, id:int):
        self.x = x
        self.y = y
        self.z = z
        self.parent = None
        self.id = id
        self.children = []

    def get_name(self) -> str:
        return f"{self.x},{self.y},{self.z}"

def get_distance(a:"Position", b:"Position") -> int|float:
    step_x = (a.x - b.x) ** 2 
    step_y = (a.y - b.y) ** 2
    step_z = (a.z - b.z) ** 2
    result = sqrt(step_x + step_y + step_z)
    return result
        
def get_positions_from_code(codes:list) -> list[Position]:
    positions = list()
    id = 0
    for line in codes:
        pos = line.split(",")
        x = int(pos[0])
        y = int(pos[1])
        z = int(pos[2])
        positions.append(Position(x,y,z, id))
        id += 1

    return positions

def get_max_values(list_values:list, values=3) -> list:
    max_values = []
    for _ in range(values):
        max_value = 0
        idx = 0
        for i in range(len(list_values)):
            if list_values[i] > max_value:
                max_value = list_values[i]
                idx = i
        max_values.append(max_value)
        list_values.pop(idx)
    return max_values


if __name__ == "__main__":
    
    PART_ONE = False
    DEBUG = False

    file_name = r"day_8/codes.txt"
    codes = ""
    with open(file_name, "r") as file:
        codes = file.readlines()

    ######### DISTANCES SORTED ##################################
    position_list = get_positions_from_code(codes)
    distance_list = []
    for net_id in range (0, len(position_list)-1):
        first_pos = position_list[net_id]
        for second_pos in position_list[net_id+1:]:
            distance = get_distance(first_pos, second_pos)
            distance_list.append((distance, first_pos, second_pos))

    sorted_distance_list = sorted(distance_list, key=lambda x: x[0])
     ############################################################
    if DEBUG:
        # Vizualize all distances points
        count = 0
        for dist, a, b in sorted_distance_list:
            print(f"{a.get_name()} : {b.get_name()} - {dist}")
            count += 1
            if count >= 1000: # end earlier
                break
    
    ######## NET CREATION #########################################
    net_map = dict()
    for x in range(len(position_list)):
        net_map[x] = x

    max_count = 1000
    current_count = 1
    for distance, node_a, node_b in sorted_distance_list:
        id_a = node_a.id
        id_b = node_b.id
        net_a = net_map.get(id_a)
        net_b = net_map.get(id_b)
        if DEBUG:
            print(f"TEST: {id_a} : {id_b}")

        if net_a is not None and net_b is None:
            net_map[id_b] = net_a
        
        if net_b is None and net_b is not None:
            net_map[id_a] = net_b
        
        if net_b != net_a:
            for id, net in net_map.items():
                if net == net_b:
                    net_map[id] = net_a
        if DEBUG:
            print(net_map, "\n")
        if current_count < max_count:
            current_count += 1
        else:
            break
    
    ##########################################################

    net_id_count_list = list()
    for id in range(len(position_list)):
        count = 0
        for node_id, net_id in net_map.items():
            if net_id == id:
                count += 1
        net_id_count_list.append(count)
    
    print(get_max_values(net_id_count_list))

