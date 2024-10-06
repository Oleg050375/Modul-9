def apply_all_func(int_list, *functions):
    return {x.__name__: x(int_list) for x in functions}

# ТЕСТ --------------------------------------------------------------------------------------------------

print(apply_all_func([6,20,15,9], max, min))
print(apply_all_func([6,20,15,9], len, sum, sorted))