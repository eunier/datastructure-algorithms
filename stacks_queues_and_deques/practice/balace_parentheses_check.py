def balance_check(string):
    # edge check
    if len(string) % 2 != 0:
        return False

    opening = set('{[(')
    match = {
        ('{', '}'),
        ('[', ']'),
        ('(', ')')
    }

    stack = []

    for letter in string:
        if letter in opening:
            stack.append(letter)
        else:
            last_opening = stack.pop()

            if (last_opening, letter) not in match:
                return False

    return len(stack) == 0


print(balance_check('{}'))
print(balance_check('{}{{{{}}}}[][][[[]]][({})]'))

print(balance_check('{{{{}{{{{'))

