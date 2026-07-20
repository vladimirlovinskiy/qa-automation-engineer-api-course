from pydantic import BaseModel


class AdressSchema(BaseModel):
    city: str
    zip_code: str


class UserSchema(BaseModel):
    id: int
    name: str
    adress: AdressSchema


user = UserSchema(
    id=1,
    name="Alice",
    adress={"city": "New York", "zip_code": "10001"},
)

print(user.model_dump_json())
