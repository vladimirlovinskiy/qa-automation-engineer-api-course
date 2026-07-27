from typing import Any


def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    Args:
        actual (int): Фактический статус код
        expected (int): Ожидаемыый статус код
        AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, (
        "Incorrect response status code. " f"Expected stuts code: {expected}. " f"Actual status code: {actual}. "
    )


def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    Args:
        actual (Any): Фактическое значение.
        expected (Any): Ожидаемое значение.
        name (str): Название проверяемого поля.
    """
    assert actual == expected, (
        f'Incorrect value: "{name}". ' f'Expected value "{expected}". ' f'Actual value "{actual}". '
    )
