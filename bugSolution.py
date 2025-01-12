def function_with_uncommon_error_fixed(a, b):
    if a == 0:
        return 0 #Handles the case of division by zero
    elif b == 0:
        return 0 #Handles the case of division by zero
    else:
        return b / a

result = function_with_uncommon_error_fixed(0, 10)
print(result)

result = function_with_uncommon_error_fixed(10,0)
print(result)

result = function_with_uncommon_error_fixed(10,20)
print(result)