import os


def scenario_1_basic_parsing():
    """Сценарій 1: Базова конструкція try/except.
    Предметна область: Читання конфігураційного числа з файлу конфігурації.
    Очікувані виключення: FileNotFoundError (якщо файлу не існує), 
    ValueError (якщо вміст неможливо перетворити на число).
    Заборонено використовувати голий 'except:'.
    """
    print("\n--- Сценарій 1: Базовий try/except (Парсинг числа з файлу) ---")
    filename = "config_port.txt"

    # Шлях А: Успішне створення файлу та читання коректного числа
    print("[Успішний шлях] Створюємо правильний конфігураційний файл...")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("8080")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            port = int(content)
            print(f"Успішно зчитано порт: {port}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Помилка під час зчитування конфігурації: {e}")

    # Шлях Б: Помилка — файл містить нечислові дані
    print("\n[Шлях з помилкою] Записуємо некоректні дані у файл...")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("invalid_port_number")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            port = int(content)
            print(f"Зчитано порт: {port}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Перехоплено очікувану помилку (некоректні дані): {e}")

    # Прибираємо тимчасовий файл
    if os.path.exists(filename):
        os.remove(filename)


def scenario_2_full_try_except_else_finally():
    """Сценарій 2: Повна конструкція try/except/else/finally.
    Предметна область: Конвертація та розрахунок бюджету за користувацьким введенням.
    Очікувані виключення: ZeroDivisionError (ділення на нуль), ValueError (нечисловий ввід).
    Блок else виконується лише за відсутності виключень (успішний шлях).
    Блок finally виконується завжди (для логування завершення операції).
    """
    print("\n--- Сценарій 2: Повний try/except/else/finally (Розрахунок бюджету) ---")

    test_cases = [
        ("1000", "5"),    # Успішний шлях (бюджет 1000, 5 днів)
        ("1000", "0"),    # Шлях з помилкою ділення на нуль
        ("abc", "2")      # Шлях з помилкою нечислового введення
    ]

    for budget_str, days_str in test_cases:
        print(f"\nТестуємо вхідні дані: budget='{budget_str}', days='{days_str}'")
        try:
            budget = float(budget_str)
            days = int(days_str)
            daily_allowance = budget / days
        except (ValueError, ZeroDivisionError) as e:
            print(f"[Помилка] Неможливо розрахувати бюджет: {e}")
        else:
            # Виконується лише тоді, коли не виникло жодного виключення в try
            print(f"[Else блок] Успішно! Щоденний ліміт складає: {daily_allowance:.2f} грн")
        finally:
            # Виконується завжди, гарантуючи фіксацію спроби розрахунку
            print("[Finally блок] Операцію розрахунку завершено (ресурси звільнено).")


def scenario_3_multiple_exceptions():
    """Сценарій 3: Перехоплення кількох типів виключень одним блоком except.
    Предметна область: Доступ до даних у словнику конфігурації за ключем та індексом.
    Очікувані виключення: KeyError (немає ключа) та IndexError (невірний індекс масиву).
    Об'єднані в один блок except (KeyError, IndexError), оскільки логіка обробки 
    (повернення значення за замовчуванням) для них однакова.
    """
    print("\n--- Сценарій 3: Множинне перехоплення except (KeyError, IndexError) ---")

    app_config = {
        "hosts": ["localhost", "127.0.0.1"],
        "timeout": 30
    }

    # Шлях А: Успішний доступ до існуючого елемента
    print("[Успішний шлях] Звертаємося до існуючого хоста за індексом 0...")
    try:
        host = app_config["hosts"][0]
        print(f"Знайдено хост: {host}")
    except (KeyError, IndexError) as e:
        print(f"Помилка конфігурації: відсутній ключ або індекс поза межами ({e})")

    # Шлях Б: Помилка — неіснуючий ключ або вихід за межі списку
    print("\n[Шлях з помилкою] Звертаємося до неіснуючого індексу списку [5]...")
    try:
        host = app_config["hosts"][5]
        print(f"Знайдено хост: {host}")
    except (KeyError, IndexError) as e:
        print(f"Перехоплено очікувану помилку (KeyError або IndexError): {e}")


def demonstrate_context_manager():
    """Демонстрація використання контекстного менеджера (with).
    Пояснення: оператор with автоматично викликає метод __exit__() ресурсу 
    (наприклад, закриття файлу або з'єднання) при виході з блоку, 
    навіть якщо всередині виникне непередбачене виключення. 
    Це повністю замінює громіздку та схильну до помилок конструкцію try/finally із ручним викликом .close().
    """
    print("\n--- Демонстрація контекстного менеджера (with) ---")
    filename = "demo_notes.txt"

    # Використання with гарантує закриття файлу без необхідності писати f.close() у блоці finally
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Системний лог: з'єднання стабільне.")
    
    print(f"Файл '{filename}' успішно записано та автоматично закрито через контекстний менеджер.")

    # Читаємо файл через with
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
        print(f"Вміст файлу: {data}")

    if os.path.exists(filename):
        os.remove(filename)


def main():
    # Запуск усіх сценаріїв
    scenario_1_basic_parsing()
    scenario_2_full_try_except_else_finally()
    scenario_3_multiple_exceptions()
    demonstrate_context_manager()


if __name__ == "__main__":
    main()
