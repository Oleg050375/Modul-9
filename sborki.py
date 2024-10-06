first_str = ['Киборг','Чук','Прграммист','Моня','Варик']
second_str = ['Задание','Git','Нечто','Java','Комп','Низший']

first_result = [len(x) for x in first_str if len(x) >= 5]
second_result = [(x,y) for x in first_str for y in second_str if len(x) == len(y)]
third_result = {x:len(x) for x in first_str + second_str if len(x) % 2 == 0}

# ТЕСТ --------------------------------------------------------------------------------------------------

print(first_result)
print(second_result)
print(third_result)