from typing import Any, Dict


class AppError(Exception):
    """Базовий клас для всіх доменних виключень застосунку.

    Attributes:
        message (str): Текстовий опис помилки.
        error_code (str): Унікальний код помилки.
    """

    def __init__(self, message: str, error_code: str = "ERR_000") -> None:
        super().__init__(message)
        self.message: str = message
        self.error_code: str = error_code

    def __str__(self) -> str:
        return f"[{self.error_code}] {self.message}"

    def to_dict(self) -> Dict[str, Any]:
        """Серіалізує інформацію про виключення у словник.

        Returns:
            Dict[str, Any]: Словник із полями error_type, error_code та message.
        """
        return {
            "error_type": self.__class__.__name__,
            "error_code": self.error_code,
            "message": self.message,
        }


class ConfigValidationError(AppError):
    """Помилка валідації даних конфігурації.

    Attributes:
        field_name (str): Ім'я поля, яке не пройшло перевірку.
    """

    def __init__(self, message: str, field_name: str) -> None:
        super().__init__(message, error_code="VAL_001")
        self.field_name: str = field_name


class ResourceNotFoundError(AppError):
    """Помилка відсутності файлу чи зовнішнього ресурсу.

    Attributes:
        resource_id (str): Ідентифікатор або шлях до не знайденого ресурсу.
    """

    def __init__(self, message: str, resource_id: str) -> None:
        super().__init__(message, error_code="RES_002")
        self.resource_id: str = resource_id
