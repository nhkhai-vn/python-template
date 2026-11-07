def greet(name: str) -> str:
    if not name.strip():
        raise ValueError("name is empty")
    return f"Hello, {name.strip()}!"
