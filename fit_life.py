# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_PER_LITER = 1000

user_name = input("Как вас зовут? ")

while True:
    try:
        user_age = int(input("Сколько вам лет? "))
    except ValueError:
        print("Ошибка попробуйте еще раз")
    else:
        break

while True:
    try:
        user_weight = float(input("Введите свой вес в килограммах "))
    except ValueError:
        print("Ошибка попробуйте еще раз")
    else:
        break

while True:
    try:
        user_height = float(input("Введите рост в метрах, например 1.75 "))
    except ValueError:
        print("Ошибка попробуйте еще раз")
    else:
        break

# расчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Расчет нормы воды в миллилитрах и литрах
water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml / ML_PER_LITER, 1)

# Вывод отчета
print("\n\n")
print(f"Отчет для пользователя: {user_name}, {user_age} лет\n")
print(f"Ваш индекс массы тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день\n")

print("Расчет окончен. Будьте здоровы!")
