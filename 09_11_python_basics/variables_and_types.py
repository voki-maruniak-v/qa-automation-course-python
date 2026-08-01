game_name = "GTA V"
build_number = 3
test_duration = 2.5
total_tests = 15
passed_tests = 12
build_passed = True
tester_name = 'Vadya'

print("Имя игры:", game_name, type(game_name))
print("Номер билда:", build_number, type(build_number))
print("Длительность теста:", test_duration, type(test_duration))
print("Общее количество тестов:", total_tests, type(total_tests))
print("Пройдено тестов:", passed_tests, type(passed_tests))
print("Билд пройден:", build_passed, type(build_passed))
print("Имя тестера:", tester_name, type(tester_name))

print("Пройдено тестов:", passed_tests, "Из", total_tests)

test_result = 40
print("Результат теста:", test_result, "Тип данных test_result:", type(test_result))

passed_tests = passed_tests - 1
build_passed = False
test_result = "Failed"
print("Пройдено тестов", passed_tests)
print("Билд пройден", build_passed)
print("Результат теста", test_result)

print("Тип данных test_result после изменения:", type(test_result))

first_build = 2
second_build = 2
another_build = first_build

print("ID первого билда:", id(first_build))
print("ID второго билда:", id(second_build))
print("ID другого билда:", id(another_build))
