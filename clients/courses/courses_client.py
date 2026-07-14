from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class CoursesClient(APIClient):
    pass


def test():
    pass


def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    return CoursesClient(client=get_private_http_client(user))
