# Python client for Spacelift

Python client for Spacelift using GraphQL generation.

As a user, you should be using the top-level `Client` class, which is a thin wrapper around the generated GraphQL client.

Most of the time you will be using an API key to authenticate with the Spacelift API. Example usage:

```python
client = Client(url=os.getenv("SPACELIFT_API_URL"))

# Start a new session.
client.login_with_api_key(
    id=os.getenv("SPACELIFT_API_KEY_ID"),
    secret=os.getenv("SPACELIFT_API_KEY_SECRET"),
)

# Get details of a single context.
context_details = client.get_context_details(id="my-context-id")
print(f"Context details: {context_details.context}")

# Terminate the session (optional).
client.log_out()
```

If you want to contribute a method (either a query or a mutation), you should add a corresponding GraphQL snippet to the `graphql` directory and then run `make generate` (or simply `make`) to regenerate the client.

You can also extend the `Client` class in your code with custom methods by creating inline GraphQL snippets, using the underlying `execute` and `get_data` methods.
