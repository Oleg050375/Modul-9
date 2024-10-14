def is_prime(func):  # определение декоратора
    def prime(*args):  # определение внутренней функции декоратора с передачей параметров
        av = func(*args)  # присвоение переменной результата выполнения функции
        for i in range(2, (av // 2) + 1):
            if av % i == 0:
                return str(av) + '\nСоставное'
        return str(av) + '\nПростое'

    return prime  # взврат внутренней функции


@is_prime
def sum_three(a, b, c):  # определение функции
    return a + b + c


# ТЕСТ ----------------------------------------------------------------------------------------------------------------

nt = sum_three(1, 2, 3)
print(nt)
