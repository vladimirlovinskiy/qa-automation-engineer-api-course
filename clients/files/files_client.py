from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """

    filename: str
    directory: str
    upload_file: str


class FileClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        Args:
            file_id (str): Идентификатор файла

        Returns:
            Response: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        Args:
            request (CreateFileRequestDict): Словарь с filename, directore, upload_file.

        Returns:
            Response: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request["upload_file"], "rb")},
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        Args:
            file_id (str): Идентификатор файла

        Returns:
            Response: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")


def get_files_client(user: AuthenticationUserDict) -> FileClient:
    """
    Функция создает эксземпляр FilesClient c уже настроенным HTTP-клиентом.

    Returns:
        FileClient: Готовый к использованию FilesClient.
    """
    return FileClient(client=get_private_http_client(user))
