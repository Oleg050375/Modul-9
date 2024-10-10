class StepValueError(ValueError):  # создание класса ошибки
    def __init__(self, message):
        self.message = message

    pass


class iterator:  # создание класса итератора
    def __init__(self, start, stop, step=1):
        if step == 0:  # проверка на корректность значения шага итерации
            raise StepValueError('Шаг не может быть равным нулю')  # генерация ошибки значения шага итерации
        else:
            self.start = start
            self.stop = stop
            self.step = step
            self.pointer = start  # задание начального значения счётчика

    def __iter__(self):
        self.pointer = self.start  # сброс занчения счётчика при вызове объекта
        return self

    def __next__(self):
        if self.step > 0:  # проверка направления итерации
            if self.pointer > self.stop:  # проверка на предел итерации
                raise StopIteration  # генерация ошибки окончания итерации
            else:
                a = self.pointer
                self.pointer += self.step  # итерация счётчика
                return a
        else:
            if self.pointer < self.stop:  # проверка на предел итерации
                raise StopIteration  # генерация ошибки окончания итерации
            else:
                a = self.pointer
                self.pointer += self.step  # итерация счётчика
                return a


# ТЕСТ ----------------------------------------------------------------------------------------------------------------

try:
    iter1 = iterator(1, 5, 0)
except StepValueError:
    print('Шаг указан неверно')

iter2 = iterator(6, 15, 2)
iter3 = iterator(-5, 1)
iter4 = iterator(5, 1, -1)
iter5 = iterator(10, 1)

for i in iter2:
    print(i, ' ', end='')
print()

for i in iter3:
    print(i, ' ', end='')
print()

for i in iter4:
    print(i, ' ', end='')
print()

for i in iter5:
    print(i, ' ', end='')
print()
