import httpx

from generated.client import Client as BaseClient

# InvalidAPIKeyError is an exception that is raised when an invalid API key is
# used to log in.
class InvalidAPIKeyError(Exception):
    pass

# Client is a subclass of RawClient that adds convenience methods for handling
# authentication.
class Client(BaseClient):
    def login_with_api_key(self, id: str, secret: str) -> None:
        user = self.api_key_user(id, secret).api_key_user
        if user is None:
            raise InvalidAPIKeyError()
        
        self._set_token(user.jwt)

    def _set_token(self, token: str) -> None:
        # If the headers are None, set them to an empty dictionary.
        # Otherwise, simply add the bearer token to the existing headers.
        if self.headers is None:
            self.headers = {}

        self.headers["Authorization"] = f"Bearer {token}"
        self.http_client = httpx.Client(headers=self.headers)
