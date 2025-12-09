def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def multiply(*args):
    sum = 1
    for i in args:
        sum *= i
    return sum

def clear_list(list_to_clear:list) -> list:
    new_list = list()
    for item in list_to_clear:
        if item == " " or item == "" or item == "\n":
            continue
        else:
            new_list.append(item)
    return new_list

if __name__ == "__main__":
    
    PART_1 = False

    file_name = r"day_6/codes.txt"
    codes = ""
    with open(file_name, "r") as file:
        codes = file.readlines()
    
    if PART_1:
        operations = clear_list(codes[-1].removesuffix("\n").split(" "))
        
        values_list = list()
        for i in range(0, len(codes)-1):
            value_classes = clear_list(codes[i].removesuffix("\n").split(" "))
            values_list.append(value_classes)
        
        result = list()
        current_result_list = list()
        for i, operation in enumerate(operations):
            if operation == "+":
                funf_op = add
                current_result = 0
            else:
                funf_op = multiply
                current_result = 1

            for value_classes in values_list:
                values_to_use = int(value_classes[i])
                current_result = funf_op(current_result, values_to_use)
            current_result_list.append(current_result)
        
        print(sum(current_result_list))
    
    else:
        operation_ranges = list()

        start = 0
        end = None
        last_op = codes[-1][0]

        for i in range(1, len(codes[-1])):
            operation = codes[-1][i]
            end = i
            if operation == "+" or operation == "*":
                tuple_op = (last_op, start, end)
                start = i
                last_op = operation
                operation_ranges.append(tuple_op)
        max_pos = max([len(x) for x in codes])
        tuple_op = (last_op, start, max_pos)

        operation_ranges.append(tuple_op)

        # print(operation_ranges)

        results = list()
        for operation, start, end in operation_ranges:
            values_for_operation = list()
            for i in range(start, end):
                number_str = ''
                for line in codes[0:-1]:
                    number_str +=  line[i]
                values_for_operation.append(number_str)
            
            op_funf = add if operation == "+" else multiply
            current_sum = 0 if operation == "+" else 1
            for value in values_for_operation:
                value_clean = value.strip()
                if str.isnumeric(value_clean):
                    current_sum = op_funf(current_sum, int(value_clean))
            results.append(current_sum)
        print(sum(results))
                

                

                



