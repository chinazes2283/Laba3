# Абсолютний імпорт цілого модуля
import app_package.services as services
import app_package.exceptions as exceptions


def main():
    print("=== Запуск пакета app_package через __main__.py ===")

    # Використання імпортованих сервісів
    try:
        services.validate_port(8080)
        services.validate_port(99999)  # Викине помилку валідації
    except exceptions.ConfigValidationError as e:
        print(f"Перехоплено доменну помилку: {e} (Поле: {e.field_name})")

    # Демонстрація роботи __all__ (з обмеженням зірочкового імпорту)
    print("\n--- Демонстрація обмеження __all__ ---")
    from app_package import __all__ as exported_names
    print(f"Експортовані імена через __all__ в app_package: {exported_names}")


if __name__ == "__main__":
    main()
