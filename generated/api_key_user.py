# Generated by ariadne-codegen
# Source: graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class APIKeyUser(BaseModel):
    api_key_user: Optional["APIKeyUserApiKeyUser"] = Field(alias="apiKeyUser")


class APIKeyUserApiKeyUser(BaseModel):
    jwt: str
