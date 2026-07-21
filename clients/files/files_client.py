from httpx import Response

from clients.api_client import APIClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client,
)


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

    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Метод создания файла.

        Args:
            request (CreateFileRequestSchema): Словарь с filename, directore, upload_file.

        Returns:
            Response: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data=request.model_dump(by_alias=True, exclude={"upload_file"}),
            files={"upload_file": open(request.upload_file, "rb")},
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

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)


def get_files_client(user: AuthenticationUserSchema) -> FileClient:
    """
    Функция создает эксземпляр FilesClient c уже настроенным HTTP-клиентом.

    Returns:
        FileClient: Готовый к использованию FilesClient.
    """
    return FileClient(client=get_private_http_client(user))
