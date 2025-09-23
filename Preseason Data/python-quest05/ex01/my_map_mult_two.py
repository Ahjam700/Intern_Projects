def my_map_mult_two(int_array):
    result = []
    
    for num in int_array:
        result.append(num * 2)
    return result

original_array = [4, 8, 12]
new_array = my_map_mult_two(original_array)


