# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_PER_LITER = 1000

AGE_MIN = 18
AGE_MAX = 100

WEIGHT_MIN_KG = 30.0
WEIGHT_MAX_KG = 150.0

HEIGHT_MIN_M = 1.20
HEIGHT_MAX_M = 2.50


def get_age_word(age):
    """Возвращает правильное слово для возраста."""
    # Сначала проверяем исключения 11 – 14
    if 11 <= age % 100 <= 14:
        return "лет"

    # Окончание на 1
    if age % 10 == 1:
        return "год"

    # Окончание на 2 – 4
    if 2 <= age % 10 <= 4:
        return "года"

    # Все остальное
    return "лет"


while True:
    user_name = input("Как вас зовут? ").strip()
    if user_name:
        break
    print("Ошибка. Попробуйте еще раз")

while True:
    try:
        user_age = int(input("Сколько вам лет? "))
    except ValueError:
        print("Ошибка. Попробуйте еще раз.")
    else:
        if AGE_MIN <= user_age <= AGE_MAX:
            break
        else:
            print("Ошибка. Введите корректный возраст.")

while True:
    try:
        user_weight = float(input("Введите свой вес в килограммах: "))
    except ValueError:
        print("Ошибка. Попробуйте еще раз.")
    else:
        if WEIGHT_MIN_KG <= user_weight <= WEIGHT_MAX_KG:
            break
        else:
            print("Ошибка. Введите корректный вес.")

while True:
    try:
        user_height = float(input("Введите рост в метрах, например 1.75: "))
    except ValueError:
        print("Ошибка попробуйте еще раз.")
    else:
        if HEIGHT_MIN_M <= user_height <= HEIGHT_MAX_M:
            break
        else:
            print("Ошибка. Введите корректный рост.")

# расчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Расчет нормы воды в миллилитрах и литрах
water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml / ML_PER_LITER, 1)

# Вывод отчета
print("\n")

print(f"Отчет для пользователя: {user_name}, ", end="")
print(f"{user_age} {get_age_word(user_age)}\n")

print(f"Ваш индекс массы тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л в день\n")

print("Расчет окончен. Будьте здоровы!")
