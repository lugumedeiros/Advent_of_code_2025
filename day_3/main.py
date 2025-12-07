def find_max_pair(battery_bank:int) -> int:
    def int_to_list(int_value) -> list:
        return list(str(int_value))
    
    def pair_to_int(a:str, b:str) -> int:
        return int(a + b)
    
    batteries = int_to_list(battery_bank)
    bank_len = len(batteries)

    msd_id = -2
    lsd_id = -1
    
    for current_bat_idx in range(bank_len-3, -1, -1):
        current_bat = batteries[current_bat_idx]
        msd_bat = batteries[msd_id]
        lsd_bat = batteries[lsd_id]

        if current_bat >= msd_bat:
            if msd_bat > lsd_bat:
                lsd_id = msd_id
            msd_id = current_bat_idx

    battery_pair = pair_to_int(batteries[msd_id], batteries[lsd_id])
    return battery_pair

# --------- Part 2 --------- #

def get_first_max(int_list:list, start:int, end:int) -> int:
    """returns the leading max value searching from left to right"""
    if end - start < 1:
        raise ValueError("Invalid op")
    if end - start == 1:
        return start
    
    max_value_id = start
    for idx in range (start+1, end):
        if int_list[idx] > int_list[max_value_id]:
            max_value_id = idx
        if int_list[max_value_id] == 9:
            break
    return max_value_id

def find_max_of_twelve(battery_bank:int) -> int:
    def int_to_list(int_value) -> list:
        str_list = list(str(int_value))
        return [int(x) for x in str_list]
    
    def list_to_int(list_value) -> int:
        str_list = [str(x) for x in list_value]
        return int("".join(str_list))
    
    batteries_to_find = 12
    batteries = int_to_list(battery_bank)
    bank_len = len(batteries)

    start_limit = 0
    end_limit = bank_len - batteries_to_find
    selected_batteries_ids = list()
    for _ in range(batteries_to_find):
        battery_id = get_first_max(batteries, start_limit, end_limit+1)
        selected_batteries_ids.append(battery_id)
        start_limit = battery_id + 1
        end_limit += 1
    
    real_value_list = [batteries[idx] for idx in selected_batteries_ids]
    return list_to_int(real_value_list)

    

if __name__ == "__main__":
    
    file_name = r"day_3/codes.txt"
    codes = ""
    with open(file_name, "r") as file:
        codes = file.readlines()
    
    voltage_sum = 0
    for bank_battery_line in codes:
        bank_battery = int(bank_battery_line)
        
        # max_config = find_max_pair(bank_battery)
        max_config = find_max_of_twelve(bank_battery)

        print(f"bank: {bank_battery}, max pair found: {max_config}")
        voltage_sum += max_config
    print(f"Max joltage found: {voltage_sum}")

