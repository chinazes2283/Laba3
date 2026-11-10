# Відносний імпорт всередині пакету
from ..exceptions import ConfigValidationError


def validate_port(port: int) -> None:
    """Перевіряє коректність мережевого порту."""
    if not (1 <= port <= 65535):
        raise ConfigValidationError(
            message="Порт має бути в діапазоні від 1 до 65535",
            field_name="port"
        )
    print(f"[Validator] Порт {port} успішно валідовано.")
