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


if __name__ == "__main__":
    
    file_name = r"day_3/codes.txt"
    codes = ""
    with open(file_name, "r") as file:
        codes = file.readlines()
    
    voltage_sum = 0
    for bank_battery_line in codes:
        bank_battery = int(bank_battery_line)
        max_pair = find_max_pair(bank_battery)
        print(f"bank: {bank_battery}, max pair found: {max_pair}")
        voltage_sum += max_pair
    print(f"Max joltage found: {voltage_sum}")

