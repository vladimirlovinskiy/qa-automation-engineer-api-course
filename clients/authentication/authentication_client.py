from typing import TypedDict

from httpx import Response


class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентифкацию
    """

    email: str
    password: str


class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """

    refreshToken: str


class AuthenticationClient:
    """Клиент для работы с /api/v1/authentication"""

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        Args:
            request (dict): Словарь с email и password

        Returns:
            Response: _description_
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации

        Args:
            request (RefreshRequestDict): Словарь с refreshToken

        Returns:
            Response: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)
