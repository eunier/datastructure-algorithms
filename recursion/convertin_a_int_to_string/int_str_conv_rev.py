# return a reversed string from n which is converted to string based on a base
def to_str_rev(n, base):
    convert_string = '0123456789ABCDF'
    if n < base:
        return convert_string[n]
    else:
        return convert_string[n % base] + to_str_rev(n // base, base)


output_rev_array = {
    to_str_rev(1234, 10),
    to_str_rev(1234, 16),
    to_str_rev(1234, 2),
}

for output in output_rev_array:
    print(str(type(output)) + ': ' + str(output))
