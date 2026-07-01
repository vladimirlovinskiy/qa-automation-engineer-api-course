from typing import Any

from httpx import URL, Client, QueryParams, Response
from httpx._types import RequestData, RequestFiles


class APIClient:
    def __init__(self, client: Client) -> None:
        """Базовый API клиент, принимающий объект httpx.Client.
        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
        """
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """Выполняет GET-запрос.

        Args:
            url (URL | str): URL-адрес эндпоинта
            params (QueryParams | None, optional): GET-апарметры запроса (например, ?key=value). Defaults to None.

        Returns:
            Response: Объект Response с данным ответа.
        """
        return self.client.get(url, params=params)

    def post(
        self,
        url: URL | str,
        json: Any | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
    ) -> Response:
        """Выполняет POST-запрос.

        Args:
            url (URL | str): URL-адрес эндпоинта
            json (Any | None, optional): Данные в формате JSON. Defaults to None.
            data (RequestData | None, optional): Форматированныые данные формы (например, application/x-www-form-urlencoder). Defaults to None.
            files (RequestFiles | None, optional): Файлы для загрузки на сервер. Defaults to None.

        Returns:
            Response: Response с данными ответа.
        """
        return self.client.post(url, json=json, data=data, files=files)

    def patch(
        self,
        url: URL | str,
        json: Any | None = None,
    ) -> Response:
        """Выполняется PATCH-запрос.

        Args:
            url (URL | str): URL-адрес эндпоинта
            json (Any | None, optional): Данные в формате JSON. Defaults to None.

        Returns:
            Response: Response с данными ответа.
        """
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        """Выполняется DELETE-запрос.

        Args:
            url (URL | str): URL-адрес эндпоинта

        Returns:
            Response: Response с данными ответа.
        """
        return self.client.delete(url)
