# Вибірковий імпорт конкретного виключення
from ..exceptions import ResourceNotFoundError


def parse_config_file(filename: str) -> str:
    """Симулює читання файлу конфігурації."""
    import os
    if not os.path.exists(filename):
        raise ResourceNotFoundError(
            message="Конфігураційний файл не знайдено на диску.",
            resource_id=filename
        )
    return "конфігурація_завантажена"
