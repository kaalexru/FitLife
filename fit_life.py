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


def check_range(value, min_value, max_value):
    """Проверяет, входит ли значение в допустимый диапазон."""
    return min_value <= value <= max_value


def float_ru(str):
    """локализация точки float."""
    return float(str.replace(",", "."))


def read_checked_value(
    prompt,
    value_type,
    min_value,
    max_value,
    error_message
):
    """Запрашивает значение, преобразует его и проверяет диапазон."""
    while True:
        try:
            value = value_type(input(prompt))

            if check_range(value, min_value, max_value):
                return value

        except ValueError:
            pass

        print(error_message)


while True:
    user_name = input("Как вас зовут? ").strip()
    if user_name:
        break
    print("Ошибка. Попробуйте еще раз")

user_age = read_checked_value(
    "Сколько вам лет? ",
    int,
    AGE_MIN,
    AGE_MAX,
    "Ошибка. Введите корректный возраст."
)

user_weight = read_checked_value(
    "Введите свой вес в килограммах: ",
    float_ru,
    WEIGHT_MIN_KG,
    WEIGHT_MAX_KG,
    "Ошибка. Введите корректный вес."
)

user_height = read_checked_value(
    "Введите свой рост в метрах: ",
    float_ru,
    HEIGHT_MIN_M,
    HEIGHT_MAX_M,
    "Ошибка. Введите корректный рост."
)

# расчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Расчет нормы воды в миллилитрах и литрах
water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml / ML_PER_LITER, 1)

# Вывод отчета
age_text = get_age_word(user_age)

print("\n")

print(f"Отчет для пользователя: {user_name}, {user_age} {age_text}\n")

print(f"Ваш индекс массы тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л в день\n")

print("Расчет окончен. Будьте здоровы!")
