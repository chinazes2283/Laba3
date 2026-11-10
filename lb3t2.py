import json
import os


# 1. Визначення ієрархії доменних виключень
class AppError(Exception):
    """Базовий клас для всіх доменних виключень застосунку.
    Наслідує виключно від Exception (а не від BaseException).
    """

    def __init__(self, message: str, error_code: str = "APP_ERR_000"):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self) -> str:
        return f"[{self.error_code}] {self.message}"

    def to_dict(self) -> dict:
        """Серіалізація виключення в словник (для логів чи мережевої передачі)."""
        return {
            "error_type": self.__class__.__name__,
            "error_code": self.error_code,
            "message": self.message,
        }


class ConfigValidationError(AppError):
    """Моделює помилку валідації конфігураційного поля."""

    def __init__(self, message: str, field_name: str, error_code: str = "VAL_ERR_001"):
        super().__init__(message, error_code)
        self.field_name = field_name

    def __str__(self) -> str:
        return f"[{self.error_code}] Помилка поля '{self.field_name}': {self.message}"


class ResourceNotFoundError(AppError):
    """Моделює помилку відсутності зовнішнього ресурсу чи файлу."""

    def __init__(self, message: str, resource_id: str, error_code: str = "RES_ERR_002"):
        super().__init__(message, error_code)
        self.resource_id = resource_id

    def __str__(self) -> str:
        return f"[{self.error_code}] Ресурс '{self.resource_id}' не знайдено: {self.message}"


class BusinessLogicError(AppError):
    """Моделює порушення бізнес-правил (наприклад, перевищення лімітів)."""

    def __init__(self, message: str, limit_value: float, error_code: str = "BIZ_ERR_003"):
        super().__init__(message, error_code)
        self.limit_value = limit_value

    def __str__(self) -> str:
        return f"[{self.error_code}] Порушення ліміту ({self.limit_value}): {self.message}"


# 2. Сервісні функції, що піднімають виключення
def validate_port(port: int):
    """Перевіряє коректність мережевого порту."""
    if not (1 <= port <= 65535):
        raise ConfigValidationError(
            message="Порт має бути в діапазоні від 1 до 65535",
            field_name="port"
        )
    print(f"Порт {port} успішно валідовано.")


def load_config_file(filepath: str) -> dict:
    """Завантажує файл конфігурації з демонстрацією ланцюжка виключень."""
    if not os.path.exists(filepath):
        # Ланцюжок виключень через raise ... from
        raise ResourceNotFoundError(
            message="Файл конфігурації фізично відсутній на дискі.",
            resource_id=filepath
        )
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        # Обгортаємо вбудовану помилку парсингу JSON у доменну з посиланням на причину через __cause__
        raise ConfigValidationError(
            message=f"Помилка синтаксису JSON: {e.msg}",
            field_name="config_json"
        ) from e


def process_transaction(amount: float, max_limit: float = 5000.0):
    """Обробка транзакції з використанням повторного піднесення (re-raising)."""
    if amount > max_limit:
        raise BusinessLogicError(
            message="Сума транзакції перевищує максимальний ліміт.",
            limit_value=max_limit
        )
    print(f"Транзакція на суму {amount} грн успішно виконана.")


# 3. Сценарії демонстрації
def run_scenarios():
    print("=== Демонстрація Завдання 2: Ієрархія доменних виключень ===")

    # Сценарій 1: Перехоплення конкретного виключення та категорії через базовий клас
    print("\n--- Сценарій 1: Перехоплення конкретного підкласу та базового AppError ---")
    try:
        validate_port(70000)
    except ConfigValidationError as e:
        print(f"[Перехоплено конкретний клас] {e}")
        print(f"Специфічний атрибут field_name: '{e.field_name}'")
        print(f"Серіалізація to_dict(): {e.to_dict()}")

    try:
        validate_port(-10)
    except AppError as e:
        print(f"[Перехоплено через базовий клас AppError] {e} (Код: {e.error_code})")

    # Сценарій 2: Ланцюжок виключень (raise ... from ...)
    print("\n--- Сценарій 2: Ланцюжок виключень через raise ... from ---")
    missing_file = "missing_settings.json"
    try:
        load_config_file(missing_file)
    except ResourceNotFoundError as e:
        print(f"[Перехоплено доменне виключення] {e}")
        print(f"Доступ до первинної причини (__cause__): {e.__cause__} ({type(e.__cause__)})")

    # Сценарій 3: Повторне піднесення (re-raising) без аргументів для побічної дії (логування)
    print("\n--- Сценарій 3: Повторне піднесення (re-raising) ---")
    try:
        try:
            process_transaction(12000.0)
        except BusinessLogicError as err:
            print(f"[Побічна дія всередині блоку] Запис у файл логів: збій ліміту ({err.error_code})")
            raise  # Повторне піднесення поточного виключення без втрати контексту стека
    except AppError as caught_err:
        print(f"[Зовнішній обробник прийняв виключення після ре-райзу] {caught_err}")


if __name__ == "__main__":
    run_scenarios()
