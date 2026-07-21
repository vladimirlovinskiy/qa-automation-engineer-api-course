from httpx import Response

from clients.api_client import APIClient
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema,
    RefreshRequestSchema,
)
from clients.public_http_builder import get_public_http_client


class AuthenticationClient(APIClient):
    """Клиент для работы с /api/v1/authentication"""

    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        Args:
            request (dict): Словарь с email и password

        Returns:
            Response: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/authentication/login",
            json=request.model_dump(by_alias=True),
        )

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации

        Args:
            request (RefreshRequestDict): Словарь с refreshToken

        Returns:
            Response: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/authentication/refresh",
            json=request.model_dump(by_alias=True),
        )

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """
        Метод для логина

        Args:
            request (LoginRequestSchema): Словарь для запроса аутентификации

        Returns:
            _type_: Возвращает структуру ответа аутентификации
        """
        response = self.login_api(request)  # Отправляем запрос на аутентикацию
        return LoginResponseSchema.model_validate_json(response.text)  # Извлекаем JSON из ответа


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создает экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    Returns:
        AuthenticationClient: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
