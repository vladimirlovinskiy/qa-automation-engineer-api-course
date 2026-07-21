from typing import Any

from jsonschema import validate
from jsonschema.validators import Draft202012Validator


def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instanse) заданной JSON-схеме (schema)

    Args:
        instance (Any): JSON-данные, которые нужно проверить
        schema (dict): Ожидаемая JSON-schema
    """
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
