# return a string from n converted to string based on a base
def to_str(n, base):
    convert_string = '0123456789ABCDF'
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]


output_array = {
    to_str(1234, 10),
    to_str(1234, 16),
    to_str(1234, 2),
}

for output in output_array:
    print(str(type(output)) + ': ' + str(output))
