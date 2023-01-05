# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in
# Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    result = []
    n = str(num)
    remainder = len(n)
    for digit in n:
        remainder -= 1
        if digit != '0':
            result.append(str(int(digit) * 10 ** remainder))
    return ' + '.join(result)

print(expanded_form(12))     # '10 + 2');
print(expanded_form(42))     # '40 + 2');
print(expanded_form(70304))  # '70000 + 300 + 4');
