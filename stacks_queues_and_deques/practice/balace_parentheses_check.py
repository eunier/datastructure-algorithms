def balance_check(string):
    # edge case check
    if len(string) % 2 != 0:
        return False

    opening = set('({[')
    matches = {
        ('(', ')'),
        ('{', '}'),
        ('[', ']')
    }

    stack = []

    for letter in string:
        if letter in opening:
            stack.append(letter)
        else:
            last_open = stack.pop()

            if (last_open, letter) not in matches:
                return False

    return len(stack) == 0


print(balance_check('{}'))
print(balance_check('{}{{{{}}}}[][][[[]]][({})]'))

print(balance_check('{{{{}{{{{'))
