def find_max(table: list[float|int]) -> float|int:
    if len(table) == 0:
        return None
    max_num = table[0]
    for i in range(0, len(table)):
        num = table[i]
        if num > max_num:
            max_num = num
    return max_num


input = [3,2,5,8,1]

print(max(input))