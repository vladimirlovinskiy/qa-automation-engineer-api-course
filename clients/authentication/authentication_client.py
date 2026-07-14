from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class Token(TypedDict):
    """
    Описание структуры аутентификационных токенов.
    """

    tokenType: str
    accessToken: str
    refreshToken: str


class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентифкацию
    """

    email: str
    password: str


class LoginResponseDict(TypedDict):
    """
    Описание структуры ответа аутентификации.
    """

    token: Token


class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """

    refreshToken: str


class AuthenticationClient(APIClient):
    """Клиент для работы с /api/v1/authentication"""

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        Args:
            request (dict): Словарь с email и password

        Returns:
            Response: Ответ от сервера в виде объекта httpx.Response
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

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        """_summary_

        Args:
            request (LoginRequestDict): _description_

        Returns:
            _type_: _description_
        """
        response = self.login_api(request)  # Отправляем запрос на аутентикацию
        return response.json()  # Извлекаем JSON из ответа


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создает экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    Returns:
        AuthenticationClient: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
