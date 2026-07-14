from httpx import Client


def get_public_http_client() -> Client:
    """
    Функция создает экземпляр класса httpx.Client с базовыми настройками.

    Returns:
        Client: Готовый к использованию объект httpx.Client
    """
    return Client(timeout=100, base_url="http://localhost:8000")
