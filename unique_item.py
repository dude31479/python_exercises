"""If all the numbers in a list are the same except for one."""

def find_unique_num(arr):
    my_dict = {}
    for i in arr:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    unique = min(my_dict, key=my_dict.get)
    return unique