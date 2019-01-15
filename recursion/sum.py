# no using recursion
def list_sum(num_list):
    the_sum = 0

    for i in num_list:
        the_sum += i
    return the_sum


def list_sum_rec(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])


input_list = [1, 2, 3, 4]
print(list_sum(input_list))
print(list_sum_rec(input_list))
