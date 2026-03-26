import uuid
from pydantic import BaseModel, Field, EmailStr


class CreateUserRequestSchema(BaseModel):
    email: EmailStr = Field(default=f"user@test.com")
    last_name: str = Field(alias="lastName", default="default_last")
    first_name: str = Field(alias="firstName", default="default_first")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber", default="+0085631625")


class UserSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr = Field(default=f"user@test.com")
    last_name: str = Field(alias="lastName", default="default_last")
    first_name: str = Field(alias="firstName", default="default_first")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber", default="+0085631625")


class CreateUserResponseSchema(BaseModel):
    user: UserSchema
