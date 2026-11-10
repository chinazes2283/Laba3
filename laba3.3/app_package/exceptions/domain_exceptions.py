class AppError(Exception):
    """Базовий клас доменних виключень."""

    def __init__(self, message: str, error_code: str = "ERR_000"):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self) -> str:
        return f"[{self.error_code}] {self.message}"

    def to_dict(self) -> dict:
        return {
            "error_type": self.__class__.__name__,
            "error_code": self.error_code,
            "message": self.message,
        }


class ConfigValidationError(AppError):
    """Помилка валідації даних конфігурації."""

    def __init__(self, message: str, field_name: str):
        super().__init__(message, error_code="VAL_001")
        self.field_name = field_name


class ResourceNotFoundError(AppError):
    """Помилка відсутності файлу чи ресурсу."""

    def __init__(self, message: str, resource_id: str):
        super().__init__(message, error_code="RES_002")
        self.resource_id = resource_id
