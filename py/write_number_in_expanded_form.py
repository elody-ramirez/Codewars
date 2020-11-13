# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in
# Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    result = ''
    n = list(map(int, str(num)))
    remainder = len(n)
    for i in range(0, len(n)):
        remainder -= 1
        if n[i] != 0:
            result+=str(n[i])
            for i in range(0, remainder):
                result+='0'
            result += ' + '
    if result[-3:] == ' + ':
        result = result[:-3]
    return result

print(expanded_form(12))     # '10 + 2');
print(expanded_form(42))     # '40 + 2');
print(expanded_form(70304))  # '70000 + 300 + 4');
