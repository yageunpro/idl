from pydantic import BaseModel, Field


class AuthSignUpRO(BaseModel):
    access_token: str = Field(description="access token")
    refresh_token: str = Field(description="refresh token")


class AuthSignInRO(BaseModel):
    access_token: str = Field(description="user")
    refresh_token: str = Field(description="user")
