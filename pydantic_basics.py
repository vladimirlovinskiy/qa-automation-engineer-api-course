import uuid

from pydantic import BaseModel, EmailStr, Field, HttpUrl, ValidationError


class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name} {self.middle_name}"


class CourseSchema(BaseModel):

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=1)
    description: str = "Playwright course"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")


# 1) Стандартный способ:

# course_default_model = CourseSchema(
#     id="course-id",
#     title="Playwright",
#     maxScore=100,
#     description="Playwright",
#     estimatedTime="1 week",
# )

# # 2) Инициализация с использованием словаря:

# course_dict = {
#     "id": "course-id",
#     "title": "Playwright",
#     "minScore": 10,
#     "description": "Playwright",
#     "estimatedTime": "1 week",
# }
# course_dict_model = CourseSchema(**course_dict)

# # 3) Инициализация с использованием JSON:

# course_json = """
# {
#     "id": "123",
#     "title": "Playwright",
#     "maxScore": 100,
#     "description": "Playwright",
#     "estimatedTime": "1 week"
# }
# """
# course_json_model = CourseSchema.model_validate_json(course_json)


# print("1) Course default model:", course_default_model)
# print("2) Course dict model:", course_dict_model)
# print("3) Course JSON model:", course_json)


# course = CourseSchema()

# print(course)


# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course_id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    # Добавили иницилизацию вложенной модели FileSchema
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    # Добавили инициализацию вложенной модели
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="James",
        middleName="Alise",
    ),
)


print("Course default model:", course_default_model)
