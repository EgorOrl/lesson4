from sys import argv

script_name, time_hour, money_hour, bonus = argv

print("Название скрипта: ", script_name)
print("Количество отработанных часов: ", time_hour)
print("Ставка рублей в час:: ", money_hour)
print("Премия: ", bonus)
print("Зарплата:", (int(time_hour) * int(money_hour) + int(bonus)))
