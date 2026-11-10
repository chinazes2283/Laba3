from ..exceptions import ConfigValidationError


def validate_port(port: int) -> None:
    """Перевіряє коректність значення мережевого порту.

    Args:
        port (int): Числове значення порту для перевірки.

    Returns:
        None: Функція нічого не повертає у разі успіху.

    Raises:
        ConfigValidationError: Якщо порт виходить за межі діапазону 1–65535.
    """
    if not (1 <= port <= 65535):
        raise ConfigValidationError(
            message="Порт має бути в діапазоні від 1 до 65535",
            field_name="port"
        )
    print(f"[Validator] Порт {port} успішно валідовано.")
