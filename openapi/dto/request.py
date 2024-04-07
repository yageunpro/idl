from pydantic import BaseModel, EmailStr, Field


class AuthSignUpRQ(BaseModel):
    email: EmailStr = Field(description="user email")
    password: str = Field(description="user password", min_length=6)


class AuthSignInRQ(BaseModel):
    email: EmailStr = Field(description="user email")
    password: str = Field(description="user password", min_length=6)
