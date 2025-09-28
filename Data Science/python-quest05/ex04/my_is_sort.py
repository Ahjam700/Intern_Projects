def my_is_sort(int_arr):
    if int_arr == sorted(int_arr) or int_arr == sorted(int_arr, reverse=True):
        return True
    return False

# Example usage:
int_arr1 = [1, 2, 3, 4, 5]       
int_arr2 = [5, 4, 3, 2, 1]       
int_arr3 = [3, 1, 4, 2, 5]
int_arr4 = [5, 4, 3, 2, 1]
