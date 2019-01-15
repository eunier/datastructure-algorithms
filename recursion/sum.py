# no using recursion
def list_sum(num_list):
    the_sum = 0

    for i in num_list:
        the_sum += i
    return the_sum


input_list = [1, 2, 3, 4]
print(list_sum(input_list))
