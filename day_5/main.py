class FruitSort:
    def __init__(self):
        self._id_map = dict()
        self.spoiled = set()
        self.fresh = set()

    def _check_id(self, id:int) -> bool:
        for start, end in self._id_map.items():
            if start <= id <= end:
                return True
        return False

    def add_id(self, id_start:int, id_end:int) -> None:
        if self._id_map.get(id_start) is not None:
            first = self._id_map.get(id_start)
            id_end = id_end if id_end > first else first
        self._id_map[id_start] = id_end
    
    def add_fruit(self, id:int) -> None:
        if self._check_id(id):
            self.fresh.add(id)
        else:
            self.spoiled.add(id)
    
    def get_qntd(self) -> tuple:
        return len(self.fresh), len(self.spoiled)
    
    def sort_uniques(self) -> list:
        sorted_entries = sorted(self._id_map.keys())

        current_start = sorted_entries[0]
        current_end = self._id_map[current_start]
        new_map = {}

        for entry_start in sorted_entries[1:]:
            entry_end = self._id_map[entry_start]
            if entry_start <= current_end:
                current_end = max(entry_end, current_end)

            else:
                new_map[current_start] = current_end
                current_start = entry_start
                current_end = entry_end
        new_map[current_start] = current_end

        self._id_map = new_map

    def get_max_fresh_id_sum(self) -> int:
        id_sum = 0
        for start, end in self._id_map.items():
            id_sum += end - start + 1
        return id_sum


if __name__ == "__main__":
    
    file_name = r"day_5/codes.txt"
    codes = ""
    with open(file_name, "r") as file:
        codes = file.readlines()
    print(len(codes))
    
    fruit_sort = FruitSort()
    fruit_id_ranges = list()
    fruits = list()

    for line in codes:
        if len(line) <= 1:
            continue
        
        if '-' in line:
            id_tuple = line.split('-')
            fruit_id_ranges.append((int(id_tuple[0]), int(id_tuple[1])))
        else:
            fruits.append(int(line))    

    for start, end in fruit_id_ranges:
        fruit_sort.add_id(start, end)
    
    for fruit in fruits:
        fruit_sort.add_fruit(fruit)

    fruit_sort.sort_uniques()
    
    fresh, spoiled = fruit_sort.get_qntd()
    print(f"{spoiled} Rotten fruits\n{fresh} Fresh Fruits")

    unique_fresh_ids = fruit_sort.get_max_fresh_id_sum()
    print(f"Max Fresh fruits: {unique_fresh_ids}")

    sorted = sorted(fruit_sort._id_map.keys())
    # for x in sorted:
    #     print(x, "  \t", fruit_sort._id_map[x] )

        



